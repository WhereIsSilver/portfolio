import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# =====================================================================
# ÉTAPE 1 : CHARGEMENT ET IMPUTATION DES DONNÉES D'ENTRAÎNEMENT (TRAIN)
# =====================================================================
try:
    donnees_train = pd.read_csv('billets.csv', sep=';')
except FileNotFoundError:
    print("Erreur : Le fichier 'billets.csv' est introuvable pour l'entraînement.")
    sys.exit(1)

# Imputation chirurgicale de margin_low par régression linéaire
train_avec_marge = donnees_train[donnees_train['margin_low'].notna()]
colonnes_marge = ['diagonal', 'height_left', 'height_right', 'margin_up', 'length']

modele_marge = LinearRegression()
modele_marge.fit(train_avec_marge[colonnes_marge], train_avec_marge['margin_low'])

# Remplacement ciblé uniquement sur les valeurs manquantes
nan_mask_train = donnees_train['margin_low'].isna()
if nan_mask_train.any():
    donnees_train.loc[nan_mask_train, 'margin_low'] = modele_marge.predict(donnees_train.loc[nan_mask_train, colonnes_marge])

# Préparation des variables pour la classification
toutes_les_colonnes = ['diagonal', 'height_left', 'height_right', 'margin_low', 'margin_up', 'length']
X = donnees_train[toutes_les_colonnes]
y = donnees_train['is_genuine']

# Découpage éthique et stratifié (Équilibre des classes et sans data leakage)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


# =====================================================================
# ÉTAPE 2 : MISE EN CONCURRENCE DES 4 MODÈLES & ARBITRAGE
# =====================================================================
# 1. Configuration des 3 modèles supervisés dans des Pipelines étanches
pipelines_supervises = {
    "Régression Logistique": Pipeline([('scaler', StandardScaler()), ('model', LogisticRegression(random_state=42))]),
    "KNN": Pipeline([('scaler', StandardScaler()), ('model', KNeighborsClassifier())]),
    "Random Forest": Pipeline([('scaler', StandardScaler()), ('model', RandomForestClassifier(random_state=42))])
}

modeles_entraines = {}
seuil_securite = 0.9

print("--- ÉVALUATION ET MISE EN CONCURRENCE DES MODÈLES (SEUIL 0.9) ---")

# Entraînement et évaluation des modèles supervisés
for nom, pipe in pipelines_supervises.items():
    pipe.fit(X_train, y_train)
    probs = pipe.predict_proba(X_test)[:, 1]
    predictions_09 = np.where(probs >= seuil_securite, 1, 0)
    
    modeles_entraines[nom] = pipe
    
    # Affichage de la matrice de confusion demandée par le projet
    cm = confusion_matrix(y_test, predictions_09)
    print(f"\n[+] Matrice de confusion : {nom}")
    print(f"    Vrais Négatifs (Faux détectés): {cm[0][0]} | Faux Positifs (Vrais ratés): {cm[0][1]}")
    print(f"    Faux Négatifs (Faux acceptés): {cm[1][0]} | Vrais Positifs (Vrais validés): {cm[1][1]}")

# 2. Cas du K-Means (Non supervisé utilisé pour la prédiction via ses centroïdes)
pipe_kmeans = Pipeline([('scaler', StandardScaler()), ('model', KMeans(n_clusters=2, random_state=42))])
pipe_kmeans.fit(X_train)

# Cartographie du cluster majoritaire pour les vrais billets (Traduction)
pred_train_clusters = pipe_kmeans.predict(X_train)
mapping_cluster = 1 if y_train[pred_train_clusters == 0].mean() > 0.5 else 0

# Prédiction K-means sur le jeu de test
pred_test_clusters = pipe_kmeans.predict(X_test)
predictions_kmeans = np.where(pred_test_clusters == mapping_cluster, 1, 0)

modeles_entraines["K-Means"] = (pipe_kmeans, mapping_cluster)

