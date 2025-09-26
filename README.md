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
# Plantilla General para Análisis de Casos de Uso Big Data

| V Prioritaria | Elecciones (Ingesta/Storage/Compute/Analítica) | Riesgos Clave | Mitigaciones | Métrica de Éxito |
|---------------|-----------------------------------------------|---------------|--------------|------------------|
| [Variedad/Velocidad/Volumen/Veracidad/Valor] | [Tecnologías y enfoques específicos] | [Principales desafíos] | [Estrategias de mitigación] | [KPI cuantificable] |

---

# E-commerce (Retail Online)

| Dimensión | Detalles |
|-----------|----------|
| **V Prioritaria** | **Variedad** - Múltiples fuentes heterogéneas (web, móvil, CRM, ERP, inventario) |
| **Elecciones** | **Ingesta:** Kafka + Debezium CDC<br>**Storage:** Data Lake (Parquet) + Delta Lake<br>**Compute:** Spark Structured Streaming<br>**Analítica:** Looker/Tableau + ML recomendaciones |
| **Riesgos Clave** | • Inconsistencias en datos de inventario<br>• Picos de tráfico en eventos flash sales<br>• Privacidad datos de clientes (GDPR) |
| **Mitigaciones** | • Validación en tiempo real con Great Expectations<br>• Auto-scaling clusters en Kubernetes<br>• Anonimización para analytics con tokenización |
| **Métrica de Éxito** | Aumento del 15% en tasa de conversión en 6 meses |

# Sensores IoT (Manufactura Inteligente)

| Dimensión | Detalles |
|-----------|----------|
| **V Prioritaria** | **Velocidad** - Millones de lecturas/segundo en tiempo real |
| **Elecciones** | **Ingesta:** MQTT + Kafka Connect<br>**Storage:** Time-series DB (InfluxDB/TimescaleDB)<br>**Compute:** Apache Flink para ventanas temporales<br>**Analítica:** Grafana + alertas proactivas |
| **Riesgos Clave** | • Pérdida de datos por congestión de red<br>• Latencia en detección de anomalías<br>• Coste almacenamiento masivo de telemetría |
| **Mitigaciones** | • Buffering en edge computing (AWS Greengrass)<br>• Modelos lightweight para inferencia en edge<br>• Tiered storage (hot/warm/cold) con políticas de retención |
| **Métrica de Éxito** | Tiempo medio de detección de fallos < 2 segundos |

# Logs de Fraude (Fintech/Banca)

| Dimensión | Detalles |
|-----------|----------|
| **V Prioritaria** | **Veracidad** - Calidad y confiabilidad crítica para compliance regulatorio |
| **Elecciones** | **Ingesta:** API Gateway + validación schema Avro<br>**Storage:** Blockchain-like (inmutable) + Cassandra<br>**Compute:** Rules Engine + Graph Analytics (Neo4j)<br>**Analítica:** Modelos ML explicables + dashboards auditoría |
| **Riesgos Clave** | • Falsos positivos/negativos en detección<br>• Ataques adversariales a modelos ML<br>• Requisitos regulatorios cambiantes |
| **Mitigaciones** | • Human-in-the-loop validation pipeline<br>• Ensemble de modelos con votación<br>• Audit trail completo con linaje de datos |
| **Métrica de Éxito** | Reducción del 40% en fraudes no detectados manteniendo <5% falsos positivos |

---

# Tabla Comparativa Resumen

| Caso de Uso | V Dominante | Tecnología Clave | Principal Riesgo | Mitigación Estratégica |
|-------------|-------------|------------------|------------------|------------------------|
| **E-commerce** | Variedad | Delta Lake | Inconsistencias cross-source | Validación en streaming + reconciliación batch |
| **Sensores IoT** | Velocidad | Apache Flink | Pérdida de datos en picos | Arquitectura edge-to-cloud con buffering |
| **Logs Fraude** | Veracidad | Graph Analytics | Falsos positivos | Ensemble learning + feedback humano |

**Patrón de Diseño Común:** 
- Todos requieren balance entre **latencia**, **costo** y **precisión**
- Elecciones técnicas alineadas con la "V" dominante de cada dominio
- Arquitecturas escalables pero con controles de calidad apropiados al riesgo del negocio
