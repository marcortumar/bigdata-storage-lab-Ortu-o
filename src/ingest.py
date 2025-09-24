python
import pandas as pd
import os
from pathlib import Path

class DataIngestor:
    def __init__(self, raw_data_path="data/raw"):
        self.raw_data_path = Path(raw_data_path)
        
    def load_csv_files(self):
        """Carga todos los archivos CSV del directorio raw"""
        pass
        
    def detect_schema(self, df):
        """Detecta y documenta el esquema de un DataFrame"""
        pass
        
    def create_bronze_layer(self):
        """Crea la capa bronze con datos crudos"""
        pass
