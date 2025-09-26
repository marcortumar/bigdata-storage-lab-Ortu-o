# src/validate.py
import pandas as pd
from typing import List

def basic_checks(df: pd.DataFrame) -> List[str]:
    """
    Realiza validaciones mínimas sobre columnas canónicas: date, partner, amount.
    Devuelve lista de errores encontrados.
    """
    errors = []

    # Chequear columnas obligatorias
    required = ["date", "partner", "amount"]
    for col in required:
        if col not in df.columns:
            errors.append(f"Falta columna obligatoria: {col}")
            return errors  # sin estas columnas no se puede seguir

    # Chequear nulos
    if df["date"].isna().any():
        errors.append("Existen valores nulos en 'date'.")
    if df["partner"].isna().any():
        errors.append("Existen valores nulos en 'partner'.")
    if df["amount"].isna().any():
        errors.append("Existen valores nulos en 'amount'.")

    # Chequear tipos
    if not pd.api.types.is_datetime64_any_dtype(df["date"]):
        errors.append("'date' no es de tipo datetime.")
    if not pd.api.types.is_numeric_dtype(df["amount"]):
        errors.append("'amount' no es numérico.")

    return errors