# Affichage de la matrice de confusion pour le K-Means
cm_km = confusion_matrix(y_test, predictions_kmeans)
print(f"\n[+] Matrice de confusion : K-Means (Non Supervisé)")
print(f"    Vrais Négatifs: {cm_km[0][0]} | Faux Positifs: {cm_km[0][1]}")
print(f"    Faux Négatifs: {cm_km[1][0]} | Vrais Positifs: {cm_km[1][1]}")


# ---------------------------------------------------------------------
# ARBITRAGE DU DATA SCIENTIST : FORCE LE CHOIX DE LA RÉGRESSION LOGISTIQUE
# ---------------------------------------------------------------------
meilleur_nom = "Régression Logistique"
print(f"\n🏆 Choix stratégique retenu pour la production : {meilleur_nom}")

# Réentraînement final sur la TOTALITÉ des données pour maximiser les performances
meilleur_modele = modeles_entraines[meilleur_nom]
meilleur_modele.fit(X, y)


# =====================================================================
# ÉTAPE 3 : FONCTION DE DÉTECTION SUR LES NOUVEAUX BILLETS
# =====================================================================
def predire_binaire(donnees_a_predire):
    """
    Prend un DataFrame de billets, applique l'imputation par régression linéaire,
    et effectue la prédiction finale binaire via le pipeline au seuil strict de 0.9.
    """
    # Imputation ciblée si valeurs manquantes dans margin_low
    case_vide = donnees_a_predire['margin_low'].isna()
    if case_vide.any():
        donnees_a_predire.loc[case_vide, 'margin_low'] = modele_marge.predict(donnees_a_predire.loc[case_vide, colonnes_marge])
    
    X_new = donnees_a_predire[toutes_les_colonnes]
    
    # Extraction de la probabilité d'être un vrai billet (Classe 1)
    probabilites_vrai = meilleur_modele.predict_proba(X_new)[:, 1]
    
    # Application du seuil de sécurité strict
    return np.where(probabilites_vrai >= seuil_securite, 1, 0)


# =====================================================================
# ÉTAPE 4 : LOGIQUE DE GESTION DES INPUTS (LIVRABLE COMMAND-LINE)
# =====================================================================
if len(sys.argv) > 1:
    # --- MODE 1 : PAR FICHIER CSV ---
    # Exemple d'appel : python script.py billets_production.csv
    chemin_fichier = sys.argv[1]
    try:
        donnees_prod = pd.read_csv(chemin_fichier)
        print(f"\n--- RÉSULTATS (OUTPUT BINAIRE) POUR LE FICHIER : {chemin_fichier} ---")
        predictions_finales = predire_binaire(donnees_prod)
        
        # Simple output binaire ligne par ligne
        for i, pred in enumerate(predictions_finales):
            id_billet = donnees_prod['id'].iloc[i] if 'id' in donnees_prod.columns else i
            print(f"Billet {id_billet} : {pred}")
            
    except Exception as e:
        print(f"Erreur lors du traitement du fichier : {e}")
else:
    # --- MODE 2 : PAR SAISIE MANUELLE INTERACTIVE ---
    print("\nAucun fichier fourni. Passage en mode saisie manuelle d'un billet.")
    print("Entrez les 5 dimensions séparées par des espaces dans cet ordre exact :")
    print("diagonal height_left height_right margin_up length")
    print("(Exemple : 171.43 104.14 103.62 3.27 112.95)")
    
    saisie = input("\nVos dimensions : ").strip().split()
    if len(saisie) == 5:
        try:
            valeurs = [float(x) for x in saisie]
            df_un_billet = pd.DataFrame([{
                'diagonal': valeurs[0],
                'height_left': valeurs[1],
                'height_right': valeurs[2],
                'margin_low': np.nan,  # Laissé vide pour être calculé automatiquement
                'margin_up': valeurs[3],
                'length': valeurs[4]
            }])
            
            resultat = predire_binaire(df_un_billet)[0]
            print(f"\nRésultat de la prédiction (Output binaire) : {resultat}")
            print("(1 = Vrai billet, 0 = Faux billet)")
        except ValueError:
            print("Erreur : Veuillez n'insérer que des nombres valides.")
    else:
        print("Erreur : Vous devez fournir exactement 5 dimensions géométriques.")