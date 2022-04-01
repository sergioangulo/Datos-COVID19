# DP95 - Defunciones sospechosas acumuladas por COVID en Chile (reporte diario): Descripción.

Los datos entregados en defunciones_sospechosas.csv (y sus versiones transpuestas y std) provienen de los reportes diarios proporcionados por la autoridad sanitaria
Esta información corresponde a los fallecimientos sopechosos por COVID registrados por el DEIS (de manera acumulada). Es importante notar que un fallecido sospechoso puede en fechas posteriores confirmarse como fallecimiento por COVID, por lo que se resta de la categoría sospechosa y se contabiliza como fallecimiento confirmado (los cuales se contabilizan en el producto 37). 
Es por lo anterior que la diferencia entre días no es necesariamente un valor positivo (ya que disminuye si es que se confirman casos sospechosos).

Este archivo es acumulativo del total de casos sospechosos. Para ver la distribución de los casos sospechosos según día de defunción, ver el producto 37.

# Fuente
Reporte diario del Ministerio de Salud. Ver en:
https://www.gob.cl/coronavirus/cifrasoficiales/#reportes
 
# Frecuencia de actualización
Diaria