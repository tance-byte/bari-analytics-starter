from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def load_cpi(path: Path = DATA_DIR / "raw" / "cpi_ch.csv") -> pd.DataFrame:
    """Charge l'IPC suisse depuis un CSV (doit contenir au minimum une colonne date et une colonne index)."""
    df = pd.read_csv(path)
    return df

def load_eurchf(path: Path = DATA_DIR / "raw" / "eurchf.csv") -> pd.DataFrame:
    """Charge la série EUR/CHF (doit contenir date et prix)."""
    df = pd.read_csv(path)
    return df
