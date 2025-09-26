# bigdata-storage-lab-Ortu-o
## 🤔 Prompts de reflexión

1. **V dominante hoy y V dominante si 2× tráfico**  
   _Respuesta (3 líneas):_  
   Hoy la **Variedad (V)** es dominante, porque integro múltiples CSV con esquemas heterogéneos.  
   Si el tráfico se duplicara, la **Volumen (V)** pasaría a ser dominante, ya que el sistema tendría que procesar más filas y conservar linaje.  
   Esto justifica decisiones de agregación y validación temprana para mantener consistencia y performance.

2. **Trade-off elegido (ej.: más compresión vs CPU)**  
   _Respuesta:_  
   Se priorizó **simplicidad y CPU mínima** sobre compresión agresiva, usando CSV y pandas nativo, porque los volúmenes actuales son manejables.  
   _Cómo lo medirás:_  
   Midiendo tiempo de ingestión y normalización por archivo y comparando memoria usada en RAM.

3. **Por qué “inmutable + linaje” mejora veracidad y qué coste añade**  
   _Respuesta:_  
   Mantener los datos bronze inmutables y con `_lineage` permite rastrear origen de cada fila, asegurando reproducibilidad y auditabilidad.  
   El coste añadido es **espacio en disco extra** y mayor complejidad al unir o limpiar múltiples fuentes.

4. **KPI principal y SLA del dashboard**  
   _Respuesta:_  
   KPI principal: suma de `amount` por partner y mes (silver).  
   _Decisión habilitada:_ permite detectar rápidamente partners con ventas atípicas y priorizar acciones de negocio.  
   _Justificación de latencia:_ latencia <5 segundos es aceptable para dashboards analíticos, equilibrando refresh y carga de CSVs múltiples.

5. **Riesgo principal del diseño y mitigación técnica concreta**  
   _Respuesta:_  
   Riesgo principal: errores de formato o columnas faltantes al subir CSV heterogéneos.  
   Mitigación: validaciones tempranas, mapeo dinámico origen→canónico y mensajes de error claros en la UI, evitando que datos corruptos lleguen a silver.
