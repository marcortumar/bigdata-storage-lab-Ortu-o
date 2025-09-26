# ✅ Checklist de entrega

- [ https://bigdata-storage-lab-ortu-o-rrch5dgakgkamuzdexjmxy.streamlit.app] URL de la aplicación **Streamlit** funcional y accesible.
- [ data/bronze](data/silver) Archivos `bronze.csv` y `silver.csv` generados y subidos en la carpeta `/data`.
- [ ] Archivo `README.md` con:
  - [ ] Justificación de decisiones de diseño (en base a las **5V del Big Data**).
  - [ ] Explicación de elecciones técnicas (formatos, normalización, etc.).
- [ ] Carpeta `docs/` con capturas de pantalla de la aplicación en funcionamiento.
- [ ] Diccionario de datos completo (columnas canónicas, tipos, significado).
- [ ] Documento de gobernanza (reglas de validación, linaje, responsables, etc.).


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

