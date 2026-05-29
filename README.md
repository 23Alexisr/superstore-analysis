# Análisis Comercial - Superstore

## Descripción
Análisis exploratorio de datos de ventas de una tienda retail con 9,994 registros,
utilizando Python para el análisis y Power BI para la visualización interactiva.

## Herramientas utilizadas
- Python - limpieza y análisis de datos
- Pandas - manipulación de datos
- Matplotlib y Seaborn - visualizaciones
- Power BI - dashboard interactivo

## Archivos del proyecto
- `analisis_superstore.py` - script de análisis en Python
- `Superstore.csv` - dataset original
- `dashboard_superstore.pbix` - dashboard Power BI

## Análisis realizados
- Ventas totales por categoría y región
- Top 5 Sub-categorías más rentables
- Sub-categorías con pérdidas
- Análisis de márgenes de ganancia
- Clasificación de productos rentables vs no rentables
- Ganancia por segmento de cliente

## Dashboard Power BI

El dashboard tiene dos páginas:

### Página 1 - Resumen Comercial
- KPIs: Total Sales, Total Profit, Total Quantity, Total Órdenes
- Ventas totales por categoría
- Ganancias por región
- Ventas por Sub-Categoría
- Tendencia de ventas por año
- Mapa de ventas por Estado

### Página 2 - Análisis de Rentabilidad
- KPIs: Margen promedio, Profit promedio
- Relación entre ventas y ganancias por Sub-Categoría
- Ganancia por categoría
- Descuentos por categoría
- Ganancia por segmento

## Conclusiones

### Ventas
- Technology es la categoría con mayores ventas ($836,154)
- Phones y Chairs lideran en Sub-Categorías
- Las ventas crecen año a año  de 2011 a 2014 subieron 40%

### Rentabilidad
- West es la región más rentable ($108,418)
- Central es la región menos rentable ($39,706)
- Home Office es el segmento más rentable
- Copiers y Phones son las Sub-Categorías más rentables
- Binders y Tables generan pérdidas

### Descuentos
- Descuentos mayores al 40% generan pérdidas
- Office Supplies tiene los mayores descuentos
- A mayor descuento, menor ganancia - correlación negativa de -0.22

### Recomendaciones
- Reducir descuentos en Binders y Tables
- Potenciar ventas en región West
- Enfocarse en segmento Home Office por su alta rentabilidad
