# Prénom Nom — Portfolio Data

Data analyst en reconversion — analyses et outils au service de la décision.

📧 vous@email.com · 💼 [LinkedIn](https://linkedin.com/in/votreprofil) · 💻 [GitHub](https://github.com/whereissilver)

---

## Sommaire

- [À propos](#à-propos)
- [Compétences](#compétences)
- [Projets](#projets)
- [Veille métier & technologique](#veille-métier--technologique)
- [Contact](#contact)

---

## À propos

<!-- REMPLACEZ ce paragraphe par votre positionnement en 3-4 lignes -->
Après [votre parcours précédent], je me suis formé(e) à l'analyse de données ([nom de la
formation], [dates]). J'aime particulièrement les projets où l'analyse débouche sur une
décision concrète : un tableau de bord qu'une équipe utilise vraiment, un modèle qui évite
des erreurs, une recommandation qui change une pratique.

Je maîtrise le cycle complet d'un projet data : cadrage du besoin métier, collecte et
nettoyage des données, analyse et modélisation, restitution (dataviz, rapport, dashboard)
et recommandations. J'utilise principalement **Python, SQL et Power BI / Tableau**.

Ce portfolio réunit 10 projets — de formation et personnels — présentés comme de vrais
livrables de mission : contexte, données, démarche, résultats, limites. L'objectif est que
vous puissiez évaluer mon niveau et ma façon de raisonner, pas seulement les outils utilisés.

---

## Compétences

| Compétence | Illustrée par |
|---|---|
| Collecte & nettoyage de données | [Projet 01](#projet-01) |
| Analyse statistique | [Projet 02](#projet-02) |
| Modélisation / Machine Learning | [Projet 03](#projet-03) |
| Dataviz & restitution (Power BI) | [Projet 04](#projet-04) |
| SQL & bases de données | [Projet 05](#projet-05) |
| Automatisation / scripting | [Projet 06](#projet-06) |
| Communication & restitution métier | [Projet 07](#projet-07) |

---

## Projets

Chaque fiche suit la même trame : **contexte → données → démarche → résultats & impact →
limites & pistes**.

### Projet 01
**Nettoyage & fiabilisation d'une base clients [secteur]**
`Formation` · `Python` · `Pandas` · [Code source ↗](https://github.com/whereissilver/nom-du-repo)

| | |
|---|---|
| **Contexte** | [Entreprise/mission fictive] disposait d'une base clients de X lignes utilisée pour le reporting mensuel, mais les analyses produisaient des chiffres incohérents d'un mois sur l'autre. Objectif : livrer une base fiabilisée et un protocole de contrôle qualité réutilisable par l'équipe. |
| **Données** | Export CRM au format CSV, ~X lignes. Qualité initiale : Y % de doublons, Z % de valeurs manquantes sur les champs clés, formats de dates hétérogènes. Limite : aucune donnée externe pour valider certains champs, historique limité à 18 mois. |
| **Démarche** | Audit qualité avec Python (Pandas, ydata-profiling) pour cartographier les anomalies. Choix de Pandas plutôt qu'Excel pour la reproductibilité (script versionné vs manipulation manuelle). Règles de déduplication et normalisation documentées. Contrôle qualité automatisé et réutilisable. |
| **Résultats & impact** | Base fiabilisée à 99 % sur les champs clés, doublons ramenés de Y % à moins de 0,5 %. Le script de contrôle qualité, relançable à chaque nouvel export, réduit le temps de fiabilisation mensuel de plusieurs heures à quelques minutes. |
| **Limites & pistes** | Certaines anomalies (adresses mal saisies) nécessiteraient une API d'adresses pour être corrigées automatiquement. Piste : intégrer ce contrôle qualité directement dans le pipeline d'ingestion, en amont du reporting. |

---

### Projet 02
**Analyse des facteurs d'attrition client**
`Formation` · `SQL` · `Stats` · [Rapport ↗](#)

| | |
|---|---|
| **Contexte** | La direction commerciale de [entreprise fictive] cherchait à comprendre pourquoi le taux de résiliation avait augmenté de X points en un an, pour prioriser ses actions de rétention. |
| **Données** | Base contrats + historique de contacts service client (SQL), ~X clients. Bonne complétude sur les champs contractuels, faible sur les motifs de résiliation (texte libre). Limite : pas de données de satisfaction (NPS) disponibles sur la période. |
| **Démarche** | Requêtes SQL pour construire une table d'analyse au niveau client. Analyse statistique (tests du chi², corrélations) pour identifier les variables liées à la résiliation. Choix d'une analyse exploratoire avant modélisation, pour garder des résultats interprétables par des non-techniciens. Restitution avec visualisations (Matplotlib/Seaborn). |
| **Résultats & impact** | Trois facteurs expliquent la majorité des résiliations : plus de 2 incidents non résolus en 6 mois, absence d'usage pendant 3 mois consécutifs, fin d'engagement contractuel. Recommandation : alerte automatique dès le 2ᵉ incident non résolu. |
| **Limites & pistes** | Analyse corrélationnelle, pas causale. Piste : modèle prédictif (voir Projet 03) et test de l'impact d'une intervention sur un échantillon pilote. |

---

### Projet 03
**[Titre du projet — modèle prédictif]**
`Formation` · `Scikit-learn` · `ML` · [Code source ↗](#)

| | |
|---|---|
| **Contexte** | [Quel besoin métier ? Qui le demande ?] |
| **Données** | [Source, volumétrie, qualité, limites] |
| **Démarche** | [Outils, méthode, étapes clés, et pourquoi ces choix] |
| **Résultats & impact** | [Ce qui a été livré + traduction business] |
| **Limites & pistes** | [Ce qui pourrait être amélioré / prochaine étape] |

---

### Projet 04
**[Titre du projet — dashboard de pilotage]**
`Formation` · `Power BI` · `DAX` · [Dashboard ↗](#)

| | |
|---|---|
| **Contexte** | [...] |
| **Données** | [...] |
| **Démarche** | [...] |
| **Résultats & impact** | [...] |
| **Limites & pistes** | [...] |

---

### Projet 05
**[Titre du projet personnel 1]**
`Personnel` · `SQL` · [Code source ↗](#)

| | |
|---|---|
| **Contexte** | [Quel problème personnel/concret avez-vous voulu résoudre ?] |
| **Données** | [...] |
| **Démarche** | [...] |
| **Résultats & impact** | [...] |
| **Limites & pistes** | [...] |

---

### Projet 06
**[Titre du projet personnel 2]**
`Personnel` · `Python` · [Code source ↗](#)

| | |
|---|---|
| **Contexte** | [...] |
| **Données** | [...] |
| **Démarche** | [...] |
| **Résultats & impact** | [...] |
| **Limites & pistes** | [...] |

---

### Projet 07
**[Titre du projet 7]**
`Formation` · `Excel` · [Code source ↗](#)

| | |
|---|---|
| **Contexte** | [...] |
| **Données** | [...] |
| **Démarche** | [...] |
| **Résultats & impact** | [...] |
| **Limites & pistes** | [...] |

---

### Projet 08
**[Titre du projet 8]**
`Formation` · `Python` · [Code source ↗](#)

| | |
|---|---|
| **Contexte** | [...] |
| **Données** | [...] |
| **Démarche** | [...] |
| **Résultats & impact** | [...] |
| **Limites & pistes** | [...] |

---

### Projet 09
**[Titre du projet personnel 3]**
`Personnel` · `API` · [Code source ↗](#)

| | |
|---|---|
| **Contexte** | [...] |
| **Données** | [...] |
| **Démarche** | [...] |
| **Résultats & impact** | [...] |
| **Limites & pistes** | [...] |

---

### Projet 10
**[Titre du projet 10]**
`Formation` · `Reporting` · [Code source ↗](#)

| | |
|---|---|
| **Contexte** | [...] |
| **Données** | [...] |
| **Démarche** | [...] |
| **Résultats & impact** | [...] |
| **Limites & pistes** | [...] |

---

## Veille métier & technologique

### Outils d'analyse & de dataviz

| Outil / méthode | Ce que j'ai identifié | Source | Pourquoi ce choix |
|---|---|---|---|
| [Ex. Power BI — nouvelles fonctions DAX] | [Ce que l'évolution apporte concrètement] | [Blog officiel / newsletter] | [Maturité, adéquation au besoin, coût] |
| [Ex. Plotly / Observable] | [...] | [...] | [...] |
| [Ex. outil no-code de dataviz] | [...] | [...] | [...] |

### Méthodes & pratiques d'analyse

| Méthode | Ce que j'ai identifié | Source | Pourquoi ce choix |
|---|---|---|---|
| [Ex. Data quality frameworks] | [...] | [Documentation officielle / article] | [Robustesse, adoption, facilité d'intégration] |
| [Ex. Tests A/B, inférence causale] | [...] | [...] | [...] |

### IA & automatisation appliquées à la data

| Outil / méthode | Ce que j'ai identifié | Source | Pourquoi ce choix |
|---|---|---|---|
| [Ex. Claude / Copilot pour l'analyse] | [...] | [...] | [Gain de temps mesuré, limites identifiées] |

### Mes sources de veille

- [Ex. Newsletters : Data Elixir, Analytics Engineering Roundup...]
- [Ex. Communautés : Kaggle, subreddits data, Slack/Discord de la promo...]
- [Ex. Blogs éditeurs : Microsoft Power BI, dbt Labs, documentation officielle...]
- [Ex. Conférences / podcasts...]

---

## Contact

📧 [vous@email.com](mailto:vous@email.com) · 💼 [LinkedIn](https://linkedin.com/in/votreprofil) · 💻 [GitHub](https://github.com/whereissilver)
