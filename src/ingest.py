# src/ingest.py
import pandas as pd
from typing import List

def tag_lineage(df: pd.DataFrame, source_name: str) -> pd.DataFrame:
    """
    Añade una columna _lineage con el nombre del archivo origen.
    """
    df = df.copy()
    df["_lineage"] = source_name
    return df


def concat_bronze(frames: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Une múltiples DataFrames bronze en uno solo.
    """
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)

