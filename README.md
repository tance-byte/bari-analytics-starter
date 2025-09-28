# BARI Analytics — Starter Repo
Projet BARI (1re année).
Deux mini-projets : inflation CH et EUR/CHF.
Objectif : apprendre à manipuler des données et faire 2 graphiques.
Petit dépôt pour 2 mini-projets **Business Analytics** pendant le BARI.

## Contenu
```
bari-analytics-starter/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── notebooks/
│   ├── 01_inflation_ch.ipynb
│   └── 02_fx_eurchf_backtest.ipynb
├── src/
│   ├── data.py
│   └── utils.py
├── data/
│   ├── raw/         # mettre ici les CSV bruts (non versionnés)
│   └── processed/   # sorties nettoyées (non versionnées)
└── figures/         # graphiques exportés
```

## Comment reproduire
1. Créer un environnement Python 3.11+
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Ouvrir `notebooks/01_inflation_ch.ipynb` et `notebooks/02_fx_eurchf_backtest.ipynb` dans Jupyter.

## Données (à ajouter manuellement)
- **Inflation CH** : Indice des prix à la consommation (IPC) — télécharger un CSV depuis une source officielle (p. ex. OFS/Office fédéral de la statistique). Enregistrer sous `data/raw/cpi_ch.csv`.
- **EUR/CHF** : séries historiques (p. ex. banque centrale). Enregistrer sous `data/raw/eurchf.csv`.

## Bonnes pratiques
- Ne commite **jamais** de données personnelles ou de secrets.
- Les répertoires `data/*` sont ignorés par git (voir `.gitignore`).
- Ajoute une capture de tes résultats dans `figures/` et lie-les dans ce README.

## Licence
MIT — fais-en ce que tu veux.
