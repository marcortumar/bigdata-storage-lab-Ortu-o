# src/transform.py
import pandas as pd

def normalize_columns(df: pd.DataFrame, mapping: dict) -> pd.DataFrame:
    """
    Renombra columnas según mapping origen->canónico.
    Convierte a tipos básicos: date (datetime), amount (float).
    """
    df = df.rename(columns=mapping)
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    if "amount" in df.columns:
        # Limpieza de formatos europeos y americanos
        df["amount"] = (
            df["amount"]
            .astype(str)
            .str.replace(r"[^\d,.\-]", "", regex=True)  # quita símbolos
            .str.replace(",", ".", regex=False)         # coma a punto
        )
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    return df


def to_silver(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega datos canónicos a nivel partner-mes con sumatoria de amount.
    """
    df = df.copy()
    df["month"] = df["date"].dt.to_period("M").astype(str)
    silver = df.groupby(["partner", "month"], as_index=False).agg(
        {"amount": "sum"}
    )
    return silver
