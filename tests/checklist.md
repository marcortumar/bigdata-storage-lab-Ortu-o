- [ ] *URL de la app Streamlit funcional*
  - Pegar aquí: "https://bigdata-storage-lab-ortu-o-rrch5dgakgkamuzdexjmxy.streamlit.app"
  - La app carga, permite subir CSV y muestra bronze, silver, KPIs y descargas.

- [ ] *bronze.csv y silver.csv subidos a /data*
  - data/bronze.csv presentes.
  - data/silver.csv presentes.
  - Archivos versionados con nombres auditables.

- [ ] *README con decisiones justificadas (5V → elecciones) y capturas en docs/*
  - Justificación clara por Volumen, Velocidad, Variedad, Veracidad, Valor.
  - Capturas de la app y de tablas bronze/silver en docs/.

- [ ] *Diccionario y gobernanza completos*
  - docs/diccionario.md actualizado con esquema canónico y mapeos.
  - docs/gobernanza.md con linaje, validaciones, mínimos privilegios, trazabilidad y roles.


# 📊 Rúbrica de evaluación

Total: **10 puntos**

1. **Diseño y justificación (3 puntos)**
   - (1) Explica claramente las decisiones de normalización y agregación.
   - (1) Justifica las elecciones usando las **5V del Big Data** (volumen, velocidad, variedad, veracidad, valor).
   - (1) Relaciona la arquitectura propuesta con la problemática de negocio.

2. **Calidad de los datos (3 puntos)**
   - (1) Implementa validaciones básicas (nulos, tipos, negativos).
   - (1) KPIs de calidad sobre bronze y silver documentados.
   - (1) Evidencia de que los errores se detectan y reportan correctamente.

3. **Trazabilidad y Data Warehouse (2 puntos)**
   - (1) Uso de linaje (`_lineage`) para rastrear origen de los datos.
   - (1) Construcción de la tabla **silver** con agregación mensual por partner.

4. **Documentación (2 puntos)**
   - (1) README claro con decisiones, instrucciones y referencias.
   - (1) Evidencias en `docs/` (capturas, ejemplos) + diccionario y gobernanza.

