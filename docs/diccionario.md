# Diccionario de Datos

## Estructura de Archivos Fuente

### Archivo: ventas_[fecha].csv
- **Descripción**: Datos de ventas diarias
- **Esquema detectado**:
  - `fecha_venta`: Date (YYYY-MM-DD)
  - `producto_id`: String
  - `cantidad`: Integer
  - `monto`: Decimal

### Archivo: clientes.csv
- **Descripción**: Maestro de clientes
- **Esquema detectado**:
  - `cliente_id`: String
  - `nombre`: String
  - `region`: String
