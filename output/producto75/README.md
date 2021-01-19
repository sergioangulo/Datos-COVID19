# DP75 - Media Móvil de casos nuevos y de casos activos: Descripción
Este producto da cuenta de la media movil semanal de casos nuevos confirmados por region, y la de casos activos confirmados más probables por región. 

# Columnas y valores
El archivo MediaMovil_activos.csv contiene una columna 'Region', seguida por columnas correspondientes a ['fecha']. 
Estas últimas columnas contienen el promedio de casos activos en los últimos 7 días, sumando casos confirmados y casos probables.

El archivo MediaMovil_casos_nuevos.csv contiene una columna 'Region', seguida por columnas correspondientes a ['fecha']. 
Estas últimas columnas contienen el promedio de casos nuevos en los últimos 7 días.

# Fuente
Ministerio de Salud. Ver en:
https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/

# Frecuencia de actualización
Actualización diaria. 

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo no contempla los casos con región o comuna desconocida, es decir, aquellos casos en que no se registró la región de vivienda habitual en la notificación o bien son casos con domicilio en el extranjero.

**Nota aclaratoria 2:**  Los reportes del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 
