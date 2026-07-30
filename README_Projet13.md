# Analyse du stock et des ventes — Bottleneck

Notebook d'analyse croisant les données ERP et site web de Bottleneck (vente de vin en ligne) : chiffre d'affaires, palmarès des ventes, taux de marge, mois de stock, détection d'anomalies de prix.

## Structure

- `Module_06_OC.ipynb` — notebook principal (nettoyage, fusion, analyse, visualisations)
- `Module_13_OC_DOC.docx` — compte rendu : amélioration IA (Partie 1), veille technologique (Partie 2), cahier des charges (Partie 3), gestion de projet (Partie 4)
- `erp.xlsx`, `web.xlsx`, `liaison.xlsx` — fichiers sources (à placer dans le même dossier que le notebook, non fournis dans ce dépôt)

## Environnement

- Python 3.x
- Librairies : `pandas`, `numpy`, `plotly`, `ydata-profiling`, `sweetviz`
- Versions exactes : lancer `pip freeze > requirements.txt` dans l'environnement utilisé et joindre le fichier
- Seeds : non applicable — aucun traitement aléatoire (pas de split train/test, pas de modèle prédictif)

## Exécution

```
pip install pandas numpy plotly ydata-profiling sweetviz
```

1. Placer `erp.xlsx`, `web.xlsx`, `liaison.xlsx` dans le dossier du notebook
2. Ouvrir `Module_06_OC.ipynb`
3. Kernel → Restart & Run all

## Traçabilité des essais IA et justifications techniques

Détaillées dans le compte rendu, non dupliquées ici :
- **Partie 1** : prompts testés, variantes de code, choix justifié (histogramme plotly retenu vs boxplot dupliqué / alternative seaborn)
- **Partie 2** : panel de solutions, critères de comparaison, choix justifié (ydata-profiling retenu vs Sweetviz)

## Limites et biais

- Détection des outliers de prix (z-score + IQR) : peut exclure à tort des produits premium légitimement chers plutôt que de vraies erreurs de saisie — à valider manuellement avant toute action commerciale.
- Le CA calculé ne compte que les ventes reliées ERP ↔ web via `sku`/`id_web` ; les lignes non reliées sont exclues, ce qui peut légèrement sous-estimer le CA réel.
- Analyse figée à une date T : aucune saisonnalité ni tendance temporelle n'est prise en compte.
- Le taux de marge par catégorie peut être instable si une catégorie contient peu de produits.

## Synthèse recruteur / client

- **Résultats** : CA fiabilisé, palmarès des ventes, outliers de prix identifiés, mois de stock par produit.
- **Impact** : les équipes commerciale et achats peuvent prioriser leurs décisions sur des données vérifiées plutôt que sur les fichiers bruts.
- **Recommandations** : valider manuellement les outliers avant action commerciale ; automatiser ce notebook en pipeline récurrent si le volume de données augmente.
- **Prochaines étapes** : ajouter une dimension temporelle (évolution mensuelle du CA) ; envisager un modèle de prévision de la demande si le besoin se confirme.
