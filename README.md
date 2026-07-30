# Kévin Papama — Portfolio Data Analyst

📧 kevin.papama@gmail.com · 💻 [GitHub](https://github.com/WhereIsSilver) · 📍 Toulouse (31200)

---

## Sommaire

- [À propos](#à-propos)
- [Expérience professionnelle](#expérience-professionnelle)
- [Compétences](#compétences)
- [Projets](#projets)
- [Veille métier & technologique](#veille-métier--technologique)
- [Contact](#contact)

---

## À propos

Étudiant en alternance, je suis le parcours Data Analyst d'OpenClassrooms
(titre RNCP de niveau 6).

Ce portfolio réunit 11 projets réalisés dans le cadre d'OpenClassrooms — présentés comme
de vrais livrables de mission : contexte, données, démarche, résultats, limites.

Chez Groupe VMS, l'entreprise qui m'a accueilli pour l'alternance, je conçois et maintiens
un écosystème de reporting Power BI.

---

## Expérience professionnelle

**Data Analyst — Alternance (2 ans)**
Groupe VMS, Giroussens — vente et location de matériel BTP, agricole, industriel et loisirs
*Septembre 2024 – Septembre 2026*

Conception et maintenance d'un outil de pilotage de plus de 100 pages de dashboards Power BI
couvrant les principaux domaines métiers (ventes, location, SAV, pièces détachées, comptabilité).

- **Reporting & gouvernance des données** — tableaux de bord multi-services, suivi des flux
  opérationnels (entrées/sorties machines, stock), monitoring des processus internes (VGP,
  contrôle technique, maintenance), suivi financier automatisé (SIG, balance générale)
- **Data engineering** — nettoyage, transformation et optimisation des données via Power Query
  (ETL), amélioration de la qualité des données (doublons, valeurs manquantes, normalisation)
- **SQL & automatisation** — requêtes SQL via Microsoft Access pour extraction rapide à la
  demande, scripts Python pour automatisation (scraping, génération de QR codes)

---

## Compétences

| Compétence | Illustrée par |
|---|---|
| Power BI & restitution | [Projet 06](#projet-06) · [Projet 09](#projet-09) |
| SQL & bases de données | [Projet 02](#projet-02) · [Projet 04](#projet-04) |
| Python / R — analyse & modélisation | [Projet 03](#projet-03) · [Projet 11](#projet-11) |
| Excel avancé (TCD, formules, VBA) | [Projet 01](#projet-01) |
| Qualité des données & RGPD | [Projet 04](#projet-04) · [Projet 07](#projet-07) |
| ETL / Power Query | Expérience VMS |
| Étude de marché & analyse business | [Projet 10](#projet-10) |

---

## Projets

Chaque fiche suit la même trame : **contexte → données → démarche → résultats & impact →
limites & pistes**.

### Projet 01
**Analyse de ventes pour un e-commerce**
`Formation` · `Excel` · `TCD` · [Dossier du projet ↗](https://github.com/WhereIsSilver/portfolio/tree/main/Projets/1%20-%20Faites%20une%20analyse%20de%20ventes%20pour%20un%20e-commerce)

| | |
|---|---|
| **Contexte** | Mission fictive pour un site e-commerce multi-catégories (nourriture, biens de consommation, high-tech) : la direction marketing constate un chiffre d'affaires en baisse malgré une forte hausse du trafic, et demande un rapport mensuel identifiant les causes et des pistes d'action. |
| **Données** | Exports mensuels des ventes des clients affiliés (mars 2019 à février 2020) : ID client, temps passé avant achat, montant du panier, catégorie du produit. Qualité : données propres et structurées, mais limitées — pas de données démographiques sur les clients, pas de détail sur l'origine du trafic (source d'acquisition), historique d'un an seulement. |
| **Démarche** | Construction de tableaux croisés dynamiques (TCD) sous Excel pour croiser clients, catégories et mois. Calcul d'indicateurs clés : CA par catégorie, panier moyen, temps passé sur le site, et surtout **taux de conversion** (ventes / visites). Choix d'Excel plutôt qu'un outil de code : volumétrie limitée et livrable destiné à être repris directement par l'équipe marketing, sans dépendance à un environnement technique. |
| **Résultats & impact** | Le CA recule depuis avril 2019 alors même que le trafic sur le site est multiplié par ~30 sur la période. Cause identifiée : le taux de conversion s'effondre, passant de 11 % à 5 %. Le mix produit se déplace aussi vers la catégorie nourriture, au détriment du high-tech. Recommandations formulées : simplifier le tunnel d'achat, proposer le paiement en tant qu'invité, diversifier les moyens de paiement, afficher des signaux de confiance sur le site. |
| **Limites & pistes** | Analyse descriptive : elle identifie une corrélation (trafic ↑, conversion ↓) mais ne permet pas d'isoler la cause exacte de la baisse de conversion (UX, prix, qualité du trafic acquis...). Pistes : croiser avec les données d'acquisition marketing (source du trafic), suivre le taux d'abandon de panier, et tester les recommandations via A/B test sur un échantillon avant déploiement général. |

---

### Projet 02
**Requêtage d'une base de données avec SQL**
`Formation` · `SQL` · `MySQL Workbench` · [Dossier du projet ↗](https://github.com/WhereIsSilver/portfolio/tree/main/Projets/2%20-%20Requ%C3%AAtez%20une%20base%20de%20donn%C3%A9es%20avec%20SQL)

| | |
|---|---|
| **Contexte** | Mission fictive pour une compagnie d'assurance habitation : modéliser et charger un portefeuille de contrats dans une base de données relationnelle, afin de pouvoir répondre rapidement à des questions métier ponctuelles (prix de cotisation, surfaces, répartition géographique...) sans dépendre d'un accès manuel aux fichiers sources. |
| **Données** | Deux fichiers CSV sources : `Contrat.csv` (30 335 lignes — surface, type de local, formule, valeur déclarée des biens, prix de cotisation mensuel...) et `Region.csv` (38 916 lignes — référentiel géographique commune/département/région/académie). Qualité : structure homogène, mais présence de cellules vides sur certaines colonnes à traiter lors de la modélisation. Limite : base figée à un instant T, pas de mise à jour automatisée, pas d'autres entités (sinistres, clients) reliées aux contrats. |
| **Démarche** | 1) Construction d'un **dictionnaire des données** (type, taille, clé, description de chaque colonne) pour cadrer la structure avant modélisation. 2) Conception d'un **schéma relationnel normalisé** (table `Contrat` liée à la table `Region` par la clé `Code_dep_code_commune`) sous MySQL Workbench. 3) Génération du script SQL de création des tables à partir du schéma, en ajustant les longueurs de `VARCHAR` pour la compatibilité MySQL. 4) Import des données et **vérification du nombre de lignes chargées** (30 335 / 38 916) pour garantir la cohérence avec les fichiers sources avant toute analyse. 5) Rédaction d'une dizaine de requêtes SQL répondant à des questions métier concrètes, mobilisant jointures (`JOIN`), filtres (`WHERE`), agrégations (`AVG`, `COUNT`), regroupements (`GROUP BY`, `HAVING`) et tris (`ORDER BY`, `LIMIT`). |
| **Résultats & impact** | Base de données relationnelle fonctionnelle, intégralement chargée et vérifiée. Les requêtes livrées répondent à des besoins métier variés : prix moyen de cotisation national (19,33 €), classement des départements où la cotisation moyenne est la plus élevée (Paris : 36,40 € ; Hauts-de-Seine : 26,27 €...), surface moyenne des contrats dans l'académie de Paris (51,77 m²), ou encore identification des communes à fort volume de contrats (Paris 18ᵉ : 515 contrats). Ces requêtes, réutilisables, permettent d'obtenir une réponse métier en quelques secondes plutôt qu'en manipulant les fichiers sources à la main. |
| **Limites & pistes** | Le schéma reste volontairement simple (2 tables) ; une base de production intégrerait d'autres entités (sinistres, clients, historique). Les requêtes sont exécutées ponctuellement à la demande. Piste d'amélioration : les transformer en vues SQL réutilisables, voire les connecter à un outil de restitution (Power BI) pour un accès self-service par les équipes métier, sans dépendre d'un analyste pour chaque nouvelle question. |

---

### Projet 03
**Étude de santé publique — sous-nutrition mondiale (données FAO)**
`Formation` · `R` · `RMarkdown` · `ggplot2` · [Dossier du projet ↗](https://github.com/WhereIsSilver/portfolio/tree/main/Projets/3%20-%20R%C3%A9alisez%20une%20%C3%A9tude%20de%20sant%C3%A9%20publique%20avec%20R%20ou%20Python)

| | |
|---|---|
| **Contexte** | Mission fictive pour une ONG luttant contre la faim dans le monde : exploiter les données ouvertes de la FAO pour objectiver la situation de la sous-nutrition mondiale et identifier les pays et les leviers sur lesquels concentrer les actions. |
| **Données** | 4 fichiers CSV de la FAO : population, disponibilité alimentaire (par pays et par produit), aide alimentaire, sous-nutrition. Qualité : valeurs manquantes sur `dispo_alimentaire` (traitées comme des 0), valeurs non numériques sur `sous_nutrition` nécessitant une conversion, unités hétérogènes selon les fichiers (milliers de tonnes, milliers de personnes) à redresser avant toute analyse. Limite : le remplacement des valeurs manquantes par 0 est une simplification qui peut sous-estimer certains totaux ; la sous-nutrition est mesurée sur une plage d'années (2016-2018) rapprochée d'une population figée à 2017. |
| **Démarche** | Nettoyage sous R : renommage des colonnes, redressement des unités, traitement des valeurs manquantes. Rédaction sous **RMarkdown** pour produire un rapport reproductible combinant code, résultats chiffrés et visualisations (`ggplot2`, `barplot`) dans un document unique. Choix de R plutôt que Python : écosystème statistique adapté à ce type d'analyse académique (`aggregate`, `merge`) et RMarkdown permettant de livrer un rapport directement exploitable sans repasser par un outil de mise en forme externe. 11 analyses construites pour répondre à des questions métier précises : taux de sous-nutrition, capacité théorique de la disponibilité alimentaire mondiale à nourrir la population, répartition des usages (alimentation humaine, animale, pertes...), focus pays. |
| **Résultats & impact** | En 2017, **535,7 millions de personnes** étaient en sous-nutrition, soit environ 7,1 % de la population étudiée. Point clé : la disponibilité alimentaire mondiale permettrait théoriquement de nourrir **9,5 milliards de personnes** (130 % de la population mondiale) — et même **7,8 milliards** (108 %) en ne comptant que les produits végétaux. La faim dans le monde n'est donc pas un problème de volume de production, mais de répartition et d'accès. Sur les céréales spécifiquement, 43 % de la disponibilité sert à l'alimentation humaine directe contre 36 % à l'alimentation animale — un levier de réallocation possible. Les pays les plus touchés (Haïti 48,3 %, Corée du Nord 47,2 %, Madagascar 41,1 %) et les principaux bénéficiaires de l'aide alimentaire (Syrie, Éthiopie, Yémen) coïncident largement avec des zones de crise ou de conflit. Le focus sur la Thaïlande illustre bien le paradoxe : 83 % du manioc produit est exporté alors que le pays compte encore 9 % de sa population en sous-nutrition. |
| **Limites & pistes** | Le remplacement des valeurs manquantes par 0 n'est pas neutre statistiquement et peut biaiser certains totaux à la baisse — une piste serait de distinguer une donnée réellement nulle d'une donnée non collectée. L'analyse reste une photographie à un instant T, sans série temporelle longue permettant d'observer une tendance. Piste d'approfondissement : croiser ces données avec des indicateurs socio-économiques (PIB, conflits, climat) pour mieux comprendre les causes structurelles de la sous-nutrition au-delà de la seule disponibilité alimentaire. |

---

### Projet 04
**Création et exploitation d'une base de données immobilière**
`Formation` · `SQL` · `MySQL` · `RGPD` · [Dossier du projet ↗](https://github.com/WhereIsSilver/portfolio/tree/main/Projets/4%20-%20Cr%C3%A9ez%20et%20utilisez%20une%20base%20de%20donn%C3%A9es%20immobili%C3%A8re%20avec%20SQL)

| | |
|---|---|
| **Contexte** | Mission fictive pour Laplace Immo, un réseau d'agences immobilières qui souhaite mieux conseiller ses clients sur les prix de vente pour se démarquer de la concurrence. Objectif : modéliser et charger une base de données des ventes immobilières en France, exploitable par les agences via des requêtes métier. |
| **Données** | Trois sources croisées : un référentiel géographique (régions/départements/communes), un fichier de données communes (démographie), et les valeurs foncières (transactions immobilières incluant les noms des acquéreurs). Analyse RGPD réalisée en amont : les données géographiques et démographiques ne contiennent aucune donnée personnelle, contrairement aux valeurs foncières qui identifient les acquéreurs et nécessitent donc un traitement adapté (anonymisation) avant exploitation. |
| **Démarche** | Construction d'un dictionnaire des données sur 4 entités (`Region`, `Commune`, `Bien`, `Vente`) précisant pour chaque champ son type, sa longueur et ses règles de gestion (nullabilité, format de date...). Conception d'un schéma relationnel normalisé, puis création et chargement de la base sous MySQL avec vérification systématique du nombre de lignes chargées. Rédaction de 12 requêtes SQL répondant à des besoins métier concrets des agences : volumes de ventes, prix au m² par zone géographique, taux d'évolution, classements de communes et de départements. |
| **Résultats & impact** | Base opérationnelle permettant de répondre en quelques secondes à des questions clés pour les agences : 31 378 appartements vendus au 1ᵉʳ semestre 2020, prix moyen du m² pour une maison en Île-de-France estimé à 3 765 €, taux d'évolution des ventes de +3,6 % entre le 1ᵉʳ et le 2ᵉ trimestre 2020, écart de prix au m² de 12,7 % entre un appartement de 2 et de 3 pièces. Ces indicateurs donnent aux conseillers des arguments chiffrés et à jour pour orienter leurs clients sur une estimation de prix. |
| **Limites & pistes** | La base reste à ce stade un outil de reporting descriptif et rétrospectif (un seul semestre analysé), alors que l'objectif final de Laplace Immo est de **prévoir** les prix de vente. Piste naturelle : faire évoluer cette base vers un modèle prédictif (régression sur les caractéristiques du bien — surface, pièces, localisation) plutôt qu'une simple consultation de l'historique, en s'appuyant sur la même logique de modélisation que le Projet 03. |

---

### Projet 05
**Optimisation de la gestion des données d'une boutique — Bottleneck**
`Formation` · `Python` · `Pandas` · `Plotly` · [Dossier du projet ↗](https://github.com/WhereIsSilver/portfolio/tree/main/Projets/5%20-%20Optimisez%20la%20gestion%20des%20donn%C3%A9es%20d%27une%20boutique%20avec%20R%20ou%20Python)

| | |
|---|---|
| **Contexte** | Mission fictive pour Bottleneck, une boutique de vente de vins et spiritueux en ligne, à l'approche de la mise en place d'un nouvel ERP. Objectif présenté en comité de direction : nettoyer et fiabiliser les données issues de deux systèmes (ERP interne et site web) pour livrer un état des lieux fiable du catalogue, du stock et de la rentabilité avant la bascule. |
| **Données** | Trois fichiers Excel : `erp.xlsx` (825 lignes — stock, prix d'achat, prix de vente, statut de stock), `web.xlsx` (1 513 lignes, réduites à 4 colonnes utiles après nettoyage), et `liaison.xlsx` (table de correspondance entre les identifiants ERP et web). Qualité : prix et stocks négatifs détectés, prix d'achat parfois supérieur au prix de vente, statut de stock déclaratif incohérent avec la quantité réelle, SKU manquants côté web, écarts entre les 3 fichiers sur le flag "en vente sur le web". Limite : photo des données à un instant T, pas de flux temps réel. |
| **Démarche** | Python (Pandas, NumPy) pour le nettoyage : reconstruction du statut de stock à partir de la quantité réelle plutôt que du champ déclaratif jugé peu fiable. Jointures successives ERP → liaison → web, avec vérification systématique des non-correspondances à chaque étape (produits sans équivalent web, doublons de SKU) plutôt qu'une suppression aveugle des lignes ambiguës. Détection des valeurs aberrantes sur les prix par deux méthodes complémentaires (Z-score et intervalle interquartile) pour croiser les résultats. Construction d'indicateurs métier avec Plotly Express et Seaborn : chiffre d'affaires par article, courbe de concentration du CA, rotation de stock, valorisation du stock, taux de marge, matrice de corrélation stock/ventes/prix. |
| **Résultats & impact** | Chiffre d'affaires du site calculé à **143 680 €**. Constat notable pour la direction : 61 % du catalogue génère 80 % du CA et des ventes en volume — un catalogue moins concentré sur quelques best-sellers que ne le laisserait attendre la règle classique du 80/20, donc moins dépendant d'un petit nombre de références. Stock valorisé à **277 305 €** pour 16 739 unités, taux de marge s'échelonnant de 23 % à 48 % selon les produits. Analyse de corrélation : les produits plus chers se vendent moins (cohérent pour du vin et des spiritueux premium), le niveau de stock a peu d'influence sur le prix. Recommandations formulées en CODIR avant la bascule ERP : revoir les produits à publier ou non sur le site, automatiser le calcul du statut de stock (source d'erreurs en saisie manuelle), et clarifier les écarts entre prix d'achat et prix de vente. |
| **Limites & pistes** | La vérification croisée de la cohérence entre plusieurs colonnes (prix, quantité, CA) pour repérer d'éventuelles erreurs de saisie a été la partie la plus délicate, et certains taux de marge atypiques restent à investiguer avec les équipes commerciales avant la migration. Piste : automatiser ces contrôles de cohérence en amont plutôt qu'en aval de la bascule ERP, pour éviter de reproduire les mêmes anomalies dans le nouveau système. |

---

### Projet 06
**Tableau de bord dynamique Power BI — avancement de projets**
`Formation` · `Power BI` · `Power Query` · `DAX` · `Gantt` · [Fichier .pbix ↗](https://github.com/WhereIsSilver/portfolio/tree/main/Projets/6%20-%20Cr%C3%A9ez%20un%20tableau%20de%20bord%20dynamique%20avec%20Power%20BI%20pour%20visualiser%20l%27avancement%20de%20projets)

| | |
|---|---|
| **Contexte** | Mission fictive réalisée pour le compte d'ESNDATA (ESN) auprès d'un client du secteur santé, Sanitoral. Commanditaire : Sophie, cheffe de projet au sein du PMO (Project Management Office) de Sanitoral. Objectif cadré en amont via un **Product Strategy Canvas** : évaluer la performance des projets IT et Marketing de l'entreprise, pour 3 profils d'utilisateurs identifiés avec des besoins différents — le DG (vision globale, alerte à 15 % d'écart, décision d'arrêt ou de poursuite), les directeurs région (suivi et alerte sur leur périmètre) et les directeurs pays (indicateurs et mesures correctives sur leurs projets). |
| **Données** | Fichiers Excel importés et préparés via Power Query : plans de projets (coûts et durées planifiés), coûts réels, durées réelles, livrables réels, localisation des projets par pays, profils pays (région, type). Nettoyage : suppression des lignes vides, renommage des colonnes, et surtout création d'une **colonne ID calculée** (concaténation projet + phase) pour relier les 6 tables entre elles en un modèle en étoile. Portefeuille final : 104 projets, répartis à parts égales entre IT (CRM) et Marketing (lancement produit). |
| **Démarche** | Rapport Power BI construit en 6 pages dédiées à des usages différents plutôt qu'une page unique surchargée : une page de **synthèse** (KPI et répartitions), une page de **cadrage** reprenant le Product Strategy Canvas, une page **méthodologie** documentant les étapes de préparation des données, une page d'**analyse détaillée par phase** avec règles d'alerte explicites (coût : écart ≥ 15 % ; livraison : livrables réalisés < prévus ; durée : réelle > planifiée), une **carte géographique** des pays en retard, et un **planning Gantt** filtrable par intervalle de dates. Mesures DAX pour l'ensemble des KPI et de la jauge budgétaire. Documenter les règles d'alerte directement dans le rapport (page "Explication") plutôt que de les laisser implicites était un choix délibéré, pour qu'un utilisateur non technique comprenne ce qu'il regarde. |
| **Résultats & impact** | Sur les 104 projets suivis : **44 projets (42 %)** présentent un écart de coût significatif (≥ 15 %), **24 projets (23 %)** sont en retard, et le coût réel cumulé atteint **60 M€ contre 56 M€ planifiés**, soit un dépassement budgétaire global d'environ 7 %. La carte géographique identifie **24 pays** concernés par au moins un projet en retard, répartis entre Europe, Moyen-Orient, Afrique, Asie et Amérique du Sud. Au niveau le plus fin (par phase de projet), le compteur d'alerte comptabilise 243 alertes de coût, 214 phases en retard et 378 livraisons conformes. Ce niveau de détail permet à un directeur pays de cibler précisément les phases à risque de ses projets, sans attendre un reporting consolidé manuel. |
| **Limites & pistes** | Le seuil d'alerte de 15 % d'écart de coût est un choix fixé dans le cadrage initial (Product Strategy Canvas) qui mériterait d'être challengé projet par projet selon leur criticité, plutôt qu'appliqué uniformément. Le rapport reste une photo à un instant T, sans actualisation automatisée démontrée. Pistes : connecter la source à une actualisation planifiée dans le service Power BI, et conserver un historique des écarts dans le temps pour distinguer un projet ponctuellement en difficulté d'un projet structurellement mal engagé. |

---

### Projet 07
**Analyse des indicateurs d'égalité femmes/hommes en respect du RGPD**
`Formation` · `KNIME` · `RGPD` · [Dossier du projet ↗](https://github.com/WhereIsSilver/portfolio/tree/main/Projets/7%20-%20Analysez%20des%20indicateurs%20de%20l%27%C3%A9galit%C3%A9)

| | |
|---|---|
| **Contexte** | Mission fictive pour un cabinet de conseil en transformation digitale de 150+ collaborateurs en forte croissance : formaliser un diagnostic de l'égalité femmes-hommes pour améliorer la marque employeur et répondre aux obligations légales (index égalité professionnelle). |
| **Données** | Trois fichiers CSV RH sources (informations professionnelles, rémunération, données salarié). Étape d'anonymisation réalisée avant toute analyse : suppression du nom/prénom (donnée à caractère personnel), du téléphone (donnée confidentielle), de la date de naissance (trop précise) et de l'état civil (non utile aux indicateurs légaux exigés). Effectif final analysé : 256 salariés (131 hommes, 125 femmes). Limite majeure : la donnée de congé maternité est binaire (0/1), sans date de retour, ce qui empêche de vérifier l'obligation légale d'augmentation dans les 12 mois suivant le retour. |
| **Démarche** | Choix de **KNIME**, outil no-code fonctionnant par blocs visuels, pour plusieurs raisons assumées : import facilité de fichiers RH multi-sources, nettoyage et **anonymisation reproductibles** (donc conformes RGPD dès la collecte plutôt qu'en correction a posteriori), calcul automatisé des indicateurs, et surtout un workflow **rejouable chaque année** sans tout reconstruire — un vrai critère pour un livrable RH récurrent. Calcul des indicateurs de l'index égalité professionnelle (éventail des rémunérations, taux d'augmentation, taux de promotion, part des femmes parmi les 10 plus hauts salaires) puis analyses croisées par service, ancienneté et type de contrat. |
| **Résultats & impact** | Rémunération médiane de 165 chez les hommes contre 146 chez les femmes, avec un écart de taux de rémunération de 2 % en faveur des hommes — mais des écarts inversés sur le taux d'augmentation (+7 % en faveur des femmes) et le taux de promotion (+1 % en faveur des femmes). 30 % des 10 plus hauts salaires de l'entreprise sont occupés par des femmes. Recommandations concrètes formulées : recruter davantage de femmes dans le service informatique où elles sont sous-représentées, et revoir les salaires des femmes du service RH où un écart a été identifié. |
| **Limites & pistes** | Le score global de l'index égalité professionnelle n'a **pas pu être calculé**, faute de pouvoir mesurer correctement l'indicateur lié au congé maternité (donnée binaire insuffisante pour vérifier l'augmentation légale dans les 12 mois suivant le retour) — limite assumée et documentée plutôt que masquée par un score approximatif. Piste : faire remonter cette donnée manquante (date de retour de congé maternité) dans les prochaines campagnes de collecte RH, et industrialiser le workflow KNIME pour un suivi comparatif d'une année sur l'autre. |

---

### Projet 08
**Analyse des ventes d'une librairie — Lapage**
`Formation` · `Python` · `Pandas` · `Tests statistiques` · [Dossier du projet ↗](https://github.com/WhereIsSilver/portfolio/tree/main/Projets/8%20-%20Analysez%20les%20ventes%20d%27une%20librairie)

| | |
|---|---|
| **Contexte** | Mission confiée par Lapage, une librairie physique multi-points de vente ayant lancé son site de vente en ligne depuis 2 ans face au succès de ses produits. Objectifs : mieux comprendre l'activité, définir des indicateurs de vente (CA, top/flop produits, clients les plus fidèles) et analyser le comportement des clients via des corrélations (âge, genre, catégories achetées). |
| **Données** | Trois fichiers CSV : `customers` (8 621 clients — sexe, année de naissance), `products` (3 286 produits répartis en 3 catégories), `transactions` (687 534 lignes sur ~2 ans, mars 2021 à mars 2023). Nettoyage effectué : vérification et suppression des doublons (0 doublon résiduel après nettoyage), gestion des valeurs manquantes après jointure des trois tables. Limite assumée dès la présentation : une période d'observation de 2 ans reste courte pour distinguer une tendance de fond d'un effet ponctuel (saisonnalité, opération commerciale). |
| **Démarche** | Python (Pandas, Matplotlib, Plotly Express) sous notebook. Jointure des 3 tables et création de variables temporelles (année, mois, jour, semaine) pour analyser le CA à plusieurs granularités : quotidienne, hebdomadaire (avec moyenne mobile pour lisser les fluctuations), mensuelle et annuelle. Construction d'indicateurs métier : CA par catégorie, top 10 / flop 10 produits, top 10 clients, courbe de Lorenz pour mesurer la concentration du CA, analyse séparée des clients B2B. Pour l'analyse des comportements clients, **choix d'un test statistique différent selon la nature de chaque relation** plutôt qu'un test unique généralisé : chi² pour une relation entre deux variables qualitatives (genre × catégorie), corrélation de Spearman pour des relations monotones non linéaires (âge × montant, âge × fréquence), corrélation de Pearson pour une relation linéaire (âge × panier moyen), et test de Kruskal-Wallis pour comparer une variable quantitative entre plusieurs groupes (âge selon la catégorie de livre). |
| **Résultats & impact** | Chiffre d'affaires total de **12 027 663 €** sur la période, en hausse de 4 % entre avril 2021 et janvier 2023, malgré des fluctuations marquées (pic sept./oct. 2021, hausse fév./mars 2022) dont la cause reste à confirmer (hypothèses : rentrée scolaire, prix littéraire, rupture de stock). Les catégories 0 et 1 génèrent le plus de CA en volume, mais ce sont les livres de catégorie 2 qui dominent le classement des tops produits — un écart entre volume global et performance produit individuelle à ne pas confondre. Le CA B2B est concentré sur 4 clients seulement (le principal pesant à lui seul près de 3 % du CA total), alors que la clientèle B2C affiche une répartition plus homogène. Côté comportement : l'âge est fortement corrélé négativement au montant moyen des achats (Spearman r = -0,88) et au panier moyen (Pearson r = -0,72) — les clients plus jeunes achètent davantage et avec un panier plus élevé — et diffère significativement selon la catégorie de livre achetée (Kruskal-Wallis, p ≈ 0). Le lien entre genre et catégorie achetée est statistiquement significatif (χ² = 22,67 ; p < 0,001) mais visuellement peu marqué : plutôt que de le sur-interpréter, la conclusion retenue est que le comportement d'achat reflète surtout l'offre disponible. |
| **Limites & pistes** | La période d'observation reste courte pour confirmer une tendance de fond, et plusieurs pics de CA demeurent inexpliqués faute de données externes (calendrier commercial, actualité éditoriale, ruptures de stock). Point méthodologique assumé : une corrélation statistiquement significative (comme le chi² genre/catégorie) n'est pas toujours pertinente sur le plan opérationnel si son effet visuel est faible. Pistes : croiser ces données avec le calendrier des opérations commerciales pour expliquer les pics observés, et étendre la période d'analyse pour distinguer plus clairement tendance de fond et effets ponctuels. |

---

### Projet 09
**Étude sur l'accès à l'eau potable — DWFA**
`Formation` · `Power BI` · [Dossier du projet ↗](https://github.com/WhereIsSilver/portfolio/tree/main/Projets/9%20-%20Faites%20une%20%C3%A9tude%20sur%20l%27eau%20potable)

| | |
|---|---|
| **Contexte** | Mission de consultant data pour l'ONG fictive DWFA (Drinking Water For All), dont l'action s'articule autour de 3 expertises : création de points d'eau, modernisation d'infrastructures existantes, et conseil aux gouvernements. Objectif : identifier les pays à prioriser pour orienter les interventions de chacune de ces 3 expertises. |
| **Données** | 5 fichiers CSV : population (2000-2018), référentiel région/pays, stabilité politique (2000-2018), taux de mortalité lié à l'eau (2016), et taux d'accès aux services d'eau potable basiques et "safely managed" (2000-2017). Prétraitement documenté et appliqué systématiquement à chaque source : conversion des séparateurs décimaux, conversion en format numérique et en pourcentage pour les taux, conversion de la colonne année, nettoyage et renommage du référentiel pays. Limite : les sources couvrent des périodes différentes (mortalité limitée à 2016 seule, autres jusqu'à 2017-2018), ce qui empêche de croiser tous les indicateurs sur une même année de référence. |
| **Démarche** | Conception d'un **blueprint** (maquette) avant construction, pour structurer le rapport autour des 3 domaines d'expertise de l'ONG plutôt que par simple découpage technique : une **vue mondiale** avec des cartes filtrées sur des seuils métier (pays où moins de 50 % de la population a accès à l'eau potable, ou à des services de qualité) et des filtres croisés (stabilité politique, mortalité, accès à l'eau) ; une **vue continentale** comparant taux d'infrastructures "basiques" et "safely managed", avec un nuage de points dédié à l'axe conseil ; une **vue nationale** suivant dans le temps la stabilité politique, la population et sa densité pour affiner le diagnostic pays par pays. Choix de Power BI justifié explicitement : gratuit, cartes et filtres interactifs natifs, aucun coût pour une analyse locale, interface intuitive adaptée à un public non technique comme celui d'une ONG. |
| **Résultats & impact** | À l'échelle mondiale (7,6 milliards d'habitants suivis), 85,58 % de la population a accès à l'eau potable / eau sûre, pour un taux de mortalité lié à l'eau de 11,41 pour 100 000 habitants et un indice de stabilité politique moyen de -0,06 ; l'accès reste plus élevé en zone urbaine (55,29 % de la population) qu'en zone rurale (44,71 %). L'écart le plus révélateur apparaît à l'échelle continentale (exemple des Amériques) : 87,10 % de la population dispose d'un accès "basique" à l'eau potable, contre seulement 25,44 % d'un accès qualifié "safely managed" — un écart de plus de 60 points qui montre qu'une large part de la population considérée comme "ayant accès à l'eau" ne bénéficie pas d'un service réellement sûr, un insight clé pour prioriser les actions de **modernisation**. Le nuage de points croisant stabilité politique et score d'accès à l'eau (axe **conseil**) identifie des pays comme Haïti ou le Venezuela, où une instabilité politique marquée combinée à un score d'accès modéré à faible signale un besoin d'accompagnement plutôt qu'une simple intervention technique. |
| **Limites & pistes** | L'hétérogénéité des périodes couvertes par les sources limite la possibilité de croiser tous les indicateurs sur une même année de référence, en particulier pour la mortalité liée à l'eau (2016 uniquement). Autre point identifié en testant le rapport : sur la vue nationale sans pays sélectionné, l'indice de stabilité politique agrégé affiche une valeur incohérente (-11,87) très éloignée de la moyenne mondiale (-0,06) — signe qu'une mesure DAX resterait à corriger pour gérer proprement l'agrégation par défaut d'un indice qui n'a de sens qu'en moyenne, pas en somme. Pistes : corriger cette mesure, rechercher des sources actualisées et mieux alignées temporellement, et enrichir le modèle avec des données de financement déjà alloué par pays pour faire évoluer l'outil vers une aide à la priorisation budgétaire. |

---

### Projet 10
**Étude de marché à l'export — La poule qui chante**
`Formation` · `Python` · `ACP` · `Clustering` · [Dossier du projet ↗](https://github.com/WhereIsSilver/portfolio/tree/main/Projets/10%20-%20Produisez%20une%20%C3%A9tude%20de%20march%C3%A9%20avec%20R%20ou%20Python)

| | |
|---|---|
| **Contexte** | Mission fictive pour "La poule qui chante", entreprise française d'élevage et de vente de poulets certifiés Agriculture Biologique (positionnement premium), dont le PDG souhaite explorer de nouveaux marchés à l'export sans zone géographique prédéfinie. Mission confiée au data analyst : segmenter les marchés mondiaux pour identifier les pays prioritaires à l'export et fournir une aide à la décision hiérarchisée plutôt qu'une simple liste. |
| **Données** | Dataset consolidé de 150 pays et 10 indicateurs, construit selon le cadre stratégique **PESTEL** (Politique, Économique, Socioculturel, Technologique, Environnemental, Légal), à partir de 4 sources distinctes : FAOSTAT (bilans alimentaires, population), Banque Mondiale (PIB/habitant, stabilité politique, accès à l'électricité), CEPII (distances depuis la France), ITC/UE (taxes douanières, accords commerciaux). Défi technique résolu : standardisation des noms de pays via les codes ISO3 pour fusionner correctement les 4 sources. Limite : le niveau de fiabilité et d'actualisation diffère d'une source à l'autre. |
| **Démarche** | Python (Pandas, scikit-learn) pour la fusion et le nettoyage, puis **Analyse en Composantes Principales (ACP)** pour réduire la dimensionnalité — 3 composantes retenues pour atteindre l'objectif de 60 % de variance expliquée fixé en amont, contre 2 initialement envisagées. Double **clustering** (k-means et Classification Ascendante Hiérarchique) pour croiser deux méthodes et valider la cohérence des regroupements obtenus. Nombre de clusters (4) déterminé via l'analyse du coude sur l'inertie k-means, comme meilleur compromis entre cohérence statistique et lisibilité stratégique. Sélection du cluster cible par comparaison de boxplots sur les variables métier (distance, taxes, PIB, stabilité, accords commerciaux) plutôt que sur les seuls centroïdes, pour ancrer le choix dans des critères directement actionnables par l'entreprise. |
| **Résultats & impact** | Le **Cluster 2** (33 pays, dont Allemagne, Belgique, Finlande, Pays-Bas, Espagne, États-Unis) ressort comme la cible prioritaire : distance minimale et peu dispersée depuis la France, taxes douanières quasi nulles, plus forte concentration d'accords commerciaux avec l'UE, PIB par habitant médian le plus élevé du groupe, stabilité politique parmi les meilleures, et accès à l'électricité de 100 % — un critère décisif pour la chaîne du froid d'un produit périssable. Recommandation finale hiérarchisée sur 3 pays avec un argumentaire différencié : **Belgique** (proximité maximale et plus forte intensité d'import du groupe), **Allemagne** (marché solvable et volumineux, cadre politique stable), **Finlande** (positionnement premium justifié par un PIB/habitant élevé malgré l'éloignement). |
| **Limites & pistes** | L'objectif de 60 % de variance expliquée n'a été atteint qu'en passant à 3 composantes, ce qui signifie qu'une part non négligeable de l'information reste hors de la réduction de dimension — un choix assumé plutôt que masqué. L'agrégation des indicateurs au niveau pays lisse d'éventuelles disparités régionales internes. Pistes : affiner l'analyse à une granularité infranationale pour les pays finalement retenus, et remplacer la distance à vol d'oiseau par des données logistiques plus précises (mode de transport, délais réels) pour fiabiliser l'estimation des coûts d'export. |

---

### Projet 11
**Détection de faux billets par Machine Learning — ONCFM**
`Formation` · `Python` · `Scikit-learn` · `ML` · [Dossier du projet ↗](https://github.com/WhereIsSilver/portfolio/tree/main/Projets/11%20-%20D%C3%A9tectez%20des%20faux%20billets%20avec%20R%20ou%20Python)

| | |
|---|---|
| **Contexte** | Mission fictive pour l'ONCFM (Organisation Nationale de lutte Contre le Faux Monnayage) : développer une application intégrant un modèle de Machine Learning capable de prédire automatiquement si un billet est vrai ou faux, face à des réseaux criminels utilisant des scanners et imprimantes modernes très précis (0,05 mm) et un taux d'erreur humaine élevé en situation de contrôle sous stress. |
| **Données** | 1 500 billets déjà analysés et étiquetés (1 000 vrais, 500 faux), décrits par 6 dimensions géométriques (diagonale, hauteurs gauche/droite, marges haute/basse, longueur). 37 valeurs manquantes sur la marge basse, imputées par **régression linéaire** à partir des 5 autres dimensions plutôt que par suppression des lignes (R² du modèle d'imputation : 0,48 — modeste mais assumé et documenté). |
| **Démarche** | Mise en concurrence de deux approches plutôt qu'un modèle unique : un **K-means non supervisé** pour vérifier, sans connaître les étiquettes à l'avance, que les billets se séparent naturellement en 2 groupes cohérents (confirmé par la méthode du coude et un Silhouette Score maximal à k = 2, et visualisé via une ACP dont les 2 premiers axes capturent 60,3 % de la variance) ; puis trois modèles **supervisés** (Régression Logistique, KNN, Random Forest) évalués par **validation croisée stratifiée** pour écarter tout surapprentissage. Décision pilotée par une logique métier explicite plutôt qu'un seuil par défaut : seuil de classification strict fixé à 0,9, car un faux billet accepté comme vrai est plus dangereux pour la banque qu'un vrai billet rejeté par excès de prudence. Livrable final : un **script en ligne de commande réutilisable en production**, avec deux modes d'usage (fichier CSV en lot ou saisie manuelle interactive), imputation automatique des valeurs manquantes et seuil de sécurité intégrés directement dans la fonction de prédiction. |
| **Résultats & impact** | La **Régression Logistique** a été retenue comme modèle final malgré un rappel et un F1-score légèrement inférieurs à ceux du KNN (94,5 % contre 97 %), pour trois raisons assumées et hiérarchisées : une précision de **100 %** (aucun faux billet accepté comme vrai — le critère de sécurité prioritaire pour une banque), un score de 97,75 % rigoureusement identique entre validation croisée et entraînement (aucun signe de surapprentissage), et une **interprétabilité totale** via les coefficients du modèle, permettant d'expliquer précisément à un comité de direction pourquoi un billet est rejeté — contrairement au KNN, plus performant sur le papier mais qui fonctionne en boîte noire et doit stocker l'intégralité des données d'entraînement pour prédire. L'analyse K-means en amont a par ailleurs dégagé un profil géométrique intelligible : un vrai billet est plus long avec des marges fines, un faux billet est plus court avec des marges anormalement épaisses — un résultat qui donne du sens métier au modèle au-delà de sa seule performance chiffrée. |
| **Limites & pistes** | Le compromis retenu (précision de 100 % au prix d'un rappel plus faible que le KNN) implique qu'une partie des vrais billets sera rejetée par excès de prudence, générant des vérifications manuelles supplémentaires — un arbitrage assumé pour la sécurité, mais qui a un coût opérationnel côté guichet à objectiver. Le R² modeste (0,48) du modèle d'imputation des valeurs manquantes introduit par ailleurs une incertitude sur les 37 valeurs reconstruites, non propagée dans l'évaluation finale du modèle de classification. Pistes : suivre en production le taux de rejet de vrais billets pour ajuster le seuil si nécessaire, et tester une méthode d'imputation plus robuste (imputation multiple) pour fiabiliser les valeurs manquantes en amont. |

---

## Veille métier & technologique

### Power BI, Power Query & DAX

**Mes sources de veille sur ce thème :**
- Blog officiel Microsoft (notes de version mensuelles de Power BI)
- Blog Next Decision, spécialisé Power BI/DAX
- LinkedIn — comptes spécialisés (ex. Nicolas Brabant)
- YouTube — [Dataseito](https://www.youtube.com/@Dataseito)
- Reddit — [r/PowerBI](https://www.reddit.com/r/PowerBI/)

*Exemples concrets trouvés via ces sources :*

| Outil / technique | Ce que j'ai identifié | Source | Pourquoi ce choix |
|---|---|---|---|
| Auto-référencement d'une requête Power Query | Technique permettant à une requête de se référencer elle-même pour conserver une colonne de notes ajoutée manuellement, sans qu'elle soit écrasée à chaque actualisation. | [Post LinkedIn — Nicolas Brabant](https://fr.linkedin.com/posts/nicolas-brabant_lauto-r%C3%A9f%C3%A9rencement-dune-requ%C3%AAte-power-activity-7371908057372647424-3IdZ) | Problème rencontré concrètement en alternance : sans cette technique, toute note manuelle ajoutée sur une table est perdue au rafraîchissement suivant. |
| Calculs directement dans les visuels (sans mesure DAX) | Depuis mai 2026, Power BI permet d'ajouter des sommes cumulées, moyennes mobiles ou pourcentages directement dans un visuel, sans créer de mesure DAX. | [Next Decision — Nouveautés Power BI mai 2026](https://www.next-decision.fr/wiki/les-nouveautes-power-bi-mai-2026) | Évite de multiplier des mesures DAX qui ne servent qu'à un affichage isolé — à tester sur mon prochain rapport. |

### Python & analyse de données

**Mes sources de veille sur ce thème :**
- LinkedIn — actualités data en général
- YouTube — [Dataseito](https://www.youtube.com/@Dataseito)

*Exemple concret trouvé via ces sources :*

| Outil / technique | Ce que j'ai identifié | Source | Pourquoi ce choix |
|---|---|---|---|
| Polars, alternative à Pandas | Librairie qui monte en 2026 pour l'analyse de données volumineuses, avec des gains de performance sur des jeux de données larges. | [Python in Plain English — The Python Data Analyst Stack in 2026](https://python.plainenglish.io/the-python-data-analyst-stack-in-2026-duckdb-polars-and-the-death-of-pandas-790f92b39722) | Mes projets actuels restent sur des volumes raisonnables, donc pas de besoin concret aujourd'hui. Je garde cet outil en veille pour le jour où Pandas montrerait ses limites. |

### IA appliquée à l'analyse de données

**Mes sources de veille sur ce thème :**
- LinkedIn
- YouTube

*Exemple concret trouvé via ces sources :*

| Outil | Ce que j'identifie / usage concret | Source | Pourquoi ce choix |
|---|---|---|---|
| ChatGPT | Débogage de formules DAX, requêtes Power Query (M) et scripts Python quand une syntaxe ne fonctionne pas. | Usage direct en tant qu'outil de travail | Gain de temps réel sur le débogage, mais je vérifie systématiquement le résultat plutôt que de le copier tel quel — une formule DAX syntaxiquement correcte peut donner un résultat métier faux. |

---

## Contact

📧 [kevin.papama@gmail.com](mailto:kevin.papama@gmail.com) · 💻 [GitHub](https://github.com/WhereIsSilver)
