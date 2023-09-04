# DP1 - Casos totales por comuna incremental: Descripción
Archivo que da cuenta de los casos confirmados y probables notificados (desde el 19 de junio, informe #27 se incluyen los casos probables) en cada una de las comunas de Chile, según residencia, y concatena la historia de los informes epidemiológicos publicados por el Ministerio de Salud del país.

Se entiende por Caso probable: persona que cumple los criterios de definición de caso sospechoso con una muestra “indeterminada” a SARS-CoV-2 o bien personas en contacto estrecho con un caso confirmado que desarrollan al menos un síntoma compatible con COVID-19.

Se entiende por Caso confirmado: persona notificada que cumple los criterios de definición de caso sospechoso o probable con una muestra positiva a SARS-CoV-2, o bien persona no notificada con un registro de resultado de laboratorio positiva a SARS-CoV-2.
Se entiende por comuna de residencia la comuna que la persona declara como su vivienda habitual. 

# Columnas y valores
El archivo Covid-19.csv contiene las columnas 'Región', ‘Código Región’, 'Comuna', ‘Código comuna’, 'Población', múltiples columnas correspondientes a '[fecha]', y una columna 'Tasa'. Estas últimas columnas, ‘[fecha]’, contienen los 'Casos Confirmados' reportados por el Ministerio de Salud de Chile en cada una de las fechas que se indican en las respectivas columnas. La columna 'Tasa' contiene el número de casos confirmados por cada 100 mil habitantes de una población. El archivo Covid-19_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Informes epidemiológicos publicados periódicamente por el Ministerio de Salud de Chile. Ver en:
https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/

A su vez, el Ministerio de Salud utiliza como fuente para la elaboración de estos informes el Sistema de notificación EPIVIGILA, del Departamento de Epidemiología, DIPLAS. 

# Frecuencia de actualización

Cada 2 a 3 días.

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo no contempla los casos con región o comuna desconocida, es decir, aquellos casos en que no se registró la región de vivienda habitual en la notificación o bien son casos con domicilio en el extranjero. 

**Nota aclaratoria 2:** Los informes epidemiológicos del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

**Nota aclaratoria 3:** Previo al 15 de abril de 2020 los informes epidemiológicos del Ministerio de Salud no entregaban datos de confirmados notificados en comunas con bajo número de casos, para proteger la identidad de las personas contagiadas. 

**Nota aclaratoria 4:** Acorde a lo informado por Epidemiología MINSAL, los datos de residencia son provisorios a la fecha del último reporte, pues se van actualizando retroactivamente a medida que se confirman casos y evoluciona la investigación epidemiológica.

**Nota aclaratoria 5:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

---
---
<br><br><br>

# DP2 - Casos totales por comuna: Descripción
Serie de archivos que dan cuenta de los casos confirmados y casos probables (desde el 19 de junio, informe #27) notificados en cada una de las comunas de Chile, según residencia. Cada uno de los archivos corresponde a un informe publicado por el Ministerio de Salud del país, por fechas en que fueron publicados. 

Se entiende por Caso probable: persona que cumple los criterios de definición de caso sospechoso con una muestra “indeterminada” a SARS-CoV-2 o bien personas en contacto estrecho con un caso confirmado que desarrollan al menos un síntoma compatible con COVID-19. 

Se entiende por Caso confirmado: persona notificada que cumple los criterios de definición de caso sospechoso o probable con una muestra positiva a SARS-CoV-2, o bien persona no notificada con un registro de resultado de laboratorio positiva a SARS-CoV-2.

Se entiende por comuna de residencia la comuna que la persona declara como su vivienda habitual. 

# Columnas y valores
El archivo contiene las columnas 'Región', ‘Código Región’, 'Comuna', ‘Código comuna’, 'Población' y 'Casos Confirmados'. Estos valores están separados entre sí por comas (csv).

# Fuente

Informes epidemiológicos publicados periódicamente por el Ministerio de Salud de Chile. Ver en:
https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/

A su vez, el Ministerio de Salud utiliza como fuente para la elaboración de estos informes el Sistema de notificación EPIVIGILA, del Departamento de Epidemiología, DIPLAS. 

# Frecuencia de actualización
Cada 2 a 3 días. 

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo no contempla los casos con región o comuna desconocida, es decir, aquellos casos en que no se registró la región de vivienda habitual en la notificación o bien son casos con domicilio en el extranjero. 

**Nota aclaratoria 2:**  Los informes epidemiológicos del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

**Nota aclaratoria 3:** Previo al 15 de abril de 2020 los informes epidemiológicos del Ministerio de Salud no entregaban datos de confirmados notificados en comunas con bajo número de casos, para proteger la identidad de las personas contagiadas. 

**Nota aclaratoria 4:** Acorde a lo informado por Epidemiología MINSAL, los datos de residencia son provisorios a la fecha del último reporte, pues se van actualizando retroactivamente a medida que se confirman casos y evoluciona la investigación epidemiológica. A raíz de eso se recomienda utilizar el [Data Product 1 - Casos totales por comuna incremental](https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto1) para contar con la información más actualizada.

**Nota aclaratoria 5:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

---
---
<br><br><br>

# DP3 - Casos totales por región: Descripción
Este producto da cuenta de los casos totales diarios confirmados por laboratorio en cada una de las regiones de Chile, según residencia, y concatena la información reportada por el Ministerio de Salud del país. 

Los archivos TotalesPorRegion('.csv', '_T.csv' y '_std.csv') ensamblan las distribuciones regionales de: Casos acumulados, Casos nuevos totales, Casos nuevos con sintomas, Casos nuevos sin sintomas, Casos nuevos sin notificar y Fallecidos totales.

Se entiende por caso confirmado la persona que cumple con los criterios de definición de caso sospechoso con una muestra positiva de SARS-CoV-2.

Se entiende por región de residencia la región que la persona declara como su vivienda habitual. Se entiende por porcentaje de casos totales el porcentaje del número total de casos registrados en el país. 

# Columnas y valores
El archivo TotalesPorRegion.csv contiene una columna 'Region' seguida por 'Categoria', seguida por columnas correspondientes a ['fecha']. 
Estas últimas columnas contienen los casos por 'Categoria' ordenados de la siguiente manera:

filas, Distribución:<br/>
2-17 Distribución de los Casos acumulados, fila 18: total de esta distribución<br/>
19-34 Distribución de los Casos nuevos totales, fila 35: total de esta distribución<br/>
36-51 Distribución de los Casos nuevos con sintomas, fila 52: total de esta distribución<br/>
53-68 Distribución de los Casos nuevos sin sintomas, fila 69: total de esta distribución<br/>
70-85 Distribución de los Casos nuevos sin notificar, fila 86: total de esta distribución<br/>
87-102 Distribución de los Fallecidos totales, fila 103 total de esta distribución<br/>
104-119 Distribución de los Casos confirmados recuperados, fila 120 total de esta distribución<br/>
121-136 Distribución de los Casos activos confirmados, fila 137 total de esta distribución<br/>
138-153 Distribución de los Casos activos probables, fila 154 total de esta distribución<br/>
155-170 Distribución de los Casos probables acumulados, fila 171 total de esta distribución<br/>

Cada una de las Categorías son reportadas por el Ministerio de Salud de Chile.

El archivo CasosTotalesCumulativo.csv contiene una columna 'Región', seguida por columnas correspondientes a '[fecha]'. Estas últimas columnas, ‘[fecha]’, contienen los 'Casos acumulados' reportados por el Ministerio de Salud de Chile en cada una de las fechas que se indican en las respectivas columnas. El archivo CasosTotalesCumulativo_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Ministerio de Salud. Ver en:
https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/

# Frecuencia de actualización
Actualización diaria. 

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo no contempla los casos con región o comuna desconocida, es decir, aquellos casos en que no se registró la región de vivienda habitual en la notificación o bien son casos con domicilio en el extranjero.

**Nota aclaratoria 2:**  Los reportes del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

**Nota aclaratoria 3:** Previo al 15 de abril de 2020 los reportes del Ministerio de Salud no entregaban datos de confirmados notificados en comunas con bajo número de casos, para proteger la identidad de las personas contagiadas. 

**Nota aclaratoria 4:** Dado que los archivos TotalesPorRegion('.csv', '_T.csv' y '_std.csv') contienen los datos reportados en CasosTotalesCumulativo, este último se deprecará en dos semanas.


---
---
<br><br><br>

# DP4 - Casos totales por región: Descripción
Serie de archivos que dan cuenta del número de casos nuevos, del total de casos confirmados, recuperados (antes del 21 de marzo) % de casos totales y casos fallecidos en cada una de las regiones de Chile, según residencia. Cada uno de los archivos corresponde a la información diaria que reporta el Ministerio de Salud del país. Existe variabilidad en los campos según la fecha (ver sección Columnas y valores).

Se entiende por caso confirmado la persona que cumple con los criterios de definición de caso sospechoso con una muestra positiva de SARS-CoV-2.

Se entiende en este reporte los casos recuperados como las personas que tras ser confirmadas de COVID-19, han estado en cuarentena pasando 14 días sin síntomas. Para calcular recuperados de otra manera, se puede utilizar el [producto 15: Casos nuevos por fecha de inicio de sintomas](https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto15). 

Se entiende por región de residencia la región que la persona declara como su vivienda habitual. 

Se entiende por porcentaje de casos totales el porcentaje del número total de casos registrados en el país. 

# Columnas y valores
Los archivos correspondientes a fechas anteriores al 21-03-2020 (inclusive), contienen las columnas ‘Región’, ‘Casos nuevos’, ‘Casos totales’ y ‘Casos recuperados’. 

Los archivos correspondientes a fechas desde el 22-03-2020 al 25-03-2020 (inclusive), contienen las columnas 'Región', ‘Casos nuevos’, ‘Casos totales’ y ‘Fallecidos’. 

Los archivos correspondientes a fechas desde el 26-03-2020 al 04-04-2020 (inclusive), contienen las columnas 'Región', ‘Casos nuevos’, ‘Casos totales’, ‘Casos recuperados’ y ‘Fallecidos’.

Los archivos correspondientes a fechas desde el 05-04-2020 en adelante, contienen las columnas 'Región', ‘Casos nuevos’, ‘Casos totales’, ‘% de casos totales’ y ‘Fallecidos’.

La última fila contiene Totales. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Ministerio de Salud. Ver en:
https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/

# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo no contempla los casos con región o comuna desconocida, es decir, aquellos casos en que no se registró la región de vivienda habitual en la notificación o bien son casos con domicilio en el extranjero. 

**Nota aclaratoria 2:**  Los reportes del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

**Nota aclaratoria 3:** Previo al 15 de abril de 2020 los reportes del Ministerio de Salud no entregaban datos de confirmados notificados en comunas con bajo número de casos, para proteger la identidad de las personas contagiadas. 


---
---
<br><br><br>

# DP5 - Totales Nacionales Diarios: Descripción
Set de 2 archivos sobre casos a nivel nacional. El primero de ellos (TotalesNacionales.csv) incluye los casos nuevos confirmados, totales o acumulados, fallecidos a nivel nacional, activos y recuperados según fecha de diagnóstico y según fecha de inicio de síntomas, reportados diariamente por el Ministerio de Salud desde el 03-03-2020 y proyectados desde el 8 de junio para el caso de activos y recuperados por fecha de diagnóstico según criterios de la autoridad sanitaria.

Se entiende por caso confirmado la persona que cumple con los criterios de definición de caso sospechoso con una muestra positiva de SARS-CoV-2.

Se entiende por caso nuevo sin síntomas por casos que han sido confirmados COVID-19 positivos pero no tienen manifestación clínica de la enfermedad. La autoridad de salud indicó que estos casos se han testeado por cercanía con contagiados de diversas índoles.

Se entiende por casos totales o acumulados el número total de casos confirmados desde el primer caso confirmado hasta la fecha de elaboración del reporte o informe. 

Se entiende en este reporte por "recuperados por fecha de diagnóstico" la proyección de personas que tras ser confirmadas de COVID-19, han estado en cuarentena pasando 14 días sin síntomas. Se entiende en este reporte por "recuperados por fecha de inicio de síntomas" la proyección de recuperados que tras ser confirmados, reportan su fecha de inicio de síntomas y han transcurrido 14 días o más desde ella.

Se entiende en este reporte por casos activos la diferencia entre el total de casos confirmados y (personas recuperadas y personas fallecidas). Para calcularlos segun fecha de incio de síntomas se utilizan los recuperados por fecha de incio de síntomas, y por fecha de diagnóstico los recuperados por fecha de diagnóstico.

# Columnas y valores
El primer archivo (TotalesNacionales.csv) contiene las filas ‘Fecha’, ‘Casos nuevos’, ‘Casos totales’, ‘Fallecidos’, ‘Casos activos por FIS’, ‘Casos recuperados por FIS’, 'Casos activos por FD’, ‘Casos recuperados por FD’. Estos valores están separados entre sí por comas (csv).

# Fuente
Ministerio de Salud. Ver en:
https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/

# Frecuencia de actualización
Actualización diaria. 

# Notas aclaratorias

**Nota aclaratoria 1**:  Los reportes del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

**Nota aclaratoria 2**: Previo al 15 de abril de 2020 los reportes del Ministerio de Salud no entregaban datos de confirmados notificados en comunas con bajo número de casos, para proteger la identidad de las personas contagiadas.

**Nota aclaratoria 3**: A partir del 2 de junio las series por Fecha de Diagnóstico se dejaron de reportar diariamente, pero se mantiene el cálculo acá a pedida de varios usuarios que quieren continuar utilizando dichas curvas.


---
---
<br><br><br>

# DP6 - Enriquecimiento del Data Product 2: Descripción
Set de 2 archivos, en formato CSV y JSON, que dan cuenta de la tasa de incidencia acumulada y los casos confirmados acumulados en cada una de las comunas de Chile, según residencia, conforme a los informes epidemiológicos publicados por el Ministerio de Salud del país. Esto es una mejora derivada del [producto 2](https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto2), al colocar varios archivos de aquel producto en un solo archivo.

Se entiende por caso confirmado la persona que cumple con los criterios de definición de caso sospechoso con una muestra positiva de SARS-CoV-2.

Se entiende por comuna de residencia la comuna que la persona declara como su vivienda habitual. 

Se entiende por casos acumulados el número total de casos confirmados desde el primer caso confirmado hasta la fecha de elaboración del reporte o informe. 

Se entiende por tasa de incidencia acumulada el número total de casos acumulados en relación a la población susceptible de enfermar en un período determinado. 

# Columnas y valores
El archivo con valores separados entre sí por comas (csv) contiene las columnas ‘Población’, ‘Casos Confirmados’, ‘Fecha’, ‘Region ID’’, ‘Región’, ‘Provincia ID’, ‘Provincia’, ‘Comuna ID’ y ‘Tasa’. El código de comuna es siguiendo estandar del 2017.

El archivo json contiene las tuplas correspondiente a esta información por comuna.

# Fuente
Informes epidemiológicos publicados periódicamente por el Ministerio de Salud de Chile. Ver en:
https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/

A su vez, el Ministerio de Salud utiliza como fuente para la elaboración de estos informes el Sistema de notificación EPIVIGILA, del Departamento de Epidemiología, DIPLAS. 

# Frecuencia de actualización
Cada 2 a 3 días. 

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo no contempla los casos con región o comuna desconocida, es decir, aquellos casos en que no se registró la región de vivienda habitual en la notificación o bien son casos con domicilio en el extranjero. 

**Nota aclaratoria 2:**  Los informes epidemiológicos del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

**Nota aclaratoria 3:** Previo al 15 de abril de 2020 los informes epidemiológicos del Ministerio de Salud no entregaban datos de confirmados notificados en comunas con bajo número de casos, para proteger la identidad de las personas contagiadas. 

**Nota aclaratoria 4:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

---
---
<br><br><br>

# DP7 - Exámenes PCR por región de toma de muestra: Descripción
Set de 2 archivos que dan cuenta del número de exámenes PCR realizados por región reportados diariamente por el Ministerio de Salud, desde el 09-04-2020. 

El proceso ocurre hasta la fecha de la siguiente manera: 1) Paciente va al médico 2) Médico identifica síntomas que constituyen caso sospechoso y ordena tomar muestras y realizar test PCR 3) Las muestras van al laboratorio para test PCR.

# Columnas y valores
El archivo (PCR.csv) contiene las columnas ‘Región’, ‘Código Región’ y ‘Población’, seguidas por columnas correspondientes a ‘[Fecha]’. Estas últimas columnas, ‘[Fecha]’ indican el número de exámenes realizados por región, desde el 09-04-2020 hasta la fecha. El archivo PCR_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Reporte diario del Ministerio de Salud. Ver en: https://www.gob.cl/coronavirus/cifrasoficiales/#reportes

# Frecuencia de actualización
Actualización diaria. 

# Notas aclaratorias

**Nota aclaratoria 1:** Los reportes del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

**Nota aclaratoria 2:** El número de exámenes PCR realizados no refleja necesariamente la cantidad de muestras tomadas por región. En algunos casos el número de exámenes PCR realizados es menor al número de muestras dado que ha sido alcanzada la capacidad máxima de diagnóstico de la región. Por lo mismo, algunas de las muestras son enviadas a laboratorios ubicados fuera de la región de referencia. 

---
---
<br><br><br>

# DP8 - Pacientes COVID-19 en UCI por región: Descripción
Set de 2 archivos que dan cuenta del número de pacientes en UCI, y que son casos confirmados por COVID-19, por región reportados diariamente por el Ministerio de Salud, desde el 01-04-2020.

# Columnas y valores
El archivo UCI.csv contiene las columnas ‘Región’, ‘Código Región’ y ‘Población’, y múltiples columnas correspondientes a ‘[Fecha]’. Estas últimas columnas, ‘[Fecha]’ indican el número de pacientes en UCI por región, desde el 01-04-2020 hasta la fecha. El archivo UCI_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Reporte diario del Ministerio de Salud. Ver en:
https://www.gob.cl/coronavirus/cifrasoficiales/#reportes

# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** Los reportes del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

---
---
<br><br><br>

# DP9 - Pacientes COVID-19 en UCI por grupo de edad: Descripción
Set de 2 archivos que dan cuenta del número de pacientes en UCI por grupos etarios (<=39; 40-49; 50-59; 60-69; y >=70) y que son casos confirmados por COVID-19, reportados diariamente por el Ministerio de Salud, desde el 01-04-2020.

# Columnas y valores
El archivo HospitalizadosUCIEtario.csv contiene la columna ‘Grupo de edad’, seguida por columnas correspondientes a ‘[Fecha]’. Estas últimas columnas, ‘[Fecha]’, indican el número de pacientes en UCI por grupo etario, desde el 01-04-2020 hasta la fecha. El archivo HospitalizadosUCIEtario_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Reporte diario del Ministerio de Salud. Ver en:
https://www.gob.cl/coronavirus/cifrasoficiales/#reportes

# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** Los reportes del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

---
---
<br><br><br>

# DP10 - Fallecidos con COVID-19 por grupo de edad: Descripción
Set de 2 archivos que dan cuenta del número de personas fallecidas con COVID-19, agrupadas por rangos etarios (<=39; 40-49; 50-59; 60-69; 70-79; 80-89; y >=90) reportados diariamente por el Ministerio de Salud, desde el 09-04-2020.

# Columnas y valores
El archivo FallecidosEtario.csv contiene la columna ‘Grupo de edad’, seguida por columnas correspondientes a ‘[Fecha]’. Estas últimas columnas, ‘[Fecha]’, indican el número de personas fallecidas por grupo etario, desde el 09-04-2020 hasta la fecha. El archivo FallecidosEtario_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Reporte diario del Ministerio de Salud. Ver en:
https://www.gob.cl/coronavirus/cifrasoficiales/#reportes

# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** Los reportes del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

**Nota aclaratoria 2:** Los datos son provisorios a la fecha del último reporte, pues se van actualizando retroactivamente a medida que se confirman casos y evoluciona la vigilancia e investigación epidemiológica desarrollada por el Departamento de Epidemiología del Ministerio de Salud del país.

---
---
<br><br><br>

# DP11 - Enriquecimiento del Data Product 4: Descripción
El [Data Product 4](../producto4) con todos los datos compilados en formato CSV y JSON, en un solo archivo, llamados producto4.csv y producto4.json respectivamente. Set de 2 archivos, en formato CSV y JSON, que dan cuenta de la tasa de incidencia acumulada y los casos nuevos, los acumulados confirmados y los fallecidos en cada una de las regiones de Chile, según los datos diariamente reportados por el Ministerio de Salud, desde el 03-03-2020. 

Se entiende por caso confirmado la persona que cumple con los criterios de definición de caso sospechoso con una muestra positiva de SARS-CoV-2.

Se entiende por comuna de residencia la comuna que la persona declara como su vivienda habitual. 

Se entiende por casos acumulados el número total de casos confirmados desde el primer caso confirmado hasta la fecha de elaboración del reporte o informe. 

Se entiende por tasa de incidencia acumulada el número total de casos acumulados en relación a la población susceptible de enfermar en un período determinado. 

# Columnas y valores
Los archivos contienen las columnas ‘Región’, ‘Nuevos Casos’, ‘Casos Confirmados’, ‘Fallecidos’, ‘Fecha’, ‘Región ID’, ‘Población’ y ‘Tasa’. Estos valores están separados entre sí por comas (csv), y organizados en tuplas en el caso del JSON.

# Fuente
Reporte diario del Ministerio de Salud. Ver en:
https://www.gob.cl/coronavirus/cifrasoficiales/#reportes

# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1**: Los reportes del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

**Nota aclaratoria 2**: Los datos son provisorios a la fecha del último reporte, pues se van actualizando retroactivamente a medida que se confirman casos y evoluciona la vigilancia e investigación epidemiológica desarrollada por el Departamento de Epidemiología del Ministerio de Salud del país.

**Nota aclaratoria 3**: Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

---
---
<br><br><br>

# DP12 - Enriquecimiento del Data Product 7: Descripción
El [Data Product 7](../producto7) con todos los datos compilados en formato CSV y JSON, en un solo archivo, llamados producto7.csv y producto7.json respectivamente. Set de 2 archivos, en formato CSV y JSON, que dan cuenta de la tasa de incidencia acumulada y el número de PCR realizados en cada una de las regiones de Chile, según los datos diariamente reportados por el Ministerio de Salud, desde el 09-04-2020.

Se entiende por casos acumulados el número total de casos confirmados desde el primer caso confirmado hasta la fecha de elaboración del reporte o informe. 

Se entiende por tasa de incidencia acumulada el número total de casos acumulados en relación a la población susceptible de enfermar en un período determinado. 

# Columnas y valores
Los archivos contienen las columnas ‘Región’, ‘Población’, ‘Fecha’, ‘PCR Realizados’, ‘Región ID’, y ‘Tasa’. Estos valores están separados entre sí por comas (csv), y organizados en tuplas en el JSON.

# Fuente
Reporte diario del Ministerio de Salud. Ver en:
https://www.gob.cl/coronavirus/cifrasoficiales/#reportes

# Frecuencia de actualización
Actualización diaria. 

# Notas aclaratorias
**Nota aclaratoria 1**: Los reportes del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs.

**Nota aclaratoria 2**: Los datos son provisorios a la fecha del último reporte, pues se van actualizando retroactivamente a medida que se confirman casos y evoluciona la vigilancia e investigación epidemiológica desarrollada por el Departamento de Epidemiología del Ministerio de Salud del país.

**Nota aclaratoria 3**: Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

---
---
<br><br><br>

# DP13 - Casos nuevos totales por región incremental: Descripción
Set de 2 archivos que dan cuenta del número de casos nuevos por día según resultado del diagnóstico, por región de residencia, reportados por el Ministerio de Salud desde el 03-03-2020. 

A partir del 29 de abril esta serie de tiempo incluye los casos nuevos sin síntomas, es decir es el total de casos nuevos (sin síntomas + con síntomas)

También existe el [producto 15: Casos nuevos por fecha de inicio de sintomas](https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto15) que reporta casos nuevos por fecha de inicio de síntomas, resultado de la vigilancia e investigación epidemiológica del Ministerio de Salud de Chile.

# Columnas y valores
El archivo CasosNuevosCumulativo.csv contiene la columna ‘Región’, seguida por columnas correspondientes a ‘[Fecha]’. Estas últimas columnas, ‘[Fecha]’, indican el número de casos nuevos acumulativos, por región, desde el 03-03-2020 hasta la fecha. El archivo CasosNuevosCumulativo_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Reporte diario del Ministerio de Salud. Ver en:
https://www.gob.cl/coronavirus/cifrasoficiales/#reportes

# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** Los reportes del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs.

---
---
<br><br><br>

# DP14 - Fallecidos con COVID-19 por región incremental: Descripción
Set de 2 archivos que dan cuenta del número de personas con diagnóstico COVID-19 fallecidas por día, según región de residencia, y concatena la historia de los reportes del Ministerio de Salud desde el 22-03-2020.

Se entiende por región de residencia la región que la persona declara como la de su vivienda habitual. 

# Columnas y valores
El archivo FallecidosCumulativo.csv contiene la columna ‘Región’, seguida por columnas correspondientes a ‘[Fecha]’. Estas últimas columnas, ‘[Fecha]’, indican el número de fallecidos acumulativo, por región, desde el 22-03-2020 hasta la fecha. El archivo FallecidosCumulativo_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Reporte diario del Ministerio de Salud. Ver en: https://www.gob.cl/coronavirus/cifrasoficiales/#reportes

# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** Los reportes del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs.

**Nota aclaratoria 2:** Los datos son provisorios a la fecha del último reporte, pues se van actualizando retroactivamente a medida que se confirman casos y evoluciona la vigilancia e investigación epidemiológica desarrollada por el Departamento de Epidemiología del Ministerio de Salud del país.


---
---
<br><br><br>

# DP15 - Casos nuevos por fecha de inicio de síntomas por comuna: Descripción
Set de 4 archivos que dan cuenta de los casos nuevos por fecha de inicio de sus síntomas en cada una de las comunas 
de Chile, según residencia. Refleja la información del último informe epidemiológico publicado por el Ministerio de 
Salud del país. Se indexan estos casos según semana epidemiológica reportada en el informe, con fechas incluidas en los archivos.

Se entiende por fecha de inicio de síntomas el momento de la manifestación clínica de la enfermedad. Se entiende por 
comuna de residencia la comuna que la persona declara como su vivienda habitual. 

# Columnas y valores
El archivo FechaInicioSintomas.csv contiene las columnas 'Region', 'Código región', 'Comuna', 'Código comuna', 'Población' 
y una serie de columnas 'SE7', 'SE8', ..., que corresponden a semanas epidemiológicas. Los valores por fila corresponden 
a tuplas de comunas con sus respectivos metadatos, y la cantidad de casos confirmados por semana epidemiológica en cada 
columna 'SE...'. El archivo FechaInicioSintomas_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. 
Se incluye el archivo FechaInicioSintomas_std.csv que contiene la misma data de FechaInicioSintomas.csv en formato 
estándar (unpivoted). El tercer archivo (SemanasEpidemiologicas.csv) contiene una columna de Fecha, y columnas 
'SE...', con dos filas que indican la fecha de inicio de la semana epidemiológica, y la fecha de término de la misma. 
Todos estos valores están separados entre sí por comas (csv).

El archivo FechaInicioSintomas_std.csv contiene la misma data de FechaInicioSintomas.csv en formato estándar (unpivoted)

El archivo FechaInicioSintomasHistorico_std.csv contiene el registro de los reportes, dado que su naturaleza es dinámica,
ofreciendo una manera rápida para comparar los datos entregados en distintos períodos para las mismas semanas epidemiológicas.

# Fuente
Informes epidemiológicos publicados periódicamente por el Ministerio de Salud de Chile. Ver en:
https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/

A su vez, el Ministerio de Salud utiliza como fuente para la elaboración de estos informes el Sistema de notificación EPIVIGILA, del Departamento de Epidemiología, DIPLAS. 

# Frecuencia de actualización

Cada 2 a 3 días. 

# Notas aclaratorias

**Nota aclaratoria 1:** Los datos son provisorios a la fecha del último reporte, pues se van actualizando retroactivamente a medida que se confirman casos y evoluciona la vigilancia e investigación epidemiológica desarrollada por el Departamento de Epidemiología del Ministerio de Salud del país.

**Nota aclaratoria 2:** El archivo no contempla los casos con región o comuna desconocida, es decir, aquellos casos en que no se registró la región de vivienda habitual en la notificación o bien son casos con domicilio en el extranjero. 

**Nota aclaratoria 3:** Los informes epidemiológicos del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

**Nota aclaratoria 4:** Previo al 15 de abril de 2020 los informes epidemiológicos del Ministerio de Salud no entregaban datos de confirmados notificados en comunas con bajo número de casos, para proteger la identidad de las personas contagiadas. 

**Nota aclaratoria 5:** Acorde a lo informado por Epidemiología MINSAL, la fecha de inicio de síntomas corresponde al momento de la manifestación clínica de la enfermedad, y son provisorios a la fecha del último reporte, pues se van actualizando retroactivamente a medida que se confirman casos y evoluciona la investigación epidemiológica.

**Nota aclaratoria 6:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

---
---
<br><br><br>

# DP16 - Casos por genero y grupo de edad: Descripción
Archivo que da cuenta del número acumulado de casos confirmados distribuidos por género y grupo de edad, para cada fecha reportada. Este concatena la historia de los informes epidemiológicos publicados por el Ministerio de Salud del país.

Se entiendo por caso confirmado a la persona que cumple con los criterios de definición de casos sospechoso con una muestra positiva de SARS-CoV-2.

# Columnas y valores
El archivo CasosGeneroEtario.csv contiene las columnas 'Grupo de edad' tal como lo reporta el departamento de Epidemiología para esta categoría, en incrementos de 5 años, desde 0 hasta 79, con '80 y más' como último rango; 'Sexo' con dos distinciones 'M' (las 17 primeras filas) y 'F' (las 17 últimas filas); y una serie de columnas '[Fecha]', donde se encuentra el número acumulado de casos confirmados para el rango etario y género reportados en cada publicación de Epidemiología MINSAL. El archivo CasosGeneroEtario_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Informes epidemiológicos publicados periódicamente por el Ministerio de Salud de Chile. Ver en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/

Informes de situación COVID-19 publicados periódicamente por el Ministerio de Salud de Chile. Ver en: http://epi.minsal.cl/informes-covid-19/
 
A su vez, el Ministerio de Salud utiliza como fuente para la elaboración de estos informes el Sistema de notificación EPIVIGILA, del Departamento de Epidemiología, DIPLAS.

# Frecuencia de actualización
Informe epidemiológico: Cada 2 a 3 días.

Informe situación COVID-19: Diaria

# Notas aclaratorias

**Nota aclaratoria 1:** Los informes epidemiológicos del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs.

**Nota aclaratoria 2:** Previo al 5 de abril de 2020 los informes epidemiológicos del Ministerio de Salud no entregaban datos de distribución de casos confirmados por género y grupo de edad.


---
---
<br><br><br>

# DP17 - PCR acumulado e informado en el último día por tipo de establecimientos: Descripción

Archivo que da cuenta del número total acumulado de exámenes PCR a nivel nacional y los informados durante las últimas 24 hrs. Se consideran los distintos tipos de establecimientos: Instituto de Salud Pública, Hospitales públicos y Hospitales privados. Este archivo concatena la historia de los reportes diarios publicados por el Ministerio de Salud del país.

# Columnas y valores
El archivo (PCREstablecimiento.csv), contiene las columnas 'Establecimiento' para el tipo de institución; 'Examenes', cuyas 3 primeras filas muestran el total realizado acumulado y las 3 últimas los reportados durante las últimas 24 hrs; y una serie de columnas con '[Fecha]', donde se da el número de exámenes reportados por Epidemiología MINSAL a cada fecha.

# Fuente
Reportes diarios publicados períodicamente por el Ministerio de Salud. Ver en: https://www.gob.cl/coronavirus/cifrasoficiales/#reportes
 
# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** Previo al 30 de marzo de 2020 los reportes diarios del Ministerio de Salud no entregaban datos de exámenes PCR realizados en el país.

**Nota aclaratoria 2:** En este repositorio se corrigieron 3 errores (a la fecha)

1) Error de 87 exámenes adicionales en los exámenes realizados acumulados en establecimientos privados el 25 de mayo 2020. Junto a esto, se encontró un error de 87 exámenes menos en los realizados acumulados en Hospitales públicos en la misma fecha.

2) Error de 1968 exámenes menos en los exámenes realizados acumulados en establecimientos privados el día 27 de mayo. Junto a esto, se encontró un error de 1968 exámenes adicionales en los exámenes realizados acumulados en Hospitales públicos en ese mismo día (27 de mayo 2020)

3) Error de 929 exámenes adicionales en los exámenes realizados acumulados en establecimientos privados el día 1 de junio 2020. Junto a esto, se encontró un error de 929 exámenes menos en los realizados acumulados en Hospitales públicos en ese mismo día (1 de junio 2020)

4) Error de 335 exámenes adicionales en los exámenes realizados acumulados en establecimientos privados el día 4 de junio 2020. Junto a esto, se encontró un error de 335 exámenes menos en los realizados acumulados en Hospitales públicos en ese mismo día (4 de junio 2020)

5) Error de 452 exámenes adicionales en los exámenes realizados acumulados en establecimientos privados el día 24 de junio 2020. Junto a esto, se encontró un error de 452 exámenes menos en los realizados acumulados en Hospitales públicos en ese mismo día (24 de junio 2020)

---
---
<br><br><br>

# DP18 - Tasa de incidencia historica por comuna y total regional: Descripción
Archivo que da cuenta de la tasa de incidencia acumulada en cada una de las comunas de Chile, y concatena la historia de los informes epidemiológicos publicados por el Ministerio de Salud del país.

Se entiende por tasa de incidencia al número total de casos confirmados desde el primer caso confirmado hasta la fecha de elaboración del informe epidemiológico, en relación a la población susceptible de enfermar en un periodo determinado.

Se entiendo por caso confirmado a la persona que cumple con los criterios de definición de casos sospechoso con una muestra positiva de SARS-CoV-2.

# Columnas y valores
El archivo TasadeIncidencia.csv, contiene las columnas 'Región', 'Código región', 'Comuna', 'Código comuna', 'Población', y varias columnas '[Fecha]', donde cada una tiene la 'Tasa de incidencia' reportadas en cada publicación de Epidemiología, para cada comuna, en las fechas reportadas. El archivo TasadeIncidencia_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Informes epidemiológicos publicados periódicamente por el Ministerio de Salud de Chile. Ver en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/

A su vez, el Ministerio de Salud utiliza como fuente para la elaboración de estos informes el Sistema de notificación EPIVIGILA, del Departamento de Epidemiología, DIPLAS.
 
# Frecuencia de actualización
Cada 2 a 3 días.

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo no contempla los casos con región o comuna desconocida, es decir, aquellos casos en que no se registró la región de vivienda habitual en la notificación o bien son casos con domicilio en el extranjero.

**Nota aclaratoria 2:** Los informes epidemiológicos del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs.

**Nota aclaratoria 3:** Previo al 15 de abril de 2020 los informes epidemiológicos del Ministerio de Salud no entregaban datos de confirmados notificados en comunas con bajo número de casos, para proteger la identidad de las personas contagiadas.

**Nota aclaratoria 4:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

---
---
<br><br><br>

# D19 - Casos activos por fecha de inicio de síntomas y comuna: Descripción
Archivo que da cuenta del número de casos confirmados activos notificados en cada una de las comunas de Chile, según residencia, y concatena la historia de los informes epidemiológicos publicados por el Ministerio de Salud del país.

Se entiende por caso confirmado activo a la persona viva que cumple con los criterios de definición de casos sospechoso con una muestra positiva de SARS-CoV-2, cuya fecha de inicio de síntomas en la notificación es menor o igual a 11 días a la fecha del reporte actual (considera solo vivos).

NOTA: previo al 2020-10-24 los casos activos se contaban desde la fecha de inicio de síntomas en la notificación con un número de días menor o igual a 14.

# Columnas y valores
El archivo CasosActivosPorComuna.csv, contiene las columnas 'Región', 'Código región', 'Comuna', 'Código comuna', 'Población', y una serie de columnas '[Fecha]', donde en cada una están los 'Casos activos' reportados en cada publicación de Epidemiología, por cada comuna, en cada fecha reportada. El archivo CasosActivosPorComuna_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Informes epidemiológicos publicados periódicamente por el Ministerio de Salud de Chile. Ver en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/

A su vez, el Ministerio de Salud utiliza como fuente para la elaboración de estos informes el Sistema de notificación EPIVIGILA, del Departamento de Epidemiología, DIPLAS.
 
# Frecuencia de actualización
Cada 2 a 3 días.

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo no contempla los casos con región o comuna desconocida, es decir, aquellos casos en que no se registró la región de vivienda habitual en la notificación o bien son casos con domicilio en el extranjero.

**Nota aclaratoria 2:** Los informes epidemiológicos del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs.

**Nota aclaratoria 3:** Previo al 13 de abril del 2020, los informes epidemiológicos del Ministerio de Salud no entregaban datos sobre los casos confirmados activos notificados en comunas.

**Nota aclaratoria 4:** Casos activos en este reporte (a diferencia del reporte en el [Producto 5](../producto5), corresponde al resultado de la investigación epidemiológica y considera activos a casos durante los primeros 14 días después de la fecha de inicio de sus síntomas.

**Nota aclaratoria 5:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

---
---
<br><br><br>

# DP20 - Camas Críticas Disponbles a nivel nacional: Descripción
Este producto da cuenta del número total de camas críticas en el Sistema Integrado Covid 19, el número de ventiladores disponibles y el número de ventiladores ocupados, para cada fecha reportada. Se concatena la historia de los reportes diarios publicados por el Ministerio de Salud del país.

Se entiende por número total a todos los ventiladores operativos en el Sistema Integrado Covid 19.

# Columnas y valores
En archivo NumeroVentiladores.csv, contiene las columnas 'Estado' (con valores total, disponibles, ocupados), una serie de columnas '[Fecha]', donde en cada una están los valores reportados a nivel nacional. El archivo NumeroVentiladores_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Reportes diarios publicados períodicamente por el Ministerio de Salud. Ver en: https://www.gob.cl/coronavirus/cifrasoficiales/#reportes
 
# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** Previo al 14 de abril del 2020, los reportes diarios del Ministerio de Salud no entrega información sobre la cantidad de ventiladores operativos, disponibles u ocupados.

**Nota aclaratoria 2:** A partir del reporte diario del 7 de enero, se informa como Camas críticas (antes se llamaba Ventiladores), considerando que siempre son equipadas con ventiladores mecánicos. En estos archivos se mantienen la denominaciones.

---
---
<br><br><br>

# DP21 - Sintomas por Casos Confirmados e informado en el último día: Descripción
Este producto da cuenta de la sintomatología reportada por los casos confirmados. También da cuenta de la sintomatología reportada por casos confirmados que han requerido hospitalización. Se concatena la historia de los informes de Situación Epidemiológica publicados por el Ministerio de Salud del país.

Los archivos Sintomas('.csv', '_T.csv' y '_std.csv') ensamblan la sintomatología de casos sin hospitalización y casos hospitalizados. 

Los archivos SintomasCasosConfirmados('.csv', '_T.csv' y '_std.csv') contienen la información de los archivos 'Sintomas' con categoría 'Hospitalización == NO', mientras que los archivos SintomasHospitalizados('.csv', '_T.csv' y '_std.csv') contienen la sintomatología de los archivos 'Sintomas' con categoría 'Hospitalización == SI'. Estos sets de archivos serán deprecados en 2 semanas. Se mantendrá la información concatenada en los archivos Sintomas('.csv', '_T.csv' y '_std.csv').

Se entiende por caso confirmado la persona que cumple con los criterios de definición de caso sospechoso con una muestra positiva de SARS-CoV-2.

Se entiende por paciente en hospitalización la persona que cumple con los criterios de definición de caso sospechoso con una muestra positiva de SARS-CoV-2 que ha sido ingresado en el sistema integrado y reportado por EPIVIGILA.

# Columnas y valores

El archivo Sintomas.csv contienen la columna 'Sintomas' y una serie de columnas '[Fecha]', donde por cada síntoma en una fila se reporta el número acumulado a cada fecha de casos que han reportado dicho síntoma. La sintomatología de los casos que no han requerido hospitalización a la fecha está reflejada entre las filas: 2 - 16 ('Hospitalización == NO'). Mientras que la sintomatología de los casos hospitalizados está reflejada entre las filas 17 - 31 ('Hospitalización == SI').

Los archivos SintomasCasosConfirmados.csv y SintomasHospitalizados.csv tienen una columna 'Síntomas' y una serie de columnas '[Fechas]', donde por cada síntoma en una fila, se reporta el número acumulado a cada fecha de casos confirmados con dicho síntoma (entre casos confirmados y hospitalizados, respectivamente). Cada archivo tiene una versión traspuesta (serie de tiempo) con el sufijo "\_T". Todos estos valores están separados entre sí por comas (csv).

# Fuente
Informes de Situación Epidemiológica publicados períodicamente por el departamento de Epidemiología del Ministerio de Salud con los datos reportados por EPIVIGILA. Ver en: http://epi.minsal.cl/informes-covid-19/

# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo contempla el número acumulado de casos reportando la sintomatología.

**Nota aclaratoria 2:** Posterior al 11 de abril del 2020, Los informes de Situación Epidemiológica no entregan información sobre la sintomatología de casos confirmados u hospitalizados.

**Nota aclaratoria 3:** Previo al 24 de marzo del 2020, los  informes de situación Epidemiológica del Ministerio de Salud no entrega información sobre la sintomatología de pacientes hospitalizados.

**Nota aclaratoria 4:** Previo al 10 de marzo del 2020, no hay publicaciones de los informes de situación Epidemiológica del Ministerio de Salud.

**Nota aclaratoria 5:** No todos los informes de situación COVID - 19 de EPI MINSAL contienen información sobre los síntomas.

**Nota aclaratoria 6:** Los informes de situación Epidemiológica del Ministerio de Salud se publican con fecha del día de corte. Los datos en este repositorio cotejan las fechas indicadas en el texto de la fuente utilizada con las dadas en el reporte diario e informe Epidemiológico del Ministerio de Salud.

---
---
<br><br><br>

# DP22 - Pacientes COVID-19 hospitalizados por grupo de edad: Descripción
Este producto contiene dos archivos, 1) el número acumulado del total de pacientes hospitalizados con diagnóstico COVID-19 por rango de edad y género y 2) el número acumulado de pacientes internados con diagnóstico COVID-19 en la Unidad de Cuidados Intensivos (UCI) por rango de edad. Se concatena la historia de los informes de Situación Epidemiológica publicados por el Ministerio de Salud del país.
Se entiende por paciente en hospitalización la persona que cumple con los criterios de definición de caso sospechoso con una muestra positiva de SARS-CoV-2 que ha sido ingresado en el sistema integrado y reportado por EPIVIGILA.
# Columnas y Valores
El archivo HospitalizadosEtario_Acumulado.csv contiene las columnas 'Grupo de edad','Sexo' y una serie de columnas con '[Fecha]', donde para cada fila con rango etareo (en bloques de 15 años), se indica por fecha la cantidad acumulada de hospitalizados por género. En el archivo HospitalizadosUCI_Acumulado.csv está la columa 'Grupo de edad' y una serie de columnas con '[Fecha]', donde para cada fila con rango etareo (en bloques distintos al primero), se reportan los hospitalizados UCI acumulados. Este último no tiene desglose por género. Cada archivo tiene una versión traspuesta (serie de tiempo) con el sufijo "\_T". 

Debido a un cambio en los rangos etareos el 22 de abril del 2020 los archivos presentan dos bloques con rangos de edad diferentes. Entre las filas 2 a 13 del archivo HospitalizadosEtario_Acumulado.csv, se encuentran los registros entre el 24 de marzo del 2020 al 20 de abril del 2020, para los géneros Masculino y Femenino, con rangos de edad:

00-15 años<br/>
15-29 años<br/>
30-44 años<br/>
45-59 años<br/>
60-79 años<br/>
80 y más años<br/>

A partir del 22 de abril del 2020 los rangos de edad, para los género Masculino y Femenino, publicados se describen entre las filas 14 a 27 como:

00-5 años<br/>
5-17 años<br/>
18-49 años<br/>
50-59 años<br/>
60-69 años<br/>
70-79 años<br/>
80 y más años<br/>

En el caso del archivo HospitalizadosUCI_Acumulado.csv, entre el 13 y el 20 de abril del 2020, los rangos de edad que presentan registros se encuentran entre las filas 2 a 7, y están descritos por:

< 1 años<br/>
1 - 4 años<br/>
5 - 14 años<br/>
15 - 44 años<br/>
45 - 64 años<br/>
65 y más años<br/>

A partir del 22 de abril del 2020 los rangos de edad que presentan registros se encuentran entre las filas 8 a 14, descritos como:

00-5 años<br/>
5-17 años<br/>
18-49 años<br/>
50-59 años<br/>
60-69 años<br/>
70-79 años<br/>
80 y más años<br/>

# Fuente

Informes de Situación Epidemiológica publicados períodicamente por el departamento de Epidemiología del Ministerio de Salud con los datos reportados por EPIVIGILA. Ver en: http://epi.minsal.cl/informes-covid-19/

# Frecuencia de actualización

Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo contempla el número acumulado de pacientes hospitalizados.

**Nota aclaratoria 2:** Previo al 23 de marzo del 2020, los informes de situación Epidemiológica del Ministerio de Salud no entregaban datos sobre la distribución del número de pacientes hospitalizados por rango etario.

**Nota aclaratoria 3:** Los informes de Situación Epidemiológica con fecha de publicación posterior al 21 de abril presentan un cambio en los rangos etarios. Por esta razón, hay dos escalas para los dichos rangos.

**Nota aclaratoria 4:** Los informes de situación Epidemiológica del Ministerio de Salud se publican con fecha del día de corte. Los datos en este repositorio cotejan las fechas indicadas en el texto de la fuente utilizada con las dadas en el reporte diario e informe Epidemiológico del Ministerio de Salud.

---
---
<br><br><br>

# DP23 - Pacientes críticos COVID-19: Descripción
Este producto da cuenta del número de pacientes hospitalizados con diagnóstico COVID-19 en la Unidad de Cuidados Intensivos (UCI) y se consideran en situación médica crítica. Se concatena la historia de reportes diarios publicados por el Ministerio de Salud del país.

Se entiende por paciente en hospitalización la persona que cumple con los criterios de definición de caso sospechoso con una muestra positiva de SARS-CoV-2 que ha sido ingresado en el sistema integrado y reportado por la Unidad de Gestión Centralizada de Camas (UGCC).

# Columnas y valores
El archivo PacientesCriticos.csv contiene el reporte diario de la cantidad de pacientes críticos, por cada '[Fecha]' reportada en las columnas. El archivo PacientesCriticos_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Reportes diarios publicados períodicamente por el Ministerio de Salud con los datos reportados por la Unidad de Gestión de Camas Críticas. Ver en: https://www.gob.cl/coronavirus/cifrasoficiales/#reportes

# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo contempla el número de pacientes internados en UCI en condición crítica, reportado al día.

**Nota aclaratoria 2:** Previo al 23 de marzo del 2020, los reportes diarios del Ministerio de Salud no entregaban datos sobre el número de pacientes en UCI en situación crítica.


---
---
<br><br><br>

# DP24 - Hospitalización de pacientes COVID-19 en sistema integrado: Descripción
Este producto da cuenta del número de pacientes en hospitalización con diagnóstico COVID-19 según el tipo de cama que ocupan: Básica, Media, UTI y UCI. Se concatena la historia de reportes diarios publicados por el Ministerio de Salud del país.

Se entiende por paciente en hospitalización la persona que cumple con los criterios de definición de caso sospechoso con una muestra positiva de SARS-CoV-2 que ha sido ingresado en el sistema integrado y reportado por la Unidad de Gestión Centralizada de Camas (UGCC).

Se entiende por:

**Cama básica**:  destinada a pacientes que, estando en cualquiera de las etapas de una enfermedad (evaluación, diagnóstico, tratamiento y/o recuperación), requiera hacer uso de instalaciones hospitalarias con el fin de que le sean otorgados cuidados médicos y de enfermería básicos

**Cama media**: destinada a entregar cuidados a pacientes de mediana complejidad. Se asocian a una fase aguda de enfermedad paciente, que en general debiera compensarse en pocos días.

**Camas de cuidados críticos (UTI, UCI)**: destinada a brindar cuidados de alta complejidad definida para la internación y atención de pacientes críticos, es decir, con una condición patológica que afecta uno o más sistemas, que pone en serio riesgo actual o potencial su vida y que presenta condiciones de reversibilidad. Para ellos se hace necesaria la aplicación de técnicas de monitorización, vigilancia, manejo y soporte vital avanzado hasta la compensación de sus signos vitales y hemodinámicos. El perfil de pacientes a ingresar es máximo o alto riesgo y dependencia total o parcial asociado al riesgo (CUDYR A1-A2-A3-B1-B2).

# Columnas y valores
El archivo CamasHospital_Diario.csv, corresponde al reporte diario de la cantidad de pacientes en camas (Básica, Media, UCI o en UTI). Contiene las columnas 'Tipo de Cama', y una serie de columnas '[Fecha]', donde estas contiene el número de ocupación por día, por tipo de cama. El archivo CamasHospital_Diario_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Reportes diarios publicados períodicamente por el Ministerio de Salud con los datos reportados por la Unidad de Gestión de Camas Críticas. Ver en: https://www.gob.cl/coronavirus/cifrasoficiales/#reportes

# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo contempla la cantidad de camas hospitalarias ocupadas al día.

**Nota aclaratoria 2:** Previo al 16 de abril, los reportes diarios del Ministerio de Salud no entregaban datos sobre la ocupación de camas de hospitalización.

---
---
<br><br><br>

# DP25 - Casos actuales por fecha de inicio de síntomas y comuna: Descripción
Archivo que da cuenta del número de casos actuales en cada una de las comunas de Chile según su fecha de inicio de síntomas, residencia, y concatena la historia de los informes epidemiológicos publicados por el Ministerio de Salud del país.

Se entiende por caso  actual por fecha de inicio de síntomas a la persona que cumple con los criterios de definición de casos sospechoso con una muestra positiva de SARS-CoV-2, cuya fecha de inicio de síntomas en la notificación es menor o igual a 14 días a la fecha del reporte (considera vivos y fallecidos).

Se entiende por fecha de inicio de síntomas el momento de la manifestación clínica de la enfermedad. Se entiende por comuna de residencia la comuna que la persona declara como su vivienda habitual.

# Columnas y valores
El archivo CasosActualesPorComuna.csv, contiene las columnas 'Región', 'Código región', 'Comuna', 'Código comuna', 'Población', y una serie de columnas '[fecha]', donde cada fecha tiene los 'Casos actuales' reportados en cada publicación de Epidemiología. El archivo CasosActualesPorComuna_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Informes epidemiológicos publicados periódicamente por el Ministerio de Salud de Chile. Ver en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/

A su vez, el Ministerio de Salud utiliza como fuente para la elaboración de estos informes el Sistema de notificación EPIVIGILA, del Departamento de Epidemiología, DIPLAS.
 
# Frecuencia de actualización
Cada 2 a 3 días.

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo no contempla los casos con región o comuna desconocida, es decir, aquellos casos en que no se registró la región de vivienda habitual en la notificación o bien son casos con domicilio en el extranjero.

**Nota aclaratoria 2:** Los informes epidemiológicos del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs.

**Nota aclaratoria 3:** Previo al 13 de abril del 2020, los informes epidemiológicos del Ministerio de Salud no entregaban datos sobre los casos confirmados actuales notificados en comunas.

**Nota aclaratoria 4:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

---
---
<br><br><br>

# DP26 - Casos nuevos con síntomas por región: Descripción
Set de 3 archivos que dan cuenta del número de casos confirmados nuevos por día según resultado del diagnóstico y que han presentado síntomas, por región de residencia, reportados por el Ministerio de Salud.

Esta serie de tiempo incluye los casos nuevos denominados "con síntomas" por la autoridad sanitaria.

También existe el [producto 15: Casos nuevos por fecha de inicio de sintomas](https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto15) que reporta casos nuevos por fecha de inicio de síntomas, resultado de la vigilancia e investigación epidemiológica del Ministerio de Salud de Chile.

# Columnas y valores
El archivo CasosNuevosConSintomas.csv contiene la columna ‘Región’, seguida por columnas correspondientes a ‘[Fecha]’. Estas últimas columnas, ‘[Fecha]’, indican el número de casos nuevos con síntomas por día hasta la fecha. El archivo CasosNuevosConSintomas_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. El archivo CasosNuevosConSintomas_std.csv contiene la misma data de CasosNuevosConSintomas.csv en formato estándar (unpivoted). Todos estos valores están separados entre sí por comas (csv).

# Fuente
Reporte diario del Ministerio de Salud. Ver en:
https://www.gob.cl/coronavirus/cifrasoficiales/#reportes

# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** Los reportes del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs.

---
---
<br><br><br>

# DP27 - Casos nuevos sin síntomas por región: Descripción
Set de 3 archivos que dan cuenta del número de casos confirmados nuevos por día según resultado del diagnóstico y que son asintomáticos, por región de residencia, reportados por el Ministerio de Salud.

Estos archivos incluyen datos a partir del 29 de abril. Esta serie de tiempo incluye los casos nuevos denominados "sin síntomas" por la autoridad sanitaria a partir de tal fecha. 

# Columnas y valores
El archivo CasosNuevosSinSintomas.csv contiene la columna ‘Región’, seguida por columnas correspondientes a ‘[Fecha]’. Estas últimas columnas, ‘[Fecha]’, indican el número de casos nuevos sin síntomas por día, por región, desde el 29-04-2020 hasta la fecha. El archivo CasosNuevosSinSintomas_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. El archivo CasosNuevosSinSintomas_std.csv contiene la misma data de CasosNuevosSinSintomas.csv en formato estándar (unpivoted). Todos estos valores están separados entre sí por comas (csv).

# Fuente
Reporte diario del Ministerio de Salud. Ver en:
https://www.gob.cl/coronavirus/cifrasoficiales/#reportes

# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** Los reportes del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs.

---
---
<br><br><br>

# DP28 - Casos nuevos por fecha de inicio de síntomas por Región, informado por SEREMI regionales: Descripción
Set de 3 archivos que dan cuenta de los casos nuevos por fecha de inicio de síntomas notificados por SEREMI regionales. Se indexan según semana epidemiológica reportada en el último informe epidemiológico publicado por el Ministerio de Salud del país. Estos casos tienen residencia indeterminada al momento de notificación (turistas sin domicilio conocido, pasajeros de cruceros, tripulantes de barcos mercantes, entre otros). Estos reflejan la información del último informe epidemiológico publicado por el Ministerio de Salud. Se recomienda sumar estos casos confirmados e informados por SEREMI a la suma de casos confirmados por comuna (totales regionales) dados en el [Data Product 15 - Casos nuevos por fecha de inicio de síntomas por comuna](../producto15) y a otros productos que cuenten casos con fuente el Informe Epidemiológico.

Se entiende por fecha de inicio de síntomas el momento de la manifestación clínica de la enfermedad. Se entiende por comuna de residencia la comuna que la persona declara como su vivienda habitual. 

# Columnas y valores

El archivo FechaInicioSintomas_reportadosSEREMI.csv contiene las columnas 'SEREMI notificacion', 'Codigo Region' y una serie de columnas 'SE7', 'SE8', ..., que corresponden a las semanas epidemiológicas. Los valores por fila corresponden a tuplas de SEREMI regionales con sus respectivos metadatos y la cantidad de casos confirmados por semana epidemiológica en cada columna 'SE...'. El archivo FechaInicioSintomas_reportadosSEREMI_T.csv es la versión traspuesta del primer archivo. El archivo FechaInicioSintomas_reportadosSEREMI_std.csv contiene la misma data de FechaInicioSintomas_reportadosSEREMI.csv en formato estándar (unpivoted). El archivo ([SemanasEpidemiologicas.csv](../producto15)) es útil para la lectura de estos archivos, este contiene una columna de Fecha, y columnas 'SE...', con dos filas que indican la fecha de inicio de la semana epidemiológica, y la fecha de término de la misma. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Informes epidemiológicos publicados periódicamente por el Ministerio de Salud de Chile. Ver en:
https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/

A su vez, el Ministerio de Salud utiliza como fuente para la elaboración de estos informes el Sistema de notificación EPIVIGILA, del Departamento de Epidemiología, DIPLAS. 

# Frecuencia de actualización

Cada 2 a 3 días. 

# Notas aclaratorias

**Nota aclaratoria 1:** Los datos son provisorios a la fecha del último reporte, pues se van actualizando retroactivamente a medida que se confirman casos y evoluciona la vigilancia e investigación epidemiológica desarrollada por el Departamento de Epidemiología del Ministerio de Salud del país.

**Nota aclaratoria 2:** Los informes epidemiológicos del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

**Nota aclaratoria 3:** Acorde a lo informado por Epidemiología MINSAL, la fecha de inicio de síntomas corresponde al momento de la manifestación clínica de la enfermedad, y son provisorios a la fecha del último reporte, pues se van actualizando retroactivamente a medida que se confirman casos y evoluciona la investigación epidemiológica.

---
---
<br><br><br>

# DP29 - Cuarentenas Activas e Históricas: Descripción

* Desde Julio 2020, recomendamos usar: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto74

Set de 3 archivos en formato csv y un archivo en formato GeoJSON que contiene la identificación y características de las zonas de cuarentena establecidas por el Plan de Acción por Coronavirus del Gobierno de Chile.

Las zonas de cuarentena se establecen como una medida sanitaria en una extensión territorial definida que implica que las personas deben permanecer en sus domicilios habituales hasta que la autoridad disponga lo contrario.

Los criterios para la definir la cuarentena son:

- Velocidad de Propagación de la Enfermedad
- Densidad de casos por km2
- Perfil etáreo de la población del territorio (adultos mayores y personas con enfermedades crónicas)
- Vulnerabilidad Social

Los archivos incluidos en el presente DP son:
- Cuarentenas-Activas.csv (Cuarentenas actualmente vigentes y futuras)
- Cuarentenas-Historicas.csv (Cuarentenas ya cumplidas incluyendo cambios dentro de una misma comuna)
- Cuarentenas-Totales.csv (Suma de cuarentenas vigentes, históricas y futuras)

# Columnas y valores

- Nombre: Nombre descriptivo de la zona de cuarentena.
- Estado: Valor codificado para estado de la cuarentena: Activa, No Activa, Futura, Sin Información.
- Alcance: Valor codificado para el alcance territorial de la cuarentena Comuna completa, Área Urbana Completa, Área Rural Completa, Sector Específico.
- Fecha de Inicio: Fecha y hora de inicio en tiempo UTC -4.
- Fecha de Término: Fecha y hora de término en tiempo UTC -4.
- Código CUT Comuna: Código Único Territorial de comuna asociada.
- Detalle: Observaciones adicionales al alcance de la cuarentena.
- Superficie en m<sup>2</sup>.
- Perímetro en m.

# Fuente
Plan de Acción del Gobierno de Chile para el COVID-19. Ver en: https://www.gob.cl/coronavirus/plandeaccion/

API Externa de Respaldo de Servicios para consulta. https://covid19.soporta.cl/datasets/0b944d9bf1954c71a7fae96bdddee464_1?geometry=-105.067%2C-44.515%2C-45.784%2C-32.531

Ejemplo de Uso: https://www.arcgis.com/apps/opsdashboard/index.html#/6d03fef7ffff4c7cbd11ef1e192e6bf2

# Frecuencia de actualización

Variable: días miércoles para cambios en áreas, días viernes para cambio de estado de las cuarentenas. Ocasionalmente se pueden decretar y activar cuarentenas en otras fechas

# Notas aclaratorias

**Nota aclaratoria 1:** La cartografía de delimitación de cuarentenas es de caracter referencial cuyos límites son obtenidos en base a fuentes oficiales para límites comunales y áreas urbanas

**Nota aclaratoria 2:** La definición territorial de la delimitación de cuarentenas está dada por la validación de distintas fuentes entre las que prima como criterio superior lo indicado por los Decretos en el Diario Oficial puesto que se encuentran diferencias sustantivas entre los mapas que muestran los distintos organismos de gobierno. Como criterio adicional para casos comunales se define la información y mapas proporcionados por los municipios e intendencias validada en acuerdo con las autoridades responsables de las medidas (Subsecretaría de Prevención del Delito y Jefatura de la Defensa Nacional de la correspondiente región)

# Notas de Versión

**11-09-2020**
- Pull request, el formato de las fechas estaba incorrecto: se había
  cambiado '-' por '/', este request arregla eso.
- y ahora con `pd.to_csv(..., index=False)`


**09-09-2020**
- Pull request de actualización de DataScienceUDD
- Se agregan cuarentenas hasta el dia 20200909, sólo se modifica el archivo `Cuarentenas-Totales.csv`.
- No se modifican las columnas `detalle`, `superficie en m` ni `perímetro en m`, ya que no conocemos la metodología de los autores originales.
- El pull request se hace para mantener funcionando el código del IM de DataScienceUDD, ver Producto 33

**03-08-2020**
- Se ajustan fechas de prórroga de cuarentenas vigentes a Indefinidas en conformidad con Res.Ex. 606 de 29 de julio
- Se ajustan cuarentenas notificadas en Res.Ex. 593 del 24 de julio de 2020
	- Término de Cuarentenas de San Antonio, San Felipe, Vitacura, Las Condes, Lo Barnechea, Ñuñoa, La Reina, Colina y Til Til
	- Incorporación de cuarentenas de Copiapó, Coquimbo, La Serena, La Calera, LA Cruz, Isla de Maipo y Puerto Montt

**24-07-2020**
- Se ajustan fechas de prórroga de cuarentenas vigentes en conformidad con Res.Ex. 575 del 22 de julio

**18-07-2020**
- Se ajustan fechas de prórroga de cuarentenas vigentes.

**15-07-2020**<br>
- Cambio de Estado en Cuarentenas Futuras a Activas (2)

**13-07-2020**
- Se incorporan Cuarentenas notificadas (Res.Ex. MINSAL 522 de 12 de julio de 2020) para el Radio Urbano de Arica (Re-ingreso) y Comuna de Rengo

**10-07-2020**
- Se ajustan fechas de prórroga de cuarentenas vigentes.

**01-07-2020**
- Se ajustan fechas de prórroga de cuarentenas vigentes.

**26-06-2020** MAJOR Update
- IMPORTANTE: Se actualizan CSV y proceso de cuarentenas para indicar fecha y hora en zona horaria de Chile Continental (UTC -4)
- Cambio de Estado en Cuarentenas Futuras a Activas (5)
- Se actualizan Cuarentenas ID 91, 92 y 93 (Antofagasta, Mejillones y Tocopilla) en conformidad a modificación establecida en punto 2 de en Res.Ex. MINSAL 479 del 24 de junio

**24-06-2020**<br>
- Se incorporan Cuarentenas decretadas en Res.Ex. MINSAL 478 del 21 de junio punto 1  (Antofagasta, Mejillones y Tocopilla)
- Se incorporan Cuarentenas decretadas en Res.Ex. MINSAL 479 del 24 de junio punto 3 a comunas de El Monte, Quillota, Talagante, Calera de Tango y Graneros.
- Se ajustan fechas de prórroga de cuarentenas vigentes en conformidad con Res.Ex. MINSAL 479 punto 1

**19-06-2020 rev2**<br>
- Cambio de Estado en Cuarentenas Futuras a Activas (5)

**19-06-2020**<br>
- Corrección de delimitación de cuarentena ID 90 (Curicó Urbano) en base a cartografía dispuesta por el Jefe de la Defensa Nacional Región del Maule

**18-06-2020**<br>
- Corrección de nombre de cuarentena ID 78 a Viña del Mar (CUT_COM 5109)
- Corrección de nombre de cuarentena ID 79 a Valparaíso (CUT_COM 5101)
- Se incorporan Cuarentenas decretadas en Res.Ex. MINSAL 467 del 17 de junio punto 2  (San Felipe, Los Andes, Rancagua, Machalí, Curicó Urbano)
- Se ajustan fechas de prórroga de cuarentenas en conformidad con punto 1 de la resolución antes mencionada

**12-06-2020**<br>
- Cambio de Estado en Cuarentenas Futuras a Activas (9)

**11-06-2020**<br>
- En conformidad con Res.Ex. MINSAL 424 del 7 de junio se cambia la catergoría de la cuarentena ID 77 (Calama) de "Área Urbana Completa" a "Comuna Completa" modificando el área en el archivo GeoJSON
- Se incorporan Cuarentenas decretadas en Res.Ex. MINSAL 448 del 10 de junio punto 3.
- Se ajustan fechas de prórroga de cuarentenas

---
---
<br><br><br>

# DP30 - Pacientes Hospitalizados en UCI con Ventilación Mecánica: Descripción
Este producto da cuenta del número de pacientes hospitalizados y que se encuentran en la Unidad de Cuidados intensivos. Específicamente se describe el número de pacientes conectados a ventilación mecánica invasiva, pacientes sin ventilación mecánica y aquellos conectados a ventilación mecánica no invasiva y que son casos confirmados por COVID-19. Se concatena la historia de reportes diarios publicados por el Ministerio de Salud del país.

Se entiende por paciente en hospitalización la persona que cumple con los criterios de definición de caso sospechoso con una muestra positiva de SARS-CoV-2 que ha sido ingresado en el sistema integrado y reportado por la Unidad de Gestión de Camas Críticas.

# Columnas y valores
El archivo PacientesVMI.csv contiene el reporte diario de la cantidad de pacientes conectados a ventilación mecánica invasiva, sin ventilación mecánica y en ventilación mecánica no invasiva, por cada '[Fecha]' reportada en las columnas. El archivo PacientesVMI_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. El archivo PacientesVMI_std.csv muestra la información del archivo PacientesVMI.csv pero en formato estándar (unpivoted). Todos estos valores están separados entre sí por comas (csv).

# Fuente
Reportes diarios publicados períodicamente por el Ministerio de Salud con los datos reportados por la Unidad de Gestión de Camas Críticas. Ver en: https://www.gob.cl/coronavirus/cifrasoficiales/#reportes

# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** Previo al 11 de abril del 2020, los reportes diarios del Ministerio de Salud no entregaban datos sobre el número de pacientes hospitalizados conectados a ventilación mecánica invasiva confirmados por COVID-19.

**Nota aclaratoria 2:** Previo al 24 de mayo del 2020, los reportes diarios del Ministerio de Salud no entregaban datos sobre el número de pacientes hospitalizados en la unidad de cuidados intensivos que no estuvieran conectados a ventilación mecánica invasiva o que estuvieran conectados a ventilación mecánica no invasiva y que fuesen casos confirmados por COVID-19.

---
---
<br><br><br>

# DP31 - Nacimientos en Chile: Descripción
Los datos aquí publicados provienen de registros administrativos correspondientes a los trámites de inscripción de nacimientos desde el año 2010.

Nacimientos se refiere a la cantidad inscrita en el Registro Civil, para la comuna a la que pertenece el recinto asistencial donde nació el infante.

# Columnas y valores
El archivo contiene las columnas 'Región', ‘Código Región’, 'Comuna', ‘Código comuna’, 'Población', múltiples columnas correspondientes a '[fecha]'. Estas últimas columnas, ‘[fecha]’, contienen los 'Nacimientos' inscritos en el Registro Civil de Chile.

# Fuente
Servicio de Registro Civil de Chile

# Frecuencia de actualización
Diaria

# Notas aclaratorias
**Nota aclaratoria 1:** El Regristo Civil de Chile elabora esta información en base a las actuaciones que le son propias y que se encuentran registradas en una fecha y hora determinada, sin embargo, estas son variables, ya que pueden ser objeto de rectificación no constituyendo, en consecuencia, una estadística oficial del Estado de Chile, materia que es competencia del Instituto Nacional de Estadísticas (INE).

---
---
<br><br><br>

# DP32 - Defunciones en Chile: Descripción
Los datos aquí publicados provienen de registros administrativos correspondientes a los trámites de defunción desde el año 2010.

Defunciones se refiere a la fecha en que se inscribió la defunción en el Registro Civil. El plazo para hacer la inscripción es de tres días desde el fallecimiento y debe realizarse en la comuna donde ocurrió el deceso.

# Columnas y valores
El archivo contiene las columnas 'Región', ‘Código Región’, 'Comuna', ‘Código comuna’, 'Población', múltiples columnas correspondientes a '[fecha]'. Estas últimas columnas, ‘[fecha]’, contienen las 'Defunciones' inscritas en el Registro Civil de Chile.

# Fuente
Servicio de Registro Civil de Chile

# Frecuencia de actualización
Archivos con valores 2020, cada 1 hora. Resto de los archivos, diaria.

# Notas aclaratorias
**Nota aclaratoria 1:** El Regristo Civil de Chile elabora esta información en base a las actuaciones que le son propias y que se encuentran registradas en una fecha y hora determinada, sin embargo, estas son variables, ya que pueden ser objeto de rectificación no constituyendo, en consecuencia, una estadística oficial del Estado de Chile, materia que es competencia del Instituto Nacional de Estadísticas (INE).

**Nota aclaratoria 2:** Los datos entre 2017-2020 son provisorios. El periodo 2017-2019 está en etapa de validación, 2020 de recolección. 

---
---
<br><br><br>

# DP33 - Movilidad en Chile: Descripción
Este producto contiene 3 series de tiempo que provienen del análisis realizado por el Instituto de Data Science de la Universidad del Desarrollo considerando el movimiento de los teléfonos móviles conectados a la red de Telefónica en el territorio nacional, de manera agrupada y anónima.  

La primera serie de tiempo (IM interno) representa la evolución del índice de movilidad interno a la comuna es una medida de los viajes que ocurren al interior de dicha unidad administrativa.  

La segunda serie de tiempo (IM externo) representa la evolución del índice de movilidad externo la comuna es una medida tanto de los viajes que tienen origen al interior de la comuna y destino al exterior de la comuna, como de los viajes que tienen origen al exterior de la comuna y destino al interior de la comuna.

La tercera serie de tiempo (IM) representa la evolución del índice de movilidad, que es la suma de estos últimos dos índices.

# Columnas y valores
Los archivos contienen las columnas 'Región', 'Código Región', 'Comuna', 'Código comuna', 'Población','Superficie_km2' y múltiples columnas correspondientes a '[fecha]'. Estas últimas columnas, '[fecha]', contienen el valor para el índice en la fecha indicada.

# Fuente
Instituto de Data Science de la Universidad del Desarrollo Bravo, Loreto, and Ferres, Leo. (2020). *The IM (Mobility Index) dataset*, electronic dataset, UDD and Ministry of Science, Chile.

# Frecuencia de Actualización
Mensual.

# Más información sobre cómo se obtienen estos datos
El Instituto de Data Science (IDS) de la Facultad de Ingeniería de la Universidad del Desarrollo (UDD) con el apoyo de Telefónica Chile y CISCO, convocaron a un equipo de expertos nacionales e internacionales para para proveer información actualizada y precisa sobre la movilidad en Chile en tiempos de cuarentena.

# Método
Los índices en este producto consideran datos anonimizados del periodo desde antes del comienzo de la crisis sanitaria (26 de febrero, 2020).

Se utilizaron registros anonimizados y agregados de telefonía para estimar el número de viajes entre comunas.  Es importante destacar que este set de datos no da la ubicación exacta de los dispositivos sino que la antena a la que se conectó. Es decir, ya por diseño tenemos una primera anonimización de la ubicación. El tema de la privacidad es fundamental para los participantes en esta iniciativa y se han adoptado los protocolos internacionales más estrictos.

Para efectos de este trabajo, consideramos un viaje el paso de una antena a otra. Para dos comunas A y B, tenemos entonces que el número de viajes de A a B queda estimado como la suma de los viajes entre antenas que se encuentran dentro de A y antenas que se encuentran dentro de B.

Para poder comparar las comunas, se utiliza un índice de movilidad (IM). El IM corresponde a cuantos viajes se realizaron dentro de una comuna específica normalizado por el número de habitantes de la comuna.

Es interesante distinguir entre los viajes dentro de la comuna `IM_interno` y los que cruzan el límite comunal `IM_externo`.

# Nota aclaratoria

El uso de este data product es independiente y separado de la autorización otorgada por el Ministerio de Ciencia, Tecnología, Conocimiento e Innovación, mediante resolución de fecha 3 de junio de 2020. Considerando lo anterior, así como las limitaciones convencionales mediante las cuales se acordó su publicación, este data product sólo admite usos no comerciales.

---
---
<br><br><br>

# DP34 - Cruce entre cuarentenas y manzanas censales
Los datos publicos del Censo 2017 cuentan con información demografica valiosa para distintas regiones geografica, como lo son la cantidad de habitantes, calidad de las viviendas o la distribución etarea. La región geografica más desagregada para la cual se encuentra disponible esta información se denomina **Manzana Censal**. Este producto indica las manzanas censales que pertenecen a cada zona de cuarentena (1).

# Columnas y valores
El archivo cuenta con 4 columnas, las cuales se describen a continuación:
* 'CuarentenaID': Id de la cuarentena en el GeoJson publicado en (1).
* 'Nombre': Nombre de la cuarentena según (1).
* 'ManzanasInFull': Listado de manzanas censales **completamente contenidas** en la zona de cuarentena (corresponden al MANZENT en los datos del censo).
* 'ManzanasInPartial': Listado de manzanas censales **parcialmente contenidas** en la zona de cuarentena (corresponden al MANZENT en los datos del censo). Se considera que una manzana censal está parcialmente contenida si tiene al menos un punto de su interior dentro de la zona de cuarentena

# Datos utilizados
* (1) Zonas de cuarentenas: Se utiliza el archivo GeoJSON de las cuarentenas publicado en https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto29
* (2) Microdatos Censo 2017 a nivel de manzana censal: Publicados por el Instituto Nacional de Estadisticas (INE) desde http://geoine-ine-chile.opendata.arcgis.com/datasets/54e0c40680054efaabeb9d53b09e1e7a_0

# Información adicional
* El producto29 (https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto29) contiene la información de los días que cada cuarentena está activa.


---
---
<br><br><br>

# DP35 - Comorbilidad por Casos Confirmados: Descripción
Este producto da cuenta de la distribución de las enfermedades crónicas más frecuentes en los casos confirmados no hospitalizados, también da cuenta de la distribución para los casos que han requerido hospitalización. Se concatena la historia de los informes de Situación Epidemiológica publicados por el Ministerio de Salud del país.

Se entiende por caso confirmado la persona que cumple con los criterios de definición de caso sospechoso con una muestra positiva de SARS-CoV-2.

Se entiende por paciente en hospitalización la persona que cumple con los criterios de definición de caso sospechoso con una muestra positiva de SARS-CoV-2 que ha sido ingresado en el sistema integrado y reportado por EPIVIGILA.

# Columnas y valores
El archivo Comorbilidad.csv tiene una columna 'Comorbilidad' donde se listan las enfermedades crónicas más frecuentes, 'Hospitalización' para mostrar si la categoría corresponde a 'NO' para los casos sin hospitalización y 'SI' para aquellos que han requerido hospitalización. También hay una serie de columnas '[Fechas]', donde por cada enfermedad crónica en una fila, se reporta el número de casos confirmados que padecen dicha enfermedad (entre casos sin y con hospitalización, respectivamente). El archivo tiene una versión traspuesta (serie de tiempo) con el sufijo "\_T". Todos estos valores están separados entre sí por comas (csv). Además se presenta un archivo en formato estándar con el sufijo "\_std.csv".

# Fuente

Informes epidemiológicos publicados periódicamente por el Ministerio de Salud de Chile. Ver en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/

A su vez, el Ministerio de Salud utiliza como fuente para la elaboración de estos informes el Sistema de notificación EPIVIGILA, del Departamento de Epidemiología, DIPLAS.

# Frecuencia de actualización
Cada 2 a 3 días.

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo contempla el número de casos reportando la enfermedad crónica que ha sido calculado a lo reportado en el informe Epidemiológico. En el informe epidemiológico se publican gráficos de porcentajes de casos confirmados con enfermedad crónica de base en las categorías sin y con hospitalización. Adicionalmente, en estos gráficos se muestra la población total en cada categoría (sin y con hospitalización). Los datos de porcentajes y población sin y con hospitalización provenientes del informe epidemiológico pueden encontrarse en https://github.com/MinCiencia/Datos-COVID19/blob/DP34/input/InformeEpidemiologico/Comorbilidad.csv.


**Nota aclaratoria 2:** Previo al 18 de mayo del 2020, los informes de situación Epidemiológica del Ministerio de Salud no entrega información sobre la comorbilidad de pacientes hospitalizados.

---
---
<br><br><br>

# DP36 - Residencias Sanitarias: Descripción

Archivo que da cuenta del número de residencias sanitarias informadas por región. Se consideran las categorias: Número de habitaciones totales, Número de usuarios en la residencia y número de residencias habilitadas. Este archivo concatena la historia de los reportes diarios publicados por el Ministerio de Salud del país.

Se entiende por residencia sanitaria a establecimientos acondicionados con habitaciones individuales, baños privados, servicios de alimentación y cuidados básicos que el Ministerio de Salud ha dispuesto. Se orientan a personas confirmadas con COVID-19 sin requerimiento de hospitalización y que, por diversos factores, no cuentan con condiciones de habitabilidad apropiadas en sus domicilios particulares, debiendo realizar aislamiento temporal en una residencia sanitaria dentro de su región.

# Columnas y valores
El archivo ResidenciasSanitarias.csv contiene las columnas 'Region', 'Categoria' donde, las filas 2 a 17 muestran la distribucion por regiones del número de habitaciones disponibles, las filas 18 a 33 tienen la distribución del número de usuarios en la residencia y de las filas 34 a la 49 está la distribución por regiones del número de residencias habilitadas. Luego, se presenta una serie de columnas con '[Fecha]', donde se da el número en cada categoría para cada fecha.

# Fuente
Reportes diarios publicados períodicamente por el Ministerio de Salud. Ver en: https://www.gob.cl/coronavirus/cifrasoficiales/#reportes
 
# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** Previo al 29 de mayo de 2020 los reportes diarios del Ministerio de Salud no entregaban datos del número de residencias sanitarias implementadas en el país.

---
---
<br><br><br>

# DP37 - Defunciones por COVID en Chile (reporte diario, provisorio): Descripción.
 
Los datos en defunciones.csv (y sus versiones transpuestas y std) provienen de los registros de inscripciones de fallecimientos del Registro Civil de Chile, cruzados diariamente con el registro de los resultados de laboratorio para el diagnóstico COVID19 en Chile (RT-PCR), que consolida y cura el Departamento de Epidemiología del Minsal.
 
Los criterios para identificar fallecidos debido a COVID19 para efectos del reporte diario en defunciones.csv son:
1) Certificado de defunción incluye COVID19 o algún término relacionado (se excluyen causas externas, como trauma).
2) Existe un examen positivo de RT-PCR para SARS-CoV-2 en la base de datos de laboratorio.
 
A su vez, los datos en defunciones_deis.csv (y sus versiones transpuestas y std) provienen del Departamento de Estadística e Información del Minsal (DEIS). El DEIS hace mejoras al registro de defunciones a medida que analiza diversas fuentes de datos, estas mejoras estudian la causa de defunción indicada en el certificado médico y la presencia de resultados RT-PCR, en caso de ser la defunción por cuadro clínico compatible a COVID19, y contar con PCR(-), o no haber sido testeado se incluye como sospechoso, mientras que si existe PCR(+) se incluye como confirmado.

En ambos archivos, la columna “Defunciones” se refiere a la fecha de defunción (no es la fecha de inscripción).

Más información relacionada con el procesamiento de esta información: https://github.com/MinCiencia/Datos-COVID19/issues/457
 
# Columnas y valores
Los archivos defunciones contienen las columnas 'Defunciones' y múltiples columnas correspondientes a '[fecha]'. Estas últimas columnas, ‘[fecha]’, contienen las 'Defunciones (por fecha de fechas de defunción)' inscritas en el Registro Civil de Chile con relación a COVID19, que al cruzar con la base de laboratorios tienen PCR positivo, y son datos provisorios a la fecha de publicación que se pueden actualizar retroactivamente.

Los archivos defunciones_deis contienen las columnas 'Confirmados', 'Sospechosos' y múltiples columnas correspondientes a '[fecha]'. Estas últimas columnas, ‘[fecha]’, contienen las 'Defunciones (por fecha de fechas de defunción)' confirmadas o sospchosas.
 
# Fuente
Servicio de Registro Civil de Chile y División de Planificación Sanitaria del Ministerio de Salud de Chile.
 
# Frecuencia de actualización
Diaria (Registro Civil) y Semanal (DEIS)
 
# Notas aclaratorias
**Nota aclaratoria 1:** El Registro Civil de Chile y el Ministerio de Salud de Chile elaboran esta información en base a las actuaciones que le son propias y que se encuentran registradas en una fecha y hora determinada, sin embargo, estas son variables, ya que pueden ser objeto de rectificación no constituyendo, en consecuencia, una estadística oficial del Estado de Chile, materia que es competencia del Instituto Nacional de Estadísticas (INE) (número de fallecidos) y del Departamento de Estadísticas e Información en Salud (DEIS), Minsal (causas de defunción).
 
**Nota aclaratoria 2:** Los datos son provisorios. Los valores reportados por día pueden variar retroactivamente en cada actualización, en la medida que se recibe información de exámenes de laboratorio pendientes.

---
---
<br><br><br>

# DP38 - Casos fallecidos por comuna: Descripción
Archivo que da cuenta del número de casos fallecidos en cada una de las comunas de Chile según su residencia, y concatena la historia de los informes epidemiológicos publicados por el Ministerio de Salud del país. Este producto refleja lo que publicó el Ministerio de Salud de Chile, a través de su departamento de epidemiología, cada vez que entregó un nuevo informe epidemiológico, lo anterior es importante para diferencia con otros productos como el prodcto37 o el producto84, que cada vez que se publican contienen una actualización de la curva completa de defunciones. Lo anterior explica diferencias en las cifras, que corresponden al avance en la observación de la realidad respecto de las defunciones para una determinada fecha.

Se entiende por casos fallecidos a las muertes confirmadas debido a COVID-19 y que se encuentran debidamente registradas en la base de datos del Registro Civil e Identificación. Para estos casos, la comuna de residencia fue obtenida desde la plataforma EPIVIGILA, o bien, se asignó la comuna de circunscripción donde fue inscrita la defunción en los casos sin comuna de residencia.

Este producto incluye casos probables y notificados por laboratorio, si se quiere un producto que considere los datos procesados por DEIS, y por ende mas estables se recomienda usar https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto61

# Columnas y valores
El archivo CasosFallecidosPorComuna.csv, contiene las columnas 'Región', 'Código región', 'Comuna', 'Código comuna', 'Población', y una serie de columnas '[Fecha]', donde cada fecha tiene los 'Casos fallecidos' reportados en cada publicación de Epidemiología. El archivo CasosFallecidosPorComuna_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Informes epidemiológicos publicados periódicamente por el Ministerio de Salud de Chile. Ver en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/

A su vez, el Ministerio de Salud utiliza como fuente para la elaboración de estos informes el Sistema de notificación EPIVIGILA, del Departamento de Epidemiología, DIPLAS.
 
# Frecuencia de actualización
Cada 2 a 3 días.

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo no contempla los casos con región o comuna desconocida, es decir, aquellos casos en que no se registró la región de vivienda habitual en la notificación o bien son casos con domicilio en el extranjero.

**Nota aclaratoria 2:** Los informes epidemiológicos del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs.

**Nota aclaratoria 3:** Previo al 12 de junio del 2020, los informes epidemiológicos del Ministerio de Salud no entregaban datos sobre los casos fallecidos por COVID-19 en comunas.

**Nota aclaratoria 4:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

---
---
<br><br><br>

# DP39 - Casos confirmados de COVID-19 según fecha de inicio de síntomas y notificación: Descripción
Set de 3 archivos que dan cuenta de los casos confirmados de COVID-19 según la fecha de inicio de síntomas y fecha de notificación a nivel nacional para los casos confirmados, no notificados y probables. Refleja la información del último informe epidemiológico publicado por el Ministerio de Salud del país.

Se entiende por fecha de inicio de síntomas el momento de la manifestación clínica de la enfermedad. Se entiende por fecha de notificación el día, mes y año en que el médico tratante realizó el registro del caso en el sistema epivigila. 

# Columnas y valores
El archivo NotificacionInicioSintomas.csv contiene la columna 'Categoria' para categorizar los casos por fecha de 'Notificación' y de 'Inicio de Sintomas', seguida por la 'Serie' que corresponde a la curva 'confirmada', 'no notificada' y 'probable'. A esto sigue la serie de columnas correspondientes a las fechas de los registros correspondientes a cada día reportado en el informe Epidemiológico. También se incluye su versión transpuesta con sufijo '_T.csv' y en formato estándar con sufijo '_std.csv'. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Informes epidemiológicos publicados periódicamente por el Ministerio de Salud de Chile. Ver en:
https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/

A su vez, el Ministerio de Salud utiliza como fuente para la elaboración de estos informes el Sistema de notificación EPIVIGILA, del Departamento de Epidemiología, DIPLAS. 

# Frecuencia de actualización

Cada 2 a 3 días. 

# Notas aclaratorias

**Nota aclaratoria 1:** Los datos son provisorios a la fecha del último reporte, pues se van actualizando retroactivamente a medida que se confirman casos y evoluciona la vigilancia e investigación epidemiológica desarrollada por el Departamento de Epidemiología del Ministerio de Salud del país.

**Nota aclaratoria 2:** Los informes epidemiológicos del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

**Nota aclaratoria 3:** Acorde a lo informado por Epidemiología MINSAL, la fecha de inicio de síntomas corresponde al momento de la manifestación clínica de la enfermedad, y son provisorios a la fecha del último reporte, pues se van actualizando retroactivamente a medida que se confirman casos y evoluciona la investigación epidemiológica.

**Nota aclaratoria 4:** En el informe epidemiológico correspondiente al 23 de Junio, la tabla 23 (páginas 67, 68 y 69) presenta errores entre las fechas 19 y 21 de junio que se corrigen en este repositorio

**Nota aclaratoria 5:** Las series 'confirmada', 'no notificada' y 'probable' han sido incluidas en el informe epidemiológico a partir del 31 de Julio 2020

---
---
<br><br><br>

﻿# DP 40 - Transporte aéreo de pasajeros semanal: Descripción
Los datos aquí publicados son provistos por la Junta de Aeronáutica Civil y corresponden a la cantidad de operaciones y el total de pasajeros transportados en avión entre cada par de regiones y ciudades..


# Columnas y valores
El archivo TransporteAereo.csv contiene las columnas ‘Semana’, ‘Inicio_Semana’, ‘Fin_semana’,‘Cod_region_origen’, ‘Region_origen’, ‘Cod_region_destino’, ‘Region_destino’, ‘Origen’, ‘Destino’, ‘Operaciones’ y ‘Pasajeros’. Todos estos valores están separados entre sí por comas (csv).


# Fuente
Los datos son entregados y actualizados por la Junta de Aeronáutica Civil.


# Frecuencia de actualización
Los datos se actualizarán semanalmente.


# Notas aclaratorias


**Nota Aclaratoria 1**: La información en este dataset no va a calzar en forma exacta con los datos disponibles en el portal de la JAC (http://www.jac.gob.cl/), ya que ellos corrigen con las bases de datos de las aerolíneas, pero solo reciben la apertura mensual.


**Nota Aclaratoria 2**: Solo se consideran operadores regulares (Jetsmart, LATAM, SKY, DAP).


**Nota Aclaratoria 3**: Las operaciones solo corresponden a carga de pasajeros.


**Nota aclaratoria 4**: En cada actualización semanal se corregirá la semana anterior a esa, ya que las aerolíneas tienen un plazo para corregir los datos reportados.


**Nota aclaratoria 5**: En cada cierre de mes, se corregirá todo el mes. La DGAC termina de validar los datos alrededor de 8 días después del cierre del mes y puede pedir cambiar cualquier dato de dicho mes.
---
---
<br><br><br>

﻿# DP 41 - Transacciones Bip!: Descripción
Los datos aquí publicados son provistos por el Directorio de Transporte Público Metropolitano (DTPRM) del Ministerio de Transporte y Telecomunicaciones en trabajo conjunto con el Instituto de Sistemas Complejos de Ingeniería (ISCI) de la Universidad de Chile. 


Los archivos dan cuenta del número de transacciones totales de la tarjeta bip! y su desagregación por comuna.


# Columnas y valores
El archivo BipTotal_std.csv contiene las columnas ‘Fecha’ y ‘Transacciones’, mientras que el archivo BipComuna_std.csv contiene las columnas ‘Fecha’, ‘Comuna’ y ‘Transacciones. Todos estos valores están separados entre sí por comas (csv).


# Fuente
Los datos son entregados y actualizados por el DTPRM en trabajo conjunto con el ISCI.


# Frecuencia de actualización
Los datos se actualizarán cada 2-4 semanas.


# Notas aclaratorias


**Nota Aclaratoria 1**: Los datos disponibilizados por comuna originalmente contemplan desde marzo de 2020 hasta mediados de mayo de 2020. En las siguientes actualizaciones se incluirán datos previos a marzo 2020 llegando hasta 2019.


**Nota Aclaratoria 2**: Las transacciones que no pueden ser asociadas a una comuna se indican con un ‘-’ en la celda correspondiente a comuna.
---
---
<br><br><br>

﻿# DP 42 - Viajes diarios por comuna en Transporte Público: Descripción
Los datos aquí publicados son provistos por el Directorio de Transporte Público Metropolitano (DTPRM) del Ministerio de Transporte y Telecomunicaciones en trabajo conjunto con el Instituto de Sistemas Complejos de Ingeniería (ISCI) de la Universidad de Chile. 


Los archivos dan cuenta del número de viajes diario entre comunas en transporte público.


# Columnas y valores
El archivo ViajesComunasTransportePublico.csv contiene las columnas ‘Fecha’, ‘Origen’, ‘Destino’ y ‘Viajes’. Todos estos valores están separados entre sí por comas (csv).


# Fuente
Los datos son entregados y actualizados por el DTPRM en trabajo conjunto con el ISCI.


# Frecuencia de actualización
Los datos se actualizarán cada 2-4 semanas.


# Notas aclaratorias


**Nota Aclaratoria 1**: Los datos disponibilizados contemplan desde marzo de 2020 hasta mediados de mayo de 2020. En las siguientes actualizaciones se incluirán datos previos a marzo 2020 llegando hasta 2019.


**Nota Aclaratoria 2**: Los datos disponibilizados no consideran la evasión.


**Nota Aclaratoria 3**: Los viajes son calculados a partir de las transacciones de la tarjeta Bip!. Dado que no existe validación de salida, el destino se estima con un algoritmo de seguimiento de validaciones desarrollado por la profesora Marcela Munizaga del ISCI de la Universidad de Chile.
---
---
<br><br><br>

# DP 34 - Datos de calidad del aire por hora: Descripción

Cada archivo entrega los datos de la emisión de un contaminante durante un año con frecuencia horaria junto con la información de las estaciones de medición. Existe un archivo para cada contaminante y para cada año.

Los contaminantes disponibles y sus unidades de medida son los siguientes: Dióxido de azufre (SO2) en partes por billón (ppb), Dióxido de Nitrógeno (NO2) en partes por billón (ppb), Monóxido de Carbono (CO) en partes por millón (ppm), Ozono (O3) en partes por billón (ppb), Material Particulado MP 10 en microgramos por metro cúbico normalizado (μg/m3N) y Material Particulado MP 2.5 en microgramo por metro cúbico (μg/m3).

Las coordenadas de la estación se encuentran en las filas UTM_Este y UTM_Norte. Corresponden a la ubicación de las estaciones y están en formato UTM y se entregan en dos filas distintas la coordenada Este (E) y la coordenada Norte (N). Para todas las estaciones el Huso horario es 19.

La comuna corresponde a donde está ubicada la estación.

# Columnas y valores

Cada archivo [CONTAMINANTE]-[20XX].csv contiene las filas  correspondientes al [CONTAMINANTE] medido en la Estación ‘[Nombre de estacion]’. Además, las primeras filas corresponden a ‘Region’, ‘Codigo Region’, ‘Comuna’, ‘Codigo Comuna’, 'UTM_Este’ y UTM_Norte’, para luego entregar las fechas y horas de medición. Todos estos valores están separados entre sí por comas (csv).

# Fuente

Los datos fueron entregados por el Sistema Nacional de Calidad del Aire del Ministerio de Medio Ambiente. Estos datos son públicos en una mayor agregación en https://sinca.mma.gob.cl/

# Frecuencia de Actualización

Esta información see actualzia 1 vez al día para los MP y 1 vez a la semana para los gases.

# Notas Aclaratorias

**Nota Aclaratoria 1**: La información disponible para todo el país es de Material Particulado 2.5 (MP 2.5) y Material particulado 10 (MP 10). El resto de las emisiones (gases) solo están disponibles para la Región Metropolitana y algunas estaciones en regiones.

**Nota Aclaratoria 2**: Los espacios en blanco corresponden a datos invalidados. Las invalidaciones pueden deberse a distintos motivos (falla de equipo, falla de energía, mantención, etc.) y se les asigna el código de invalidación correspondiente (códigos definidos en el artículo 17 del decreto Nº 61, de 2008, del Ministerio de Salud). 

---
---
<br><br><br>

# DP44 - Evolución semanal de egresos hospitalarios pacientes COVID-19

Archivo que da cuenta del número de egresos de pacientes que han sido ingresados en el sistema integrado COVID-19. Se considera el número total de egresos por semana. Este archivo concatena la historia de los reportes diarios publicados por el Ministerio de Salud del país.

Se entiende por egreso hospitalario a los pacientes que ya no se encuentran ocupando una cama de la dotación de un establecimiento autorizado para tal fin, tanto de establecimientos privados y públicos del sistema integrado y reportado por la Unidad de Gestión de Camas Críticas (UGCC).

# Columnas y valores
El archivo EgresosHospitalarios.csv contiene las columnas 'Evolución semanal' donde se etiquetan las semanas correspondientes siguiendo el patrón 'S'+'mes-día inicio semana'_'mes-día final semana' todas correspondientes al año 2020. Luego, se presenta una serie de columnas con '[Fecha]', donde se da el número de egresos por semana reportados en cada publicación del reporte diario.

# Fuente
Reportes diarios publicados períodicamente por el Ministerio de Salud. Ver en: https://www.gob.cl/coronavirus/cifrasoficiales/#reportes
 
# Frecuencia de actualización
Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** Previo al 26 de junio de 2020 los reportes diarios del Ministerio de Salud no entregaban datos del número de residencias sanitarias implementadas en el país.

---
---
<br><br><br>

# DP45 - Casos Probables, No Notificados y Confirmados por FIS por comuna: Descripción
Archivo que da cuenta de los casos probables, no notificados y confirmados notificados en cada una de las comunas de Chile, según residencia y fecha de inicio de síntomas.

Se entiende por caso probables la persona que cumple los criterios de definición de caso sospechoso con una muestra "indeterminada" a SARS-CoV-2 o bien personas en contacto estrecho con un caso confirmado que desarrollan al menos un síntoma compatible con COVID-19. Para efectos epidemiológicos, los casos probables se considerarán casos confirmados y por ende serán contabilizados dentro de los casos totales. 

Se entiende por caso no notificado el caso que tiene un examen PCR positivo para SARS-CoV-2 y no está registrado en la plataforma EPIVIGILA, es decir, no ha sido notificado a la autoridad sanitaria. Esta categoría se encuentra en etapa de verificación por lo que sus valores pueden cambiar en la medida que avanza la inestigación.

Se entiende por caso confirmado la persona notificada que cumple con los criterios de definición de caso sospechoso o probable con una muestra positiva de SARS-CoV-2, o bien persona no notificada con un registro de resultado de laboratorio positiva a SARS-CoV-2.

Se entiende por comuna de residencia la comuna que la persona declara como su vivienda habitual. 

# Columnas y valores
El archivo 'Casos'+ categoria +'PorComuna.csv' contiene las columnas 'Región', ‘Código Región’, 'Comuna', ‘Código comuna’, 'Población', y una serie de columnas 'YYYYSE', que corresponden a semanas epidemiológicas del año. Los valores por fila corresponden a tuplas de comunas con sus respectivos metadatos, y la cantidad de casos en las categorias: probables, no notificados o confirmados, por semana epidemiológica en cada columna 'SE...'. Todos estos valores están separados entre sí por comas (csv).

En el caso de las tablas con el sufijo Histórico_YYYY.csv, cuenta con una columna extra "publicación" que corresponde a cuando se publicaron los datos por parte de la autoridad sanitaria.

# Fuente
Informes epidemiológicos publicados periódicamente por el Ministerio de Salud de Chile. Ver en:
https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/

A su vez, el Ministerio de Salud utiliza como fuente para la elaboración de estos informes el Sistema de notificación EPIVIGILA, del Departamento de Epidemiología, DIPLAS. 

# Frecuencia de actualización

Cada 2 a 3 días.

# Notas aclaratorias

**Nota aclaratoria 1:** Los informes epidemiológicos del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

**Nota aclaratoria 2:** Previo al 15 de abril de 2020 los informes epidemiológicos del Ministerio de Salud no entregaban datos de confirmados notificados en comunas con bajo número de casos, para proteger la identidad de las personas contagiadas. 

**Nota aclaratoria 3:** Acorde a lo informado por Epidemiología MINSAL, los datos de residencia son provisorios a la fecha del último reporte, pues se van actualizando retroactivamente a medida que se confirman casos y evoluciona la investigación epidemiológica.

**Nota aclaratoria 4:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

---
---
<br><br><br>

# DP46 - Curva Activos vs. Recuperados: Descripción
Archivo sobre casos activos y recuperados a nivel nacional, se actualiza la curva completa diariamente. 

Se entiende en este reporte por "recuperados" la proyección de recuperados que tras ser confirmados, reportan su fecha de inicio de síntomas y han transcurrido 11 días o más desde ella.

Se entiende en este reporte por "activos", a aquellos casos que se encuentran en los primeros 11 días posteriores a su fecha de diagnóstico.

En ambos casos, se excluyen fallecidos.

# Columnas y valores
El  archivo contiene las columnas ‘Fecha’, ‘activos’, ‘recuperados’, donde cada fila presenta el total de casos activos y recuperados presentes en la fecha correspondiemnte. Estos valores están separados entre sí por comas (csv).

# Fuente
Ministerio de Salud. 

# Frecuencia de actualización
Actualización diaria. 

# Notas aclaratorias

**Nota aclaratoria 1**:  Los valores en las últimas dos semanas se encuentran en etapa de reporte, por ende son provisorios y se espera que sean actualizados junto con cada publicación.

**Nota aclaratoria 2**:  Esta curva incluye casos activos no-notificados, probables y confirmados. En el caso de lo reportado diaramente por Minsal, incluye solo estos últimos.

---
---
<br><br><br>

# DP47 - Casos totales por región: Descripción
Este producto da cuenta de la media movil semanal de casos nuevos confirmados por region, normalizado por cada 100,000 habitantes.
# Columnas y valores
El archivo MediaMovil.csv contiene una columna 'Region', seguida por columnas correspondientes a ['fecha']. 
Estas últimas columnas contienen el promedio de casos nuevos en los últimos 7 días, normalizados por cada 100.000 habitantes de cada territorio.

# Fuente
Ministerio de Salud. Ver en:
https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/

# Frecuencia de actualización
Actualización diaria. 

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo no contempla los casos con región o comuna desconocida, es decir, aquellos casos en que no se registró la región de vivienda habitual en la notificación o bien son casos con domicilio en el extranjero.

**Nota aclaratoria 2:**  Los reportes del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

**Nota aclaratoria 3:** Previo al 15 de abril de 2020 los reportes del Ministerio de Salud no entregaban datos de confirmados notificados en comunas con bajo número de casos, para proteger la identidad de las personas contagiadas. 
---
---
<br><br><br>

# DP48 - Encuesta Diaria Realidad Nacional Medicina Intensiva: Descripción
Archivo que da cuenta del número de camas ocupadas por servicio de salud a lo largo del país, considerando los tipos de 
camas, incluyendo: camas intensivas ocupadas, camas intensivas totales, camas intermedias ocupadas, camas intermedias 
totales, ventiladores mecanicos invasivos (VMI) en uso por pacientes Covid19 confirmados y Covid19 sospechosos, Vmi 
ocupados y Vmi totales. Estos valores son levantados y reportados de manera diaria por los miembros de la SOCHIMI y la 
Universidad Finis Terrae, por fecha y servicio de salud, y disponibilizados por el Laboratorio de Biología Computacional
 de la Fundación Ciencia & Vida.

El archivo 'SOCHIMI.csv' tiene las siguientes columnas:

* **Codigo region**: código regional
* **Region**: nombre de la región
* **Servicio salud**: Servicio de Salud
* **Serie**: nombre de la serie de datos
    * **Camas ocupadas intensivo**: número de camas UCI ocupadas
    * **Camas totales intensivo**: número de camas UCI totales
    * **Camas ocupadas intermedio**: número de camas UTI ocupadas
    * **Camas totales intermedio**: número de camas UTI totales
    * **VMI COVID19 confirmados**: número de pacientes conectados a ventilación con COVID19
    * **VMI COVID19 sospechosos**:  número de pacientes conectados a ventilación con sospecha de COVID19
    * **VMI ocupados**: número de ventiladores ocupados por todo tipo de pacientes
    * **VMI totales**: número de ventiladores totales
* **Fechas**: valor de la serie correpondiente para la fecha indicada en el título de la columna

# Fuente
* Ingreso y recopilación de datos: SOCHIMI
* Preprocesamiento y manejo de datos: Fundación Ciencia y Vida

# Frecuencia de actualización
Semanal

# Notas aclaratorias

---
---
<br><br><br>

# DP49 - Positividad diaria y media móvil de exámenes PCR informados por día: Descripción
Archivo que da cuenta del número total de exámenes PCR realizados a nivel nacional, el número de casos nuevos totales, el resultado del cociente entre casos nuevos totales y exámenes realizados y el promedio móvil de los últimos 7 días de esa cantidad. Este archivo concatena la historia de los exámenes PCR realizados en el último día (Data Product 17), los casos nuevos totales (Data Product 4 y 5) publicados en los reportes diarios del Ministerio de Salud del país.

# Columnas y valores

El archivo Positividad_Diaria_Media.csv, contiene la primera columna donde se especifican las categorías: 'pcr' para el número total de exámenes PCR realizados durante el último día, 'casos' para el número de casos nuevos totales, la 'positividad' representada por el cociente 'casos'/'pcr', y 'mediamovil_positividad' para el promedio móvil de la positividad en el lapso de 7 días. Además, contiene una serie de columnas con '[Fecha]', donde se dan las categorías mencionadas anteriormente para cada fecha.

# Fuente

Reportes diarios publicados períodicamente por el Ministerio de Salud. Ver en: https://www.gob.cl/coronavirus/cifrasoficiales/#reportes

# Frecuencia de actualización

Actualización diaria.

# Notas aclaratorias

**Nota aclaratoria 1:** Previo al 25 de marzo de 2020 los reportes diarios del Ministerio de Salud no entregaban datos de exámenes PCR realizados en el país.

---
---
<br><br><br>

# DP50 - Defunciones notificadas por el Departamento de Estadísticas e Información Sanitaria (DEIS) por comuna: Descripción
Datos que corresponden a los fallecidos en cada una de las comunas de Chile, según residencia y fecha. Estos datos provienen del Departamento de Estadísticas e Información Sanitaria (DEIS) del Ministerio de Salud del país. 

El DEIS hace mejoras al registro de defunciones a medida que analiza diversas fuentes de datos. Estas mejoras en la metodología de investigación estudian la causa de defunción indicada en el certificado médico y la presencia de resultados RT-PCR. En caso de ser la defunción por cuadro clínico compatible a COVID-19 y con exámen PCR positivo para ser incluido confirmado para COVID-19 como causa del deceso.

Se entiende por comuna de residencia la comuna que se declaró la vivienda del paciente. 

# Columnas y valores
El archivo 'DefuncionesDEISPorComuna.csv' contiene las columnas 'Región', ‘Código Región’, 'Comuna', ‘Código comuna’, 'Población', y una serie de columnas 'Fecha', ..., que corresponden a la fecha que el DEIS confirma el deceso. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Datos publicados periódicamente por el Departamento de Estadísticas e Información Sanitaria (DEIS),  Ministerio de Salud de Chile. Ver en:
https://deis.minsal.cl/

# Frecuencia de actualización

Semanal

# Notas aclaratorias

**Nota aclaratoria 1:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

---
---
<br><br><br>

# DP51 - Datos de movilidad, provistos por Instituto Sistemas Complejos de Ingeniería (ISCI) en conjunto con Entel y Entel Ocean

Datos que corresponden a la variación porcentual de la movilidad entre zonas censales a partir de datos de infraestructura de telecomunicaciones.

# Columnas y valores
El archivo 'ISCI_std.csv' contiene las columnas Region, Codigo region,Comuna, Codigo comuna, Cartodb id, Zona censal, Week, Dif salida, Dif entrada.
Las primeras siete columnas corresponden a identificadores geográficos. Week se refiere a la semana del año al que corresponde el dato. Dif salida: variación porcentual de las salidas de una zona censal a otras zonas censales, con respecto a la semana 10 (16 de marzo). Dif entrada: variación porcentual de las entradas a una zona censal desde otras zonas censales, con respecto a la semana 10 (16 de marzo).
Estos valores están separados entre sí por comas (csv).

# Fuente
Datos publicados periódicamente por el Instituto de Sistemas Complejos de Ingeniería (ISCI, www.isci.cl). Ver en: https://covidanalytics.isci.cl/movilidad/


# Frecuencia de actualización

A ser definida

# Notas aclaratorias
La información desplegada se obtiene usando datos estadísticos e información del uso de infraestructura de telecomunicaciones, entregados de manera anonimizada y agregada por Entel, agrupados a nivel de zona censal. El Instituto de Sistemas Complejos de Ingeniería (ISCI) y Entel han tomado todas las medidas necesarias para mantener y proteger la información utilizada dentro del marco legal vigente.

---
---
<br><br><br>

# DP52 - Datos de disponibilidad de camas UCI

Datos que corresponden al registro de disponibilidad de camas UCI

# Columnas y valores
El archivo 'Camas_UCI.csv' contiene las columnas Region, Serie, y [fechas].
Se entiende por:
Cama básica: destinada a pacientes que, estando en cualquiera de las etapas de una enfermedad (evaluación, diagnóstico, 
tratamiento y/o recuperación), requiera hacer uso de instalaciones hospitalarias con el fin de que le sean otorgados 
cuidados médicos y de enfermería básicos
Cama media: destinada a entregar cuidados a pacientes de mediana complejidad. Se asocian a una fase aguda de enfermedad 
paciente, que en general debiera compensarse en pocos días.
Camas de cuidados críticos (UTI, UCI): destinada a brindar cuidados de alta complejidad definida para la 
internación y atención de pacientes críticos, es decir, con una condición patológica que afecta uno o más sistemas, que 
pone en serio riesgo actual o potencial su vida y que presenta condiciones de reversibilidad. Para ellos se hace 
necesaria la aplicación de técnicas de monitorización, vigilancia, manejo y soporte vital avanzado hasta la 
compensación de sus signos vitales y hemodinámicos. El perfil de pacientes a ingresar es máximo o alto riesgo y 
dependencia total o parcial asociado al riesgo (CUDYR A1-A2-A3-B1-B2).

Estos valores están separados entre sí por comas (csv).

# Fuente
Unidad de Gestión de Camas Críticas, Subsecretaría de Redes Asistenciales, Ministerio de Salud


# Frecuencia de actualización
Semanal

# Notas aclaratorias

---
---
<br><br><br>

# DP53 - Series corregidas sobre el número de casos confirmados, provistos por el grupo ICOVID Chile. 
Este producto surge del trabajo colaborativo entre el Ministerio de Salud, el Ministerio de Ciencias, e investigadores del grupo ICOVID Chile (https://www.icovidchile.cl).

Durante una epidemia, contar con información oportuna sobre el número de casos nuevos es crucial. Sin embargo, la toma de conocimiento de su existencia por parte de la autoridad sanitaria generalmente está sujeta a demoras o rezagos debido al periodo de incubación de la enfermedad, el tiempo de consulta a un especialista, el tiempo al diagnóstico y el tiempo al reporte del diagnóstico, entre otros. Esto implica que el número de casos nuevos recientemente observados, corresponde a una fracción de los casos que han iniciado la infección, lo que resulta en una subestimación de la cantidad de casos activos y en sesgos importantes en la estimación de indicadores de interés, tales como el número de reproducción efectivo, basados en los datos disponibles.

El presente producto contiene información sobre el número de casos confirmados, según fecha de inicio de los síntomas (utilizado como un proxy de la fecha de infección), corregidos por la presencia de datos faltantes respecto de la fecha de inicio de los síntomas y por los tiempos de rezago de la información. En lugar de reportar la estimación sobre el número de casos ocurridos y de una medida de su incertidumbre, se entregan 200 series generadas a través de la técnica de imputación múltiple, en base a modelos estadísticos desarrollados por el grupo ICOVID Chile y aplicados a diferentes unidades territoriales, a partir de los datos del Ministerio de Salud de Chile. Los detalles técnicos sobre los modelos de corrección de datos y el proceso de imputación se pueden encontrar en sitio web de grupo ICOVID Chile (https://www.icovidchile.cl). 

# Columnas y valores
El archivo 'confirmados_nacionales.csv' contiene la columna 'fecha' que corresponde a la fecha de inicio de los síntomas, y una serie de columnas  'confirmados.1' , ... , 'conformados.200', que corresponden a las diferente series generadas a través de imputación múltiple conteniendo el número de casos confirmados en cada día a nivel nacional. Todos estos valores están separados entre sí por comas (csv).

El archivo 'confirmados_regionales.csv' contiene la columna 'Region', 'Codigo region' y 'fecha' que corresponden al nombre de la región, el número de la región y la fecha de inicio de los síntomas, respectivamente, y una serie de columnas  'confirmados.1' , ... , 'conformados.200', que corresponden a las diferente series generadas a través de imputación múltiple conteniendo el número de casos confirmados en cada día a nivel nacional. Todos estos valores están separados entre sí por comas (csv).

El archivo 'confirmados_provinciales.csv' contiene la columna 'Region', 'Codigo region', 'Provincia', 'Codigo provincia' y 'fecha' que corresponden al nombre de la región, el número de la región, el nombre de la provincia, el número de la provincia y la fecha de inicio de los síntomas, respectivamente, y una serie de columnas  'confirmados.1' , ... , 'conformados.200', que corresponden a las diferente series generadas a través de imputación múltiple conteniendo el número de casos confirmados en cada día a nivel nacional. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Datos publicados periódicamente por el grupo ICOVID Chile (https://www.icovidchile.cl). 

# Frecuencia de actualización
Asociado a los informes epidemiológicos publicados por el Ministerio de Salud de Chile.

# Notas aclaratorias
ICOVID Chiles es grupo interdisciplinario convocado inicialmente por los Prorrectores de la Pontificia Universidad Católica de Chile, la Universidad de Chile, y a que se suma posteriormente la Universidad de Concepción. El cálculo de estas series corregidas se enmarcan en un proyecto de colaboración entre el Ministerio de Salud de Chile, el Ministerio de Ciencia, Tecnología, Conocimiento e Innovación de Chile, la Pontificia Universidad Católica de Chile y la Universidad de Chile.
---
---
<br><br><br>

# DP54 - Número de reproducción efectivo, provisto por el grupo ICOVID Chile.

Este producto surge del trabajo colaborativo entre el Ministerio de Salud, el Ministerio de Ciencias, e investigadores del grupo ICOVID Chile (https://www.icovidchile.cl).

El presente producto contiene información sobre el número de reproducción efectivo, estimado en base a los casos confirmados según la fecha de inicio de los síntomas, utilizado como un proxy de la fecha de infección. El número de reproducción efectivo se estimó empleando el método propuesto por:

Cori, A., Ferguson, N.M., Fraser, C., Cauchemez, S. (2013). A new framework and software to estimate time-varying reproduction numbers during epidemics. American Journal of Epidemiology, 178: 1505 - 1512.

El método de Cori, así como los otros métodos de estimación del número de reproducción efectivo, asumen que la cantidad de casos que inician la infección son completamente observados. Sin embargo, la observación de casos nuevos generalmente está sujeta a demoras o rezagos debido al periodo de incubación de la enfermedad, el tiempo de consulta a un especialista, el tiempo al diagnóstico y el tiempo al reporte del diagnóstico, entre otros. En lugar de imputar la cantidad de casos esperada, lo que genera una sub-estimación de las incertidumbres de las estimaciones, se utilizó el método de imputación múltiple, en base a los datos descritos en el producto 53.  Los detalles técnicos sobre la implementación del método de estimación del número de reproducción efectivo se pueden encontrar en sitio web de grupo ICOVID Chile (https://www.icovidchile.cl).

# Columnas y valores
El archivo 'r.nacional.csv' contiene la columna 'fecha' , 'r.estimado', 'r.liminf' y 'r.lisup'  que corresponden a fecha, la estimación puntal del número de reproducción efectivo,
el límite inferior del intervalo de 95% de confianza y el límite superior del intervalo de 95% de confianza. Todos estos valores están separados entre sí por comas (csv).

El archivo 'r.regional.csv' contiene la columna  'Region', 'Codigo region', 'fecha' , 'r.estimado', 'r.liminf' y 'r.lisup'  que corresponden al nombre de la región, el código de la región, la fecha, la estimación puntal del número de reproducción efectivo,  el límite inferior del intervalo de 95% de confianza y el límite superior del intervalo de 95% de confianza. Todos estos valores están separados entre sí por comas (csv).

El archivo 'r.provincial.csv' contiene la columna   'Region', 'Codigo region', 'Provincia', 'Codigo provincia', 'fecha' , 'r.estimado', 'r.liminf' y 'r.lisup'  que corresponden al nombre de la región, el código de la región, el nombre de la provincia, el número de la provincia, la fecha, la estimación puntal del número de reproducción efectivo,  el límite inferior del intervalo de 95% de confianza y el límite superior del intervalo de 95% de confianza. Todos estos valores están separados entre sí por comas (csv).
---
---
<br><br><br>

# DP - Positividad de examenes PCR según fecha del examen, provistos por ICOVID Chile. 

Este producto surge del trabajo colaborativo entre el Ministerio de Salud, el Ministerio de Ciencias, e investigadores del grupo ICOVID Chile (https://www.icovidchile.cl). El producto contiene información sobre la media movil de los último 7 días de la positividad de los examenes de PCR a SARS-CoV-2, definida como la proporción de los test que resultan positivos, sobre el total de test efectuados ese día (test positivos / test totales).  

# Columnas y valores
El archivo 'Positividad nacional.csv' contiene la columna 'fecha' que corresponde a la fecha de toma del examen y la columna 'positividad' que indica la media movil de los último 7 días de la proporción de examenes positivos. Todos estos valores están separados entre sí por comas (csv).

El archivo 'Positividad por región.csv' contiene la columna 'codigo_region' indicando el código de la región de residencia, 'region_residencia' indicando el nombre de la región de residencia, 'fecha' indicando la fecha de toma del examen, y 'positividad'  que indica la media movil de los último 7 días de la proporción de examenes positivos. Todos estos valores están separados entre sí por comas (csv).

El archivo 'Positividad por provincia.csv' contiene la columna 'codigo_provincia' indicando el código de la provincia de residencia, 'provincia_residencia' indicando el nombre de la provincia de residencia, 'fecha' indicando la fecha de toma del examen, y 'positividad' que indica la media movil de los último 7 días de la proporción de examenes positivos. Todos estos valores están separados entre sí por comas (csv).

El archivo 'Positividad por comuna.csv' contiene la columna 'codigo_comuna' indicando el código de la comuna de residencia, 'comuna_residencia' indicando el nombre de la comuna de residencia, 'fecha' indicando la fecha de toma del examen, y 'positividad' que indica la media movil de los último 7 días de la proporción de examenes positivos. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Datos publicados periódicamente por el grupo ICOVID Chile (https://www.icovidchile.cl). 

# Frecuencia de actualización
Asociado a los informes epidemiológicos publicados por el Ministerio de Salud de Chile.

# Notas aclaratorias
(1) La informacion sobre la comuna de residencia tiene una mayor frecuencia de datos faltantes. Por esta razón, 
las series de datos de mayor nivel de agregacion no necesariamente pueden obtenerse de la simple agregación de áreas geográficas menores. Para aquellas personas sin informacion de residencia, pero para quienes existía informacion sobre el lugar de toma de muestra, este último fue utilizado para asignar el test a una determinada área geográfica

(2) ICOVID Chiles es grupo interdisciplinario convocado inicialmente por los Prorrectores de la Pontificia Universidad Católica de Chile, la Universidad de Chile, y a que se suma posteriormente la Universidad de Concepción. El cálculo de estas series corregidas se enmarcan en un proyecto de colaboración entre el Ministerio de Salud de Chile, el Ministerio de Ciencia, Tecnología, Conocimiento e Innovación de Chile, la Pontificia Universidad Católica de Chile y la Universidad de Chile.

---
---
<br><br><br>

# DP - Proporción de casos confirmados tempranos, provistos por ICOVID Chile. 

Este producto surge del trabajo colaborativo entre el Ministerio de Salud, el Ministerio de Ciencias, e investigadores del grupo ICOVID Chile (https://www.icovidchile.cl). El producto contiene información sobre la proporción de casos confirmados para los cuales el tiempo transcurrido entre la fecha de inicio de los síntomas y la fecha en que el resultado del test de PCR a SARS-CoV-2 es recibido por la autoridad sanitaria es menor o igual a 48 horas (casos confirmados tempranos).  

# Columnas y valores
El archivo 'prob48.nacional.csv' contiene la columna 'fecha' que corresponde a la fecha del último día de la semana, la columna 'prob48.estimado' que contiene la estimación de la proporción de casos confirmados tempranos a nivel nacional la semana correspondiente, y las columnas 'prob48.linf' y 'prob48.lsup' que contienen los límites del intervalo de 95% de credibilidad para la proporción de casos confirmados tempranos a nivel nacional para la semana correspondiente. Todos estos valores están separados entre sí por comas (csv).

El archivo 'prob48.regional.csv' contiene la columna 'fecha' que corresponde a la fecha del último día de la semana, 'region' indicando el código de la región, la columna 'prob48.estimado' que contiene la estimación de la  proporción de casos confirmados tempranos en cada región la semana correspondiente, y las columnas 'prob48.linf' y 'prob48.lsup' que contienen los límites del intervalo de 95% de credibilidad para la proporción de casos confirmados tempranos en cada región para la semana correspondiente. Todos estos valores están separados entre sí por comas (csv).

El archivo 'prob48.provincial.csv' contiene la columna 'fecha' que corresponde a la fecha del último día de la semana, 'region' indicando el código de la región,
'provincia' indicando el código de la provincia, la columna 'prob48.estimado' que contiene la estimación de la proporción de casos confirmados tempranos en cada provincia la semana correspondient, y las columnas 'prob48.linf' y 'prob48.lsup' que contienen los límites del intervalo de 95% de credibilidad para la proporción de casos confirmados tempranos en cada provincia para la semana correspondiente. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Datos publicados periódicamente por el grupo ICOVID Chile (https://www.icovidchile.cl). 

# Frecuencia de actualización
Asociado a los informes epidemiológicos publicados por el Ministerio de Salud de Chile.

# Notas aclaratorias
(1) Estos resultados son estimados como parte de un modelo de estimación de casos presentes, cuyos resultados están disponibles en el Data Product 53, y corresponden a una característica de la distribución del rezago para cada semana epidemiológica.

(2) ICOVID Chiles es un grupo interdisciplinario convocado inicialmente por los Prorrectores de la Pontificia Universidad Católica de Chile, la Universidad de Chile, y al que se suma posteriormente la Universidad de Concepción. El cálculo de estas series corregidas se enmarcan en un proyecto de colaboración entre el Ministerio de Salud de Chile, el Ministerio de Ciencia, Tecnología, Conocimiento e Innovación de Chile, la Pontificia Universidad Católica de Chile y la Universidad de Chile.

---
---
<br><br><br>

Data Product 57 - Casos Fallecidos y estado de Hospitalización
---------------------------------------------------------------

Descripcion general
-------------------
Archivo que da cuenta de los casos fallecidos confirmados y probables por COVID-19 notificados en la plataforma EPIVIGILA o informados por los laboratorios al Ministero de Salud y que se encuentran dentro del conteo oficial de casos, por fecha de defunción, región de ocurrencia, y si el caso se hospitalizó o no. 

Caso fallecido: personas que fallecieron en territorio nacional debido a COVID-19. Considera muertes debido a Covid-19 con y sin confirmación de laboratorio (Códigos CIE-10 U07.1 y U07.2, respectivamente) informadas por el Departamento de Estadísticas e Información en Salud (DEIS) del MINSAL.

Región de ocurrencia: corresponde a la región donde el caso fue atendido y notificado.

Fecha de defunción: día, mes y año en que el médico registra en el Certificado Médico de Defunción la fecha de fallecimiento del caso.


Fuente
------
Informes epidemiológicos publicados periódicamente por el Ministerio de Salud de Chile. Ver en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/

A su vez, el Ministerio de Salud utiliza como fuente para la elaboración de estos informes el Sistema de notificación EPIVIGILA, del Departamento de Epidemiología, DIPLAS, y los informes de defunciones del Departamento de Estadísticas e Información en Salud, DIPLAS.


Frecuencia de actualizacion
---------------------------
Bisemanal


Columnas y valores
------------------
El archivo fallecidos_regionales_t.csv contiene las columnas 'Fecha', 'Región', 'Hospitalizacion' y 'Total'. 
'Fecha' se refiere a la fecha de defuncion de un caso. 
'Región' indica la región de ocurrencia de un caso.
'Hospitalizacion' toma valor FALSO cuando ese caso no registra información sobre hospitalización, y VERDADERO cuando si lo registra.
'Total' indica el número de casos fallecidos en esa fecha y región.


Notas aclaratorias
------------------
Nota aclaratoria 1: La información es validada y rectificada sistemáticamente por lo que es de carácter provisoria. 

Nota aclaratoria 2: La sistematización y codificación de las defunciones es realizada por el Departamento de Estadísticas e Información en Salud (DEIS) del Ministerio de Salud.

Nota aclaratoria 3: El número total de fallecidos que se muestra en este archivo solo contempla casos que cumplen las definiciones de vigilancia epidemiológica para casos CONFIRMADOS o PROBABLES segun Ordinario B51-2137 del 11 de junio del 2020, lo que explica el menor número observado respecto a lo informado como casos fallecidos totales en otros informes.  






---
---
<br><br><br>

Data Product 58 - Disponibilidad de camas críticas a nivel regional desagregado por día
---------------

# Descripción
Se presenta la cantidad de camas de Unidad de Cuidados Intensivos (UCI) para Adultos habilitadas por región, la ocupación total y la ocupación por COVID-19, así como la cantidad de camas disponibles.

Camas de cuidados críticos (UTI, UCI): destinada a brindar cuidados de alta complejidad definida para la internación y atención de pacientes críticos, es decir, con una condición patológica que afecta uno o más sistemas, que pone en serio riesgo actual o potencial su vida y que presenta condiciones de reversibilidad. Para ellos se hace necesaria la aplicación de técnicas de monitorización, vigilancia, manejo y soporte vital avanzado hasta la compensación de sus signos vitales y hemodinámicos. El perfil de pacientes a ingresar es máximo o alto riesgo y dependencia total o parcial asociado al riesgo (CUDYR A1-A2-A3-B1-B2). 


# Columnas y valores
El archivo 'Camas_UCI.csv' contiene las columnas Region, Serie, y [fechas].
Se entiende por:
Cama básica: destinada a pacientes que, estando en cualquiera de las etapas de una enfermedad (evaluación, diagnóstico, 
tratamiento y/o recuperación), requiera hacer uso de instalaciones hospitalarias con el fin de que le sean otorgados 
cuidados médicos y de enfermería básicos
Cama media: destinada a entregar cuidados a pacientes de mediana complejidad. Se asocian a una fase aguda de enfermedad 
paciente, que en general debiera compensarse en pocos días.
Camas de cuidados críticos (UTI, UCI): destinada a brindar cuidados de alta complejidad definida para la 
internación y atención de pacientes críticos, es decir, con una condición patológica que afecta uno o más sistemas, que 
pone en serio riesgo actual o potencial su vida y que presenta condiciones de reversibilidad. Para ellos se hace 
necesaria la aplicación de técnicas de monitorización, vigilancia, manejo y soporte vital avanzado hasta la 
compensación de sus signos vitales y hemodinámicos. El perfil de pacientes a ingresar es máximo o alto riesgo y 
dependencia total o parcial asociado al riesgo (CUDYR A1-A2-A3-B1-B2).

Estos valores están separados entre sí por comas (csv).

# Fuente
Ministerio de Salud de Chile, Subsecretaría de Redes Asistenciales, Unidad de Gestión de Camas Críticas

# Frecuencia de actualización

Semanal

# Notas aclaratorias


---
---
<br><br><br>

PRODUCTO 59 - Curva de casos por etapa clínica (confirmados, probables y no-notificados), por fecha de notificación, desagregados por día

Descripcion general
-------------------
Archivo que entrega la serie de casos confirmados por PCR(+) notificados o no en la plataforma EPIVIGILA junto a los casos probables, según fecha de notificación.


Fuente
------
Reportes de laboratorios acreditados por el Instituto de Salud Pública para el desarrollo de la técnica de PCR para detección de SARS-CoV-2 debidamente informados al Ministerio de Salud.
Plataforma de vigilancia epidemiológica EPIVIGILA del Depto. de Epidemiología, Ministerio de Salud.


Frecuencia de actualizacion
---------------------------
Bisemanal


Columnas y valores
------------------
El archivo etapa_clinica_por_fecha_notificacion.csv contiene las columnas 'fecha_notificacion' y 'etapa_clinica'.
- 'fecha_notificacion' se refiere a la fecha en la cual los casos confirmados por PCR(+) o los casos probables fueron notificados por el médico tratante en la plataforma EPIVIGILA. 
- 'etapa_clinica' toma valor 'confirmado' cuando el/los caso/s presentan una PCR(+) y estan debidamente notificados en la plataforma EPIVIGILA; 'no notificada' cuando el/los caso/s presentan una PCR(+) y NO estan debidamente notificados en la plataforma EPIVIGILA; y 'probable' cuando el/los caso/s estan debidamente notificados en la plataforma EPIVIGILA bajo esa etapa.


Notas aclaratorias
------------------
Nota aclaratoria 1: La información es validada y rectificada sistemáticamente por lo que es de carácter provisoria y puede cambiar entre un informe y otro. 

---
---
<br><br><br>

PRODUCTO 60 - Curva de casos por etapa clínica (confirmados, probables y no-notificados), por fecha de inicio de síntomas, desagregados por día

Descripcion general
-------------------
Archivo que entrega la serie de casos confirmados por PCR(+) notificados o no en la plataforma EPIVIGILA junto a los casos probables, según fecha de inicio de síntomas (para casos sintomáticos) o fecha de notificación (para casos asintomáticos).


Fuente
------
Reportes de laboratorios acreditados por el Instituto de Salud Pública para el desarrollo de la técnica de PCR para detección de SARS-CoV-2 debidamente informados al Ministerio de Salud.
Plataforma de vigilancia epidemiológica EPIVIGILA del Depto. de Epidemiología, Ministerio de Salud.


Frecuencia de actualizacion
---------------------------
Bisemanal


Columnas y valores
------------------
El archivo etapa_clinica_por_fis.csv contiene las columnas 'fecha_primeros_sintomas' y 'etapa_clinica'.
- 'fecha_primeros_sintomas' se refiere a la fecha en la cual los casos confirmados por PCR(+) o los casos probables registraron haber iniciado síntomas (casos sintomáticos) o bien cuando el médico los notificó (casos asintomáticos). 
- 'etapa_clinica' toma valor 'confirmado' cuando el/los caso/s presentan una PCR(+) y estan debidamente notificados en la plataforma EPIVIGILA; 'no notificada' cuando el/los caso/s presentan una PCR(+) y NO estan debidamente notificados en la plataforma EPIVIGILA; y 'probable' cuando el/los caso/s estan debidamente notificados en la plataforma EPIVIGILA bajo esa etapa.


Notas aclaratorias
------------------
Nota aclaratoria 1: La información es validada y rectificada sistemáticamente por lo que es de carácter provisoria y puede cambiar entre un informe y otro. 
---
---
<br><br><br>

PRODUCTO 61 - PRODUCTO 61 - Fallecidos acumulados confirmados (U07.1) y probables (U07.2) por comuna


Descripcion general
-------------------
Archivo que da cuenta de los casos fallecidos acumulados confirmados y probables por COVID-19 informados por el Departamento de Estadísticas e Información en Salud (DEIS) del Ministerio de Salud.  

Caso fallecido: personas que fallecieron en territorio nacional debido a COVID-19. Considera muertes debido a Covid-19 con y sin confirmación de laboratorio (Códigos CIE-10 U07.1 y U07.2, respectivamente) informadas por el Departamento de Estadísticas e Información en Salud (DEIS) del MINSAL.

Región de ocurrencia: corresponde a la región donde el caso fue atendido y notificado.

Fecha de defunción: día, mes y año en que el médico registra en el Certificado Médico de Defunción la fecha de fallecimiento del caso.


Fuente
------
Departamento de Estadísticas e Información en Salud, DIPLAS, Ministero de Salud.


Frecuencia de actualizacion
---------------------------
Bisemanal


Columnas y valores
------------------
El archivo serie_fallecidos_comuna.csv contiene las columnas 'Comuna', 'CIE 10' y 'Region'. 
- 'Comuna' corresponde a la comuna de residencia del caso. 
- 'CIE 10' toma valor 'U07.1' cuando el caso registró una PCR(+), y 'U07.2' cuando no lo registró, según la codificación realizada por el DEIS en base a los Certificados Médicos de Defunción y Registros de Laboratorio.
- 'Region' corresponde a la región de residencia del caso.


Notas aclaratorias
------------------
Nota aclaratoria 1: La información es validada y rectificada sistemáticamente por lo que es de carácter provisoria. 

Nota aclaratoria 2: La sistematización y codificación de las defunciones es realizada por el Departamento de Estadísticas e Información en Salud (DEIS) del Ministerio de Salud.

---
---
<br><br><br>

PRODUCTO 62 - Casos nuevos y acumulados a la fecha

Descripcion general
-------------------
Archivo que da cuenta de los casos nuevos diarios confirmados por PCR(+) notificados o no en la plataforma EPIVIGILA e informados por los laboratorios acreditados al Ministero de Salud. Estos casos constituyen las cifras oficiales comunicadas por las autoridades diariamente. Los casos acumulados contituyen la suma de todos los casos confirmados a la fecha (notificados o no) junto a los casos probables. 


Fuente
------
Reportes de laboratorios acreditados por el Instituto de Salud Pública para el desarrollo de la técnica de PCR para detección de SARS-CoV-2 debidamente informados al Ministerio de Salud.


Frecuencia de actualizacion
---------------------------
Bisemanal


Columnas y valores
------------------
El archivo casos_nuevos_acumulados_por_fecha.csv contiene las columnas 'Fecha', 'Casos'.
- 'Fecha' se refiere a la fecha en la cual se informó un determinado número de casos nuevos. 
- 'Casos' toma valor 'Casos nuevos' cuando la cifra equivale al número de casos nuevos informados para la respectiva fecha, y 'Casos acumulados' al total de casos confirmados + casos probables hasta la respectiva fecha.


Notas aclaratorias
------------------
Nota aclaratoria 1: La información es validada y rectificada sistemáticamente por lo que es de carácter provisoria. 

Nota aclaratoria 2: Pueden existir variaciones en el conteo de casos durante el período analizado, lo que se explica por los cambios definidos por las autoridades en los criterios para el conteo diario de casos.




---
---
<br><br><br>

# DP63 - Número de personas notificadas con exámenes por Comuna: Descripción
Archivo que da cuenta del número de personas notificadas con exámenes RT-PCR positivos.
Estos valores son levantados y reportados de manera semanal por el Laboratorio de Biología Computacional de la Fundación Ciencia & Vida 
acorde al informe de Indicadores de Testeo y Trazabilidad publicado semanalmente por el departamento de Epidemiología.

# Columnas y valores

El archivo 'NNotificacionPorComuna.csv' tiene las columnas 'Región', 'Código región', 'Comuna', 'Código comuna', 'Población', y una serie de columnas '[Fecha]', donde en cada una están el 'Numero notificaciones' reportados en cada publicación de Epidemiología, por cada comuna, en cada fecha reportada. El archivo NNotificacionPorComuna_T.csv es la versión traspuesta (serie de tiempo) del primer archivo y NNotificacionPorComuna_std.csv contiene la información en formato estándar. Todos estos valores están separados entre sí por comas (csv).

# Fuente
* Informe de Indicadores de Testeo y Trazabilidad, departamento de Epidemiología, Ministerio de Salud
* Preprocesamiento y manejo de datos: Fundación Ciencia y Vida

# Frecuencia de actualización
Semanal

# Notas aclaratorias

**Nota aclaratoria 1:** Los informes emanados del departamento de epidemiología del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 6 hrs.

**Nota aclaratoria 2:** Los informes de Indicadores de Testeo y Trazabilidad se han publicado a partir del 24 de Agosto 2020.

**Nota aclaratoria 3:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

**Nota aclaratoria 4:** En consideración del Ord. 105/N°3857 que "informa actualización sobre acciones de seguimiento y APS en marco de la estrategia TTA", los indicadores de trazabilidad (correspondientes a los indicadores 5, 6, 7 y Razón de contactos) se presentan basados según región de asignación FONASA. Lo anterior significa que el total regional publicado podría presentar diferencias respecto al detalle a nivel comunal, debido a que el primero es presentado por región de asignación y segundo por comuna de residencia, los cuales no necesariamente coincidirán, y por tanto, no son comparables.

**Nota aclaratoria 5:** Desde el informe publicado el 2 de febrero de 2022, el periodo de análisis de todos los indicadores TTA se basa en semanas epidemiológicas (SE), es decir, abarca de domingo a sábado de la semana previa a la publicación.

Basado en las nuevas definiciones de caso, señaladas en el Ord B51/N°269 del 19 de enero de 2022, los indicadores de trazabilidad, correspondientes a “Oportunidad de la investigación epidemiológica y registro del primer seguimiento de casos”, “Identificación de contactos”, “Oportunidad de la investigación epidemiológica y registro del primer seguimiento de en contactos” e “Indicador global de la estrategia testeo y trazabilidad” fueron adaptados. La descripción de cada uno de ellos se encuentra en el apartado metodológico del informe, disponible en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/, y están abordados dentro de los siguientes ámbitos según las gestiones realizadas en el contexto de la estrategia de trazabilidad, siendo éstas:

- Primer contacto de casos nuevos.
- Estudio de contactos estrechos en contexto de brotes investigados
- Manejo de contactos estrechos y testeo en contexto de brotes
- Investigación de nexo epidemiológico, respectivamente.

Debido a lo anteriormente señalado, el indicador “Relación de contactos por caso” fue suprimido.
---
---
<br><br><br>

# DP64 - Cantidad de Test por búsqueda activa de casos (BAC) por Comuna: Descripción
Archivo que da cuenta de la proporción de test realizados por búsqueda activa de casos sobre el total de los test realizados en las personas notificadas con resultados de laboratorio.
Estos valores son levantados y reportados de manera semanal por el Laboratorio de Biología Computacional de la Fundación Ciencia & Vida 
acorde al informe de Indicadores de Testeo y Trazabilidad publicado semanalmente por el departamento de Epidemiología.

# Columnas y valores

El archivo 'BACPorComuna.csv' tiene las columnas 'Región', 'Código región', 'Comuna', 'Código comuna', 'Población', y una serie de columnas '[Fecha]', donde en cada una están la proporción de test por 'BAC' reportados en cada publicación de Epidemiología, por cada comuna, en cada fecha reportada. El archivo BACPorComuna_T.csv es la versión traspuesta (serie de tiempo) del primer archivo y BACPorComuna_std.csv contiene la información en formato estándar. Todos estos valores están separados entre sí por comas (csv).

# Fuente
* Informe de Indicadores de Testeo y Trazabilidad, departamento de Epidemiología, Ministerio de Salud
* Preprocesamiento y manejo de datos: Fundación Ciencia y Vida

# Frecuencia de actualización
Semanal

# Notas aclaratorias

**Nota aclaratoria 1:** Los informes emanados del departamento de epidemiología del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 6 hrs.

**Nota aclaratoria 2:** Los informes de Indicadores de Testeo y Trazabilidad se han publicado a partir del 24 de Agosto 2020.

**Nota aclaratoria 3:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

**Nota aclaratoria 4:** En consideración del Ord. 105/N°3857 que "informa actualización sobre acciones de seguimiento y APS en marco de la estrategia TTA", los indicadores de trazabilidad (correspondientes a los indicadores 5, 6, 7 y Razón de contactos) se presentan basados según región de asignación FONASA. Lo anterior significa que el total regional publicado podría presentar diferencias respecto al detalle a nivel comunal, debido a que el primero es presentado por región de asignación y segundo por comuna de residencia, los cuales no necesariamente coincidirán, y por tanto, no son comparables.

**Nota aclaratoria 5:** Desde el informe publicado el 2 de febrero de 2022, el periodo de análisis de todos los indicadores TTA se basa en semanas epidemiológicas (SE), es decir, abarca de domingo a sábado de la semana previa a la publicación.

Basado en las nuevas definiciones de caso, señaladas en el Ord B51/N°269 del 19 de enero de 2022, los indicadores de trazabilidad, correspondientes a “Oportunidad de la investigación epidemiológica y registro del primer seguimiento de casos”, “Identificación de contactos”, “Oportunidad de la investigación epidemiológica y registro del primer seguimiento de en contactos” e “Indicador global de la estrategia testeo y trazabilidad” fueron adaptados. La descripción de cada uno de ellos se encuentra en el apartado metodológico del informe, disponible en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/, y están abordados dentro de los siguientes ámbitos según las gestiones realizadas en el contexto de la estrategia de trazabilidad, siendo éstas:

- Primer contacto de casos nuevos.
- Estudio de contactos estrechos en contexto de brotes investigados
- Manejo de contactos estrechos y testeo en contexto de brotes
- Investigación de nexo epidemiológico, respectivamente.

Debido a lo anteriormente señalado, el indicador “Relación de contactos por caso” fue suprimido.
---
---
<br><br><br>

# DP65 - Indice de Positividad Test RT-PCR por Comuna: Descripción
Archivo que da cuenta de la proporción de resultados de test positivos en las personas notificadas con resultados de laboratorio.
Estos valores son levantados y reportados de manera semanal por el Laboratorio de Biología Computacional de la Fundación Ciencia & Vida 
acorde al informe de Indicadores de Testeo y Trazabilidad publicado semanalmente por el departamento de Epidemiología.

# Columnas y valores

El archivo 'PositividadPorComuna.csv' tiene las columnas 'Región', 'Código región', 'Comuna', 'Código comuna', 'Población', y una serie de columnas '[Fecha]', donde en cada una están la proporción de test positivos ('Positividad') reportados en cada publicación de Epidemiología, por cada comuna, en cada fecha reportada. El archivo PositividadPorComuna_T.csv es la versión traspuesta (serie de tiempo) del primer archivo y PositividadPorComuna_std.csv contiene la información en formato estándar. Todos estos valores están separados entre sí por comas (csv).

# Fuente
* Informe de Indicadores de Testeo y Trazabilidad, departamento de Epidemiología, Ministerio de Salud
* Preprocesamiento y manejo de datos: Fundación Ciencia y Vida

# Frecuencia de actualización
Semanal

# Notas aclaratorias

**Nota aclaratoria 1:** Los informes emanados del departamento de epidemiología del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 6 hrs.

**Nota aclaratoria 2:** Los informes de Indicadores de Testeo y Trazabilidad se han publicado a partir del 24 de Agosto 2020.

**Nota aclaratoria 3:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

**Nota aclaratoria 4:** En consideración del Ord. 105/N°3857 que "informa actualización sobre acciones de seguimiento y APS en marco de la estrategia TTA", los indicadores de trazabilidad (correspondientes a los indicadores 5, 6, 7 y Razón de contactos) se presentan basados según región de asignación FONASA. Lo anterior significa que el total regional publicado podría presentar diferencias respecto al detalle a nivel comunal, debido a que el primero es presentado por región de asignación y segundo por comuna de residencia, los cuales no necesariamente coincidirán, y por tanto, no son comparables.

**Nota aclaratoria 5:** Desde el informe publicado el 2 de febrero de 2022, el periodo de análisis de todos los indicadores TTA se basa en semanas epidemiológicas (SE), es decir, abarca de domingo a sábado de la semana previa a la publicación.

Basado en las nuevas definiciones de caso, señaladas en el Ord B51/N°269 del 19 de enero de 2022, los indicadores de trazabilidad, correspondientes a “Oportunidad de la investigación epidemiológica y registro del primer seguimiento de casos”, “Identificación de contactos”, “Oportunidad de la investigación epidemiológica y registro del primer seguimiento de en contactos” e “Indicador global de la estrategia testeo y trazabilidad” fueron adaptados. La descripción de cada uno de ellos se encuentra en el apartado metodológico del informe, disponible en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/, y están abordados dentro de los siguientes ámbitos según las gestiones realizadas en el contexto de la estrategia de trazabilidad, siendo éstas:

- Primer contacto de casos nuevos.
- Estudio de contactos estrechos en contexto de brotes investigados
- Manejo de contactos estrechos y testeo en contexto de brotes
- Investigación de nexo epidemiológico, respectivamente.

Debido a lo anteriormente señalado, el indicador “Relación de contactos por caso” fue suprimido.
---
---
<br><br><br>

# DP66 - Cobertura de testeo por Comuna: Descripción
Archivo que da cuenta de la proporción de casos nuevos notificados (sospechosos) con al menos un resultado de examen de RT-PCR.
Estos valores son levantados y reportados de manera semanal por el Laboratorio de Biología Computacional de la Fundación Ciencia & Vida 
acorde al informe de Indicadores de Testeo y Trazabilidad publicado semanalmente por el departamento de Epidemiología.

# Columnas y valores

El archivo 'CoberturaPorComuna.csv' tiene las columnas 'Región', 'Código región', 'Comuna', 'Código comuna', 'Población', y una serie de columnas '[Fecha]', donde en cada una están la proporción de casos nuevos notificados (sospechosos) 'Cobertura' reportados en cada publicación de Epidemiología, por cada comuna, en cada fecha reportada. El archivo CoberturaPorComuna_T.csv es la versión traspuesta (serie de tiempo) del primer archivo y CoberturaPorComuna_std.csv contiene la información en formato estándar. Todos estos valores están separados entre sí por comas (csv).

# Fuente
* Informe de Indicadores de Testeo y Trazabilidad, departamento de Epidemiología, Ministerio de Salud
* Preprocesamiento y manejo de datos: Fundación Ciencia y Vida

# Frecuencia de actualización
Semanal

# Notas aclaratorias

**Nota aclaratoria 1:** Los informes emanados del departamento de epidemiología del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 6 hrs.

**Nota aclaratoria 2:** Los informes de Indicadores de Testeo y Trazabilidad se han publicado a partir del 24 de Agosto 2020.

**Nota aclaratoria 3:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

**Nota aclaratoria 4:** En consideración del Ord. 105/N°3857 que "informa actualización sobre acciones de seguimiento y APS en marco de la estrategia TTA", los indicadores de trazabilidad (correspondientes a los indicadores 5, 6, 7 y Razón de contactos) se presentan basados según región de asignación FONASA. Lo anterior significa que el total regional publicado podría presentar diferencias respecto al detalle a nivel comunal, debido a que el primero es presentado por región de asignación y segundo por comuna de residencia, los cuales no necesariamente coincidirán, y por tanto, no son comparables.

**Nota aclaratoria 5:** Desde el informe publicado el 2 de febrero de 2022, el periodo de análisis de todos los indicadores TTA se basa en semanas epidemiológicas (SE), es decir, abarca de domingo a sábado de la semana previa a la publicación.

Basado en las nuevas definiciones de caso, señaladas en el Ord B51/N°269 del 19 de enero de 2022, los indicadores de trazabilidad, correspondientes a “Oportunidad de la investigación epidemiológica y registro del primer seguimiento de casos”, “Identificación de contactos”, “Oportunidad de la investigación epidemiológica y registro del primer seguimiento de en contactos” e “Indicador global de la estrategia testeo y trazabilidad” fueron adaptados. La descripción de cada uno de ellos se encuentra en el apartado metodológico del informe, disponible en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/, y están abordados dentro de los siguientes ámbitos según las gestiones realizadas en el contexto de la estrategia de trazabilidad, siendo éstas:

- Primer contacto de casos nuevos.
- Estudio de contactos estrechos en contexto de brotes investigados
- Manejo de contactos estrechos y testeo en contexto de brotes
- Investigación de nexo epidemiológico, respectivamente.

Debido a lo anteriormente señalado, el indicador “Relación de contactos por caso” fue suprimido.
---
---
<br><br><br>

# DP67 - Oportunidad en la notificación de casos nuevos por Comuna: Descripción
Archivo que da cuenta de la proporción de casos nuevos confirmados por laboratorio, que fueron notificados en la primera consulta o contacto con salud, es decir, antes del proceso de la toma de muestra.
Estos valores son levantados y reportados de manera semanal por el Laboratorio de Biología Computacional de la Fundación Ciencia & Vida 
acorde al informe de Indicadores de Testeo y Trazabilidad publicado semanalmente por el departamento de Epidemiología.

# Columnas y valores

El archivo 'OportunidadPorComuna.csv' tiene las columnas 'Región', 'Código región', 'Comuna', 'Código comuna', 'Población', y una serie de columnas '[Fecha]', donde en cada una están la proporción de casos nuevos confirmados por laboratorio notificados en la primera consulta (antes del proceso de la toma de muestra) 'Oportunidad' reportados en cada publicación de Epidemiología, por cada comuna, en cada fecha reportada. El archivo OportunidadPorComuna_T.csv es la versión traspuesta (serie de tiempo) del primer archivo y OportunidadPorComuna_std.csv contiene la información en formato estándar. Todos estos valores están separados entre sí por comas (csv).

# Fuente
* Informe de Indicadores de Testeo y Trazabilidad, departamento de Epidemiología, Ministerio de Salud
* Preprocesamiento y manejo de datos: Fundación Ciencia y Vida

# Frecuencia de actualización
Semanal

# Notas aclaratorias

**Nota aclaratoria 1:** Los informes emanados del departamento de epidemiología del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 6 hrs.

**Nota aclaratoria 2:** Los informes de Indicadores de Testeo y Trazabilidad se han publicado a partir del 24 de Agosto 2020.

**Nota aclaratoria 3:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

**Nota aclaratoria 4:** En consideración del Ord. 105/N°3857 que "informa actualización sobre acciones de seguimiento y APS en marco de la estrategia TTA", los indicadores de trazabilidad (correspondientes a los indicadores 5, 6, 7 y Razón de contactos) se presentan basados según región de asignación FONASA. Lo anterior significa que el total regional publicado podría presentar diferencias respecto al detalle a nivel comunal, debido a que el primero es presentado por región de asignación y segundo por comuna de residencia, los cuales no necesariamente coincidirán, y por tanto, no son comparables.

**Nota aclaratoria 5:** Desde el informe publicado el 2 de febrero de 2022, el periodo de análisis de todos los indicadores TTA se basa en semanas epidemiológicas (SE), es decir, abarca de domingo a sábado de la semana previa a la publicación.

Basado en las nuevas definiciones de caso, señaladas en el Ord B51/N°269 del 19 de enero de 2022, los indicadores de trazabilidad, correspondientes a “Oportunidad de la investigación epidemiológica y registro del primer seguimiento de casos”, “Identificación de contactos”, “Oportunidad de la investigación epidemiológica y registro del primer seguimiento de en contactos” e “Indicador global de la estrategia testeo y trazabilidad” fueron adaptados. La descripción de cada uno de ellos se encuentra en el apartado metodológico del informe, disponible en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/, y están abordados dentro de los siguientes ámbitos según las gestiones realizadas en el contexto de la estrategia de trazabilidad, siendo éstas:

- Primer contacto de casos nuevos.
- Estudio de contactos estrechos en contexto de brotes investigados
- Manejo de contactos estrechos y testeo en contexto de brotes
- Investigación de nexo epidemiológico, respectivamente.

Debido a lo anteriormente señalado, el indicador “Relación de contactos por caso” fue suprimido.
---
---
<br><br><br>

# DP68 - Cantidad de exámenes de PCR  por cada 1000 habitantes por semana, según fecha del examen, provistos por ICOVID Chile. 

Este producto surge del trabajo colaborativo entre el Ministerio de Salud, el Ministerio de Ciencias, e investigadores del grupo ICOVID Chile (https://www.icovidchile.cl). El producto contiene información sobre la media móvil, de los últimos 7 días, de la cantidad de examenes de PCR a SARS-CoV-2 realizados por cada 1000 habitantes. 

# Columnas y valores
El archivo 'tasa test semanal nacional.csv' contiene la columna 'fecha' que corresponde a la fecha de toma del examen y la columna 'tasatest' que indica la media movil de los último 7 días de la e la cantidad de examenes de PCR a SARS-CoV-2 realizados por cada 1000 habitantes a nivel nacional. Todos estos valores están separados entre sí por comas (csv).

El archivo 'tasa test semanal regional.csv' contiene la columna 'codigo_region' indicando el código de la región de residencia, 'region_residencia' indicando el nombre de la región de residencia, 'fecha' indicando la fecha de toma del examen, y 'tasatest' que indica la media movil de los último 7 días de la e la cantidad de examenes de PCR a SARS-CoV-2 realizados por cada 1000 habitantes a nivel regional. Todos estos valores están separados entre sí por comas (csv).

El archivo 'tasa test semanal provincial.csv' contiene la columna 'codigo_provincia' indicando el código de la provincia de residencia, 'provincia_residencia' indicando el nombre de la provincia de residencia, 'fecha' indicando la fecha de toma del examen, y 'tasatest' que indica la media movil de los último 7 días de la e la cantidad de examenes de PCR a SARS-CoV-2 realizados por cada 1000 habitantes a nivel provincial. Todos estos valores están separados entre sí por comas (csv).

El archivo 'tasa test semanal regional.csv' contiene la columna 'codigo_comuna' indicando el código de la comuna de residencia, 'comuna_residencia' indicando el nombre de la comuna de residencia, 'fecha' indicando la fecha de toma del examen, y 'tasatest' que indica la media movil de los último 7 días de la e la cantidad de examenes de PCR a SARS-CoV-2 realizados por cada 1000 habitantes a nivel comunal. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Datos publicados periódicamente por el grupo ICOVID Chile (https://www.icovidchile.cl). 

# Frecuencia de actualización
Asociado a los informes epidemiológicos publicados por el Ministerio de Salud de Chile.

# Notas aclaratorias
(1) El número de test informados diariamente corresponde al área geográfica de residencia de la persona a la que se le solicita el examen.  

(2) La informaci on sobre la comuna de residencia tiene una mayor frecuencia de datos faltantes. Por esta razón, las series de datos de mayor nivel de agregaci on no necesariamente pueden obtenerse de la simple agregaci ón de  áreas geográficas menores. Para aquellas personas sin informaci on de residencia, pero para quienes exist  ía informaci on sobre el lugar de toma de muestra, este último fue utilizado para asignar el test a una determinada  área geográfica

(3) ICOVID Chiles es grupo interdisciplinario conformado por investigadores de la Pontificia Universidad Católica de Chile, la Universidad de Chile y la Universidad de Concepción.  El cálculo de estas series se enmarcan en un proyecto de colaboración entre el Ministerio de Salud de Chile, el Ministerio de Ciencia, Tecnología, Conocimiento e Innovación de Chile, la Pontificia Universidad Católica de Chile y la Universidad de Chile.
---
---
<br><br><br>

# DP69 - Tasa de incidencia, por cada 100 mil habitantes, de casos confirmados diarios, provistos por el grupo ICOVID Chile. 

Este producto surge del trabajo colaborativo entre el Ministerio de Salud, el Ministerio de Ciencias, e investigadores del grupo ICOVID Chile (https://www.icovidchile.cl). El producto contiene información sobre la tasa de incidencia diaria, por cada 100 mil habitantes, de casos confirmados según fecha de inicio de los síntomas. 

# Columnas y valores
El archivo 'carga.nacional.ajustada.csv' contiene la columna 'fecha' que corresponde a la fecha de inicio de los síntomas, y 'carga.estimada', 'carga.liminf' y 'carga.lisup'  que corresponden a fecha de inicio de los síntomas, la estimación puntal de la tasa de incidencia por cada 100 habitantes,  el límite inferior del intervalo de 95% de credibilidad y el límite superior del intervalo de 95% de credibilidad, respectivamente. Todos estos valores están separados entre sí por comas (csv).

El archivo 'carga.regional.ajustada.csv' contiene la columna  'region', 'fecha' , 'carga.estimada', 'carga.liminf' y 'carga.lisup'  que corresponden al código de la región, la fecha, la estimación puntal de la tasa de incidencia por cada 100 habitantes,  el límite inferior del intervalo de 95% de credibilidad y el límite superior del intervalo de 95% de credibilidad, respectivamente. Todos estos valores están separados entre sí por comas (csv).

El archivo 'carga.provincial.ajustada.csv' contiene la columna 'region', 'provincia', 'fecha' , 'carga.estimada', 'carga.liminf' y 'carga.lisup'  que corresponden al código de la región, el código de la provincia, la fecha de inicio de los síntomas, la estimación puntal de  la tasa de incidencia por cada 100 habitantes, el límite inferior del intervalo de 95% de credibilidad y el límite superior del intervalo de 95% de credibilidad, respectivamente. Todos estos valores están separados entre sí por comas (csv).

El archivo  'carga.ss.ajustada.csv'  contiene la columna  'region', 'servicio.salud', 'fecha' , 'carga.estimada', 'carga.liminf' y 'carga.lisup'  que corresponden al código de la región, el código del servicio de salud, la fecha de inicio de los síntomas, la estimación puntal de  la tasa de incidencia por cada 100 habitantes, el límite inferior del intervalo de 95% de credibilidad y el límite superior del intervalo de 95% de credibilidad, respectivamente. Todos estos valores están separados entre sí por comas (csv).


# Fuente
Datos publicados periódicamente por el grupo ICOVID Chile (https://www.icovidchile.cl). 

# Frecuencia de actualización
Asociado a los informes epidemiológicos publicados por el Ministerio de Salud de Chile.

# Notas aclaratorias
ICOVID Chiles es grupo interdisciplinario de la Pontificia Universidad Católica de Chile, la Universidad de Chile, y la Universidad de Concepción.  El cálculo de estas tasas se enmarcan en un proyecto de colaboración entre el Ministerio de Salud de Chile, el Ministerio de Ciencia, Tecnología, Conocimiento e Innovación de Chile, la Pontificia Universidad Católica de Chile y la Universidad de Chile.




---
---
<br><br><br>

# DP70 - Confirmación temprana de casos sintomáticos, provistos por el grupo ICOVID Chile. 

Este producto surge del trabajo colaborativo entre el Ministerio de Salud, el Ministerio de Ciencias, e investigadores del grupo ICOVID Chile (https://www.icovidchile.cl). El producto contiene información sobre la media móvil, de 7 días, de la proporción de personas sintomáticas sospechosas cuyo resultado de PCR positivo a SARS-CoV-2 es informado a la autoridad sanitaria dentro de 3 días desde la fecha de inicio de síntomas.
 

# Columnas y valores
El archivo 'total72.nacional.csv' contiene la columna 'fecha_primeros_sintomas' que corresponde a la fecha de inicio de los síntomas, y 'prop3d' que corresponde a  la media móvil, de 7 días, de la proporción de personas sintomáticas sospechosas cuyo resultado  de PCR positivo a SARS-CoV-2 es informado a la autoridad sanitaria dentro de 3 días desde la fecha de inicio de síntomas a nivel nacional. Todos estos valores están separados entre sí por comas (csv).

El archivo 'total72.regional.csv' contiene la columna 'fecha_primeros_sintomas' que corresponde a la fecha de inicio de los síntomas, 'region' que corresponde al código de la región, y 'prop3d' que corresponde a  la media móvil, de 7 días, de la proporción de personas sintomáticas sospechosas cuyo resultado  de PCR positivo a SARS-CoV-2 es informado a la autoridad sanitaria dentro de 3 días desde la fecha de inicio de síntomas a nivel regional. Todos estos valores están separados entre sí por comas (csv).

El archivo 'total72.provincial.csv' contiene la columna 'fecha_primeros_sintomas' que corresponde a la fecha de inicio de los síntomas, 'region' que corresponde al código de la región, 'provincia' que corresponde al código de la provincia, y 'prop3d' que corresponde a  la media móvil, de 7 días, de la proporción de personas sintomáticas sospechosas cuyo resultado  de PCR positivo a SARS-CoV-2 es informado a la autoridad sanitaria dentro de 3 días desde la fecha de inicio de síntomas a nivel provincial. Todos estos valores están separados entre sí por comas (csv).



# Fuente
Datos publicados periódicamente por el grupo ICOVID Chile (https://www.icovidchile.cl). 

# Frecuencia de actualización
Asociado a los informes epidemiológicos publicados por el Ministerio de Salud de Chile.

# Notas aclaratorias
ICOVID Chiles es grupo interdisciplinario de la Pontificia Universidad Católica de Chile, la Universidad de Chile, y la Universidad de Concepción.  El cálculo de estas tasas se enmarcan en un proyecto de colaboración entre el Ministerio de Salud de Chile, el Ministerio de Ciencia, Tecnología, Conocimiento e Innovación de Chile, la Pontificia Universidad Católica de Chile y la Universidad de Chile.




---
---
<br><br><br>

# DP71 - Consulta temprana de casos sintomáticos, provistos por el grupo ICOVID Chile. 

Este producto surge del trabajo colaborativo entre el Ministerio de Salud, el Ministerio de Ciencias, e investigadores del grupo ICOVID Chile (https://www.icovidchile.cl). El producto contiene información sobre la media móvil, de 7 días, de la proporción de personas confirmadas sintomáticas que consultaron un especialista y fueron notificadas dentro de 2 días desde la fecha de iniciados sus síntomas.

# Columnas y valores
El archivo 'not48.nacional.csv' contiene la columna 'fecha_primeros_sintomas' que corresponde a la fecha de inicio de los síntomas, y 'prop2d' que corresponde a  la media móvil, de 7 días, de la proporción de personas confirmadas sintomáticas que consultaron un especialista y fueron notificadas dentro de 2 días desde la fecha de iniciados los síntomas a nivel nacional. Todos estos valores están separados entre sí por comas (csv).

El archivo 'not48.regional.csv' contiene la columna 'fecha_primeros_sintomas' que corresponde a la fecha de inicio de los síntomas, 'region' que corresponde al código de la región, y 'prop2d' que corresponde a  la media móvil, de 7 días, de la proporción de personas confirmadas sintomáticas que consultaron un especialista y fueron notificadas dentro de 2 días desde la fecha de iniciados los síntomas  a nivel regional. Todos estos valores están separados entre sí por comas (csv).

El archivo 'not48.provincial.csv' contiene la columna 'fecha_primeros_sintomas' que corresponde a la fecha de inicio de los síntomas, 'region' que corresponde al código de la región, 'provincia' que corresponde al código de la provincia, y 'prop2d' que corresponde a  la media móvil, de 7 días, de la proporción de personas confirmadas sintomáticas que consultaron un especialista y fueron notificadas dentro de 2 días desde la fecha de iniciados los síntomas a nivel provincial. Todos estos valores están separados entre sí por comas (csv).



# Fuente
Datos publicados periódicamente por el grupo ICOVID Chile (https://www.icovidchile.cl). 

# Frecuencia de actualización
Asociado a los informes epidemiológicos publicados por el Ministerio de Salud de Chile.

# Notas aclaratorias
ICOVID Chiles es grupo interdisciplinario de la Pontificia Universidad Católica de Chile, la Universidad de Chile, y la Universidad de Concepción.  El cálculo de estas tasas se enmarcan en un proyecto de colaboración entre el Ministerio de Salud de Chile, el Ministerio de Ciencia, Tecnología, Conocimiento e Innovación de Chile, la Pontificia Universidad Católica de Chile y la Universidad de Chile.




---
---
<br><br><br>

# DP72 - Tiempo de examen y laboratorio de casos sintomáticos, provistos por el grupo ICOVID Chile. 

Este producto surge del trabajo colaborativo entre el Ministerio de Salud, el Ministerio de Ciencias, e investigadores del grupo ICOVID Chile (https://www.icovidchile.cl). El producto contiene información sobre la media móvil, de 7 días, de la proporción de personas confirmadas sintomáticas cuyo resultado de PCR positivo a SARS-CoV-2 es informado a la autoridad sanitaria dentro de 1 día desde la notificación como caso sospechoso en Epivigila.

# Columnas y valores
El archivo 'lab24.nacional.csv' contiene la columna 'fecha_primeros_sintomas' que corresponde a la fecha de inicio de los síntomas, y 'prop1d' que corresponde a  la media móvil, de 7 días, de la proporción de personas confirmadas sintomáticas cuyo resultado de PCR positivo a SARS-CoV-2 es informado a la autoridad sanitaria dentro de 1 día desde la notificación como caso sospechoso en Epivigila a nivel nacional. Todos estos valores están separados entre sí por comas (csv).

El archivo 'lab24.regional.csv' contiene la columna 'fecha_primeros_sintomas' que corresponde a la fecha de inicio de los síntomas, 'region' que corresponde al código de la región, y 'prop1d' que corresponde a  la media móvil, de 7 días, de la proporción de personas confirmadas sintomáticas cuyo resultado de PCR positivo a SARS-CoV-2 es informado a la autoridad sanitaria dentro de 1 día desde la notificación como caso sospechoso en Epivigila  a nivel regional. Todos estos valores están separados entre sí por comas (csv).

El archivo 'lab24.provincial.csv' contiene la columna 'fecha_primeros_sintomas' que corresponde a la fecha de inicio de los síntomas, 'region' que corresponde al código de la región, 'provincia' que corresponde al código de la provincia, y 'prop1d' que corresponde a  la media móvil, de 7 días, de la proporción de personas confirmadas sintomáticas cuyo resultado de PCR positivo a SARS-CoV-2 es informado a la autoridad sanitaria dentro de 1 día desde la notificación como caso sospechoso en Epivigila a nivel provincial. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Datos publicados periódicamente por el grupo ICOVID Chile (https://www.icovidchile.cl). 

# Frecuencia de actualización
Asociado a los informes epidemiológicos publicados por el Ministerio de Salud de Chile.

# Notas aclaratorias
ICOVID Chiles es grupo interdisciplinario de la Pontificia Universidad Católica de Chile, la Universidad de Chile, y la Universidad de Concepción.  El cálculo de estas tasas se enmarcan en un proyecto de colaboración entre el Ministerio de Salud de Chile, el Ministerio de Ciencia, Tecnología, Conocimiento e Innovación de Chile, la Pontificia Universidad Católica de Chile y la Universidad de Chile.




---
---
<br><br><br>

# DP - Tasa de incidencia de casos confirmados, por cada 100 mil habitantes, según grupo etario y semana epidemiológica. 

El producto contiene información sobre la tasa de incidencia por cada 100 mil habitantes, de casos confirmados según semana epidemiológica de la notificación y grupo etario. 

# Columnas y valores
El archivo 'incidencia_edad_nacional.csv' contiene la columna 'semana_epidemiologica' que corresponde a la semana epidemiológica de la notificación, 'grupo_edad' que corresponde al grupo etario,  'tasa_incidencia' que corresponde a la tasa de incidencia por cada 100 mil habitantes a nivel nacional, y 'tasa_incidencia_categoria'  que corresponde a una versión categórica de la tasa de incidencia. Todos estos valores están separados entre sí por comas (csv).

El archivo 'incidencia_edad_regionales.csv' contiene la columna 'codigo_region' que corresponde al código de la región de residencia, 'region_residencia' que corresponde al nombre de la región de residencia, 'semana_epidemiologica' que corresponde a la semana epidemiológica de la notificación, 'grupo_edad' que corresponde al grupo etario,  'tasa_incidencia' que corresponde a la tasa de incidencia por cada 100 mil habitantes a nivel regional, y 'tasa_incidencia_categoria'  que corresponde a una versión categórica de la tasa de incidencia. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Datos publicados como parte del Informe Epidemiológico elaborado por el Departamento de Epidemiología de MINSAL.

# Frecuencia de actualización
Asociado a los informes epidemiológicos publicados por el Ministerio de Salud de Chile.


---
---
<br><br><br>

# DP74 - Etapas del plan paso a paso por comuna: Descripción
Archivo que da cuenta de la etapa en que se encontraba cada comuna por día  (desde que inició el plan Paso a Paso) en cada una de las comunas de Chile, definido por la autoridad sanitaria.

Etapa 1: Cuarentena

Etapa 2: Transición

Etapa 3: Preparación

Etapa 4: Apertura inicial

Etapa 5: Apurtura avanzada


# Columnas y valores
El archivo paso_a_paso.csv contiene las columnas 'Región', ‘Código Región’, 'Comuna', ‘Código comuna’, y múltiples columnas correspondientes a '[fecha]'. Esta última contiene el valor del paso en que se encontraba la comuna. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Ministerio de Salud de Chile

# Frecuencia de actualización

El equipo del Ministerio de Salud trabaja en curar la información histórica con las publicaciones en el Diario Oficial para poder actualizar el archivo cada vez que se actualiza el estado del territorio.

---
---
<br><br><br>

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

---
---
<br><br><br>

# DP76 - Avance en Campaña de Vacunación COVID-19: Descripción
Este producto da cuenta del avance en la campaña de vacunación contra Sars-Cov-2. Incluye información regional acorde a la residencia reportada y fabricante de la vacuna.

Salvo los archivos vacunacion.csv, el resto han dejado de ser mantenidos en su origen (https://github.com/juancri/covid19-vaccination/issues/34). Pueden obtener la información que entregan de las siguientes fuentes en este repo, que se mantendrán actualizadas:

- Por laboratorio que fabrica y ocurrencia de la inoculación:  https://github.com/MinCiencia/Datos-COVID19/blob/master/output/producto83
- Total y avance diario por edad: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto78 
- Total por edad y comuna: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto81
- Total por edad y región: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto77
- Total por grupo prioritario: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto79


# Columnas y valores
El archivo vacunacion.csv tiene las columnas 'Region', que indica la ubicación donde se administró la dosis, 'Dosis', que indica si es la primera o la segunda, y la serie de columnas correspondientes a la fecha, que indica la cantidad administrada por día.

El archivo fabricante.csv tiene las columnas 'Fabricante', que indica el fabricantee de la dosis administrada, 'Dosis', que indica si es la primera o la segunda, y la serie de columnas correspondientes a la fecha, que indica la cantidad administrada por día.

# Fuente
Ministerio de Salud. Ver en:
https://informesdeis.minsal.cl/SASVisualAnalytics/

# Frecuencia de actualización
Actualización diaria. 


---
---
<br><br><br>

# DP77 - Avance en Campaña de Vacunación COVID-19 por edad y región
Este producto da cuenta del avance en la campaña de vacunación contra Sars-Cov-2. 

# Columnas y valores
El archivo .csv tiene las columnas 'Region', que indica la ubicación donde se administró la dosis, 'Dosis', que indica si es la primera o la segunda, y la serie de columnas correspondientes a la fecha, que indica la cantidad administrada por edad.

# Fuente
Ministerio de Salud. Ver en:
https://informesdeis.minsal.cl/SASVisualAnalytics/

# Frecuencia de actualización
Actualización diaria. 


---
---
<br><br><br>

# DP79 - Avance en Campaña de Vacunación COVID-19 por edad y fecha
Este producto da cuenta del avance en la campaña de vacunación contra Sars-Cov-2. 

# Columnas y valores
El archivo .csv tiene las columnas 'Region', que indica la ubicación donde se administró la dosis, 'Dosis', que indica si es la primera o la segunda, y la serie de columnas correspondientes a la fecha, que indica la cantidad administrada por edad.

# Fuente
Ministerio de Salud. Ver en:
https://informesdeis.minsal.cl/SASVisualAnalytics/

# Frecuencia de actualización
Actualización diaria. 


---
---
<br><br><br>

# DP79 - Avance en Campaña de Vacunación COVID-19 por grupo prioritario
Este producto da cuenta del avance en la campaña de vacunación contra Sars-Cov-2. 

# Columnas y valores
El archivo .csv tiene las columnas 'Region', que indica la ubicación donde se administró la dosis, 'Dosis', que indica si es la primera o la segunda, y la serie de columnas correspondientes a la fecha, que indica la cantidad administrada por edad.

# Fuente
Ministerio de Salud. Ver en:
https://informesdeis.minsal.cl/SASVisualAnalytics/

# Frecuencia de actualización
Actualización diaria. 


---
---
<br><br><br>

# DP80 - Campaña de vacunación informada por el Departamento de Estadísticas e Información Sanitaria (DEIS) por comuna: Descripción
Datos que corresponden a los vacunados en cada una de las comunas de Chile, según residencia y fecha. Estos datos provienen del Departamento de Estadísticas e Información Sanitaria (DEIS) del Ministerio de Salud del país. 

El DEIS hace mejoras al registro de vacunación a medida que analiza diversas fuentes de datos. 

Se entiende por comuna de residencia la comuna que se declaró la vivienda del paciente. 

# Columnas y valores
Los archivos en esta carpeta contienen las columnas 'Región', ‘Código Región’, 'Comuna', ‘Código comuna’, 'Población', y una serie de columnas 'Fecha', que corresponden a la fecha que el DEIS confirma la vacunación. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Datos publicados periódicamente por el Departamento de Estadísticas e Información Sanitaria (DEIS), Ministerio de Salud de Chile. Ver en:
https://deis.minsal.cl/

# Frecuencia de actualización

2 veces al día

# Notas aclaratorias

**Nota aclaratoria 1:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

---
---
<br><br><br>

# DP81 - Campaña de vacunación informada por el Departamento de Estadísticas e Información Sanitaria (DEIS) por comuna y edd: Descripción
Datos que corresponden a los vacunados en cada una de las comunas de Chile, según residencia y edad. Estos datos provienen del Departamento de Estadísticas e Información Sanitaria (DEIS) del Ministerio de Salud del país. 

El DEIS hace mejoras al registro de vacunación a medida que analiza diversas fuentes de datos. 

Se entiende por comuna de residencia la comuna que se declaró la vivienda del paciente. 

# Columnas y valores
Los archivos en esta carpeta contienen las columnas 'Región', ‘Código Región’, 'Comuna', ‘Código comuna’, 'Población', y una serie de columnas 'Edad', que corresponden a la edad de la persona vacunada. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Datos publicados periódicamente por el Departamento de Estadísticas e Información Sanitaria (DEIS), Ministerio de Salud de Chile. Ver en:
https://deis.minsal.cl/

# Frecuencia de actualización

2 veces al día

# Notas aclaratorias

**Nota aclaratoria 1:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

---
---
<br><br><br>

# ISCI Producto movilidad por comunas

## Datasets:

- **week:** contiene la variación de movilidad en cada comuna, tomando como referencia las dos primeras semanas de marzo 2020. Considera días de semana (lunes-viernes) excluyendo festivos.
- **weekend:** contiene la variación de movilidad en cada comuna, tomando como referencia las dos primeras semanas de marzo 2020. Considera fines de semana (sabado-domingo).

Corresponde a un archivo .csv que contiene las siguientes variables:

## Variables



- **comuna:** CUT de la comuna.
- **nom_comuna:** nombre de la comuna.
- **region:** CUT de la region
- **semana:** semana de observación.
- **fecha_inicio:** fecha del primer día considerado en la semana (o fin de semana) correspondiente.
- **fecha_termino:** fecha del último día considerado en la semana (o fin de semana) correspondiente.
- **var_salidas_cota_superior:** cota superior de movilidad hacia afuera de la comuna durante determinada semana, con respecto al nivel base (promedio dos primeras semanas de marzo 2020).
- **var_salidas_cota_inferior:** cota inferior de la variación de movilidad hacia afuera de la comuna durante determinada semana, con respecto al nivel base.
- **var_salidas:** estimación de la variación de movilidad hacia afuera de la comuna durante determinada semana, con respecto al nivel base. Corresponde al promedio entre **var_salidas_cota_superior** y **var_salidas_cota_inferior.**
- **paso:** etapa del plan paso a paso en la que se encontró la comuna durante la mayor parte de la semana.

## Notas
 - Por problemas en la captación de datos, existen semanas que no están disponibles en el producto.
## Más información en:

- [https://covidanalytics.isci.cl/movilidad/visor-movilidad/](https://covidanalytics.isci.cl/movilidad/visor-movilidad/)
- [https://covidanalytics.isci.cl/movilidad/reportes/](https://covidanalytics.isci.cl/movilidad/reportes/)
- [https://isci.cl/wp-content/uploads/2020/06/Social-Cuarentenas-v6-ISCI.pdf](https://isci.cl/wp-content/uploads/2020/06/Social-Cuarentenas-v6-ISCI.pdf)

---
---
<br><br><br>

# DP77 - Avance en Campaña de Vacunación COVID-19 por establecimiento
Este producto da cuenta del avance en la campaña de vacunación contra Sars-Cov-2. 

# Columnas y valores
El archivo .csv tiene las columnas 'establecimiento', que indica la ubicación donde se administró la dosis, 'Dosis', que indica si es la primera o la segunda, y la serie de columnas correspondientes a la fecha, que indica la cantidad administrada por edad.

# Fuente
Ministerio de Salud. Ver en:
https://informesdeis.minsal.cl/SASVisualAnalytics/

# Frecuencia de actualización
Actualización diaria. 


---
---
<br><br><br>

# DP84 - Defunciones por COVID en Chile (reporte diario, provisorio): Descripción.
 
Los datos en defunciones.csv (y sus versiones transpuestas y std) provienen de los registros de inscripciones de fallecimientos del Registro Civil de Chile, cruzados diariamente con el registro de los resultados de laboratorio para el diagnóstico COVID19 en Chile (RT-PCR), que consolida y cura el Departamento de Epidemiología del Minsal.
 
Los criterios para identificar fallecidos debido a COVID19 para efectos del reporte diario en defunciones.csv son:
1) Certificado de defunción incluye COVID19 o algún término relacionado (se excluyen causas externas, como trauma).
2) Existe un examen positivo de RT-PCR para SARS-CoV-2 en la base de datos de laboratorio.
 
A su vez, los datos en defunciones_deis.csv (y sus versiones transpuestas y std) provienen del Departamento de Estadística e Información del Minsal (DEIS). El DEIS hace mejoras al registro de defunciones a medida que analiza diversas fuentes de datos, estas mejoras estudian la causa de defunción indicada en el certificado médico y la presencia de resultados RT-PCR, en caso de ser la defunción por cuadro clínico compatible a COVID19, y contar con PCR(-), o no haber sido testeado se incluye como sospechoso, mientras que si existe PCR(+) se incluye como confirmado.

En ambos archivos, la columna “Defunciones” se refiere a la fecha de defunción (no es la fecha de inscripción).

Más información relacionada con el procesamiento de esta información: https://github.com/MinCiencia/Datos-COVID19/issues/457
 
# Columnas y valores
Los archivos defunciones contienen las columnas 'Defunciones' y múltiples columnas correspondientes a '[fecha]'. Estas últimas columnas, ‘[fecha]’, contienen las 'Defunciones (por fecha de fechas de defunción)' inscritas en el Registro Civil de Chile con relación a COVID19, que al cruzar con la base de laboratorios tienen PCR positivo, y son datos provisorios a la fecha de publicación que se pueden actualizar retroactivamente.

Los archivos defunciones_deis contienen las columnas 'Confirmados', 'Sospechosos' y múltiples columnas correspondientes a '[fecha]'. Estas últimas columnas, ‘[fecha]’, contienen las 'Defunciones (por fecha de fechas de defunción)' confirmadas o sospchosas.
 
# Fuente
Servicio de Registro Civil de Chile y División de Planificación Sanitaria del Ministerio de Salud de Chile.
 
# Frecuencia de actualización
Diaria (Registro Civil) y Semanal (DEIS)
 
# Notas aclaratorias
**Nota aclaratoria 1:** El Registro Civil de Chile y el Ministerio de Salud de Chile elaboran esta información en base a las actuaciones que le son propias y que se encuentran registradas en una fecha y hora determinada, sin embargo, estas son variables, ya que pueden ser objeto de rectificación no constituyendo, en consecuencia, una estadística oficial del Estado de Chile, materia que es competencia del Instituto Nacional de Estadísticas (INE) (número de fallecidos) y del Departamento de Estadísticas e Información en Salud (DEIS), Minsal (causas de defunción).
 
**Nota aclaratoria 2:** Los datos son provisorios. Los valores reportados por día pueden variar retroactivamente en cada actualización, en la medida que se recibe información de exámenes de laboratorio pendientes.

---
---
<br><br><br>

# PD85: Datos del estudio de la prevalencia de anticuerpos SARS-CoV-2 en trabajadores del sector salud, durante la primera ola de COVID-19 en Chile
 
En este documento es posible revisar los resultados del estudio para el levantamiento de la prevalencia de anticuerpos SARS-CoV-2 en trabajadores del sector salud, durante la primera ola de COVID-19 en Chile

# Columnas y Valores
Corresponde a datos recolectados en el estudio de prevalencia de anticuerpos SARS-CoV-2 en trabajadores del sector salud, durante la primera ola de COVID-19 en Chile.

# Fuente
Estudio de prevalencia de anticuerpos SARS-CoV-2 en trabajadores del sector salud, durante la primera ola de COVID-19 en Chile, año 2020.

# Frecuencia de actualización
No aplica.

# Notas Aclaratorias
El archivo doc_soporte.md contiene información de soporte de para la utilización de la fuente. Para el caso del diccionario de variables, se sugiere revisar la carpeta “imágenes”

---
---
<br><br><br>

# Semáforo Poop COVID-19 en la comuna de San Pedro de la Paz en la Región del Bío Bío

El semáforo Poop COVID-19 es una herramienta que permite conocer con anticipación el alza o baja de circulacón viral del COVID-19 en las aguas servidas. 

# Colores del semáforo

Los colores son: 1 - Verde (Prevencion) / 2 - Amarillo (Precaución) / 3 - Naranjo (Alerta) / 4 - Rojo (Grave).

# Zonas del semáforo

Las zonas se pueden visualizar en https://midas-uc.shinyapps.io/semaforo-San-Pedro/. Estas corresponden a:

Zona 1: El Recodo- Camino a Santa Juana / 
Zona 2: El Venado /
Zona 3: Andalue - Los Canelos /
Zona 4: Villa San Pedro - Bayona /
Zona 5: Huertos Familiares / 
Zona 6: Candelaria 2 /
Zona 7: Candelaria 3 /
Zona 8: Boca Sur 1 /
Zona 9: Boca Sur 3 /
Zona 10: San Pedro de la Costa /
Zona 11: Michaihue /
Zona 12a: Lomas Coloradas /
Zona 12b: La Estrella /
Zona 12c: Boca Sur 2 /
Zona 12d: Candelaria 1.

# Columnas y valores

El archivo alertas_por_zona.csv contiene las columas 'Fecha', 'Zona2', 'Zona3', 'Zona4', 'Zona5', 'Zona6', 'Zona7', 'Zona8', 'Zona9', 'Zona10', 'Zona11', 'Zona12a', 'Zona12b', 'Zona12c' y 'Zona12d'. Estos valores están separados entre sí por comas (csv). Los valores corresponden al color del semáforo.

# Información sobre el proceso de detección de carga viral 

El tipo de muestra corresponde a aguas servidas (domiciliaria), 2 L de agua compuesta (5 L), según protocolo de Biodiversa S.A. La extracción se realizó vía concentración por centrifugación, TRIzol (Thermofisher) y purificación (columnas-EZNA). El método de detección utilizado es Real-time Fluorescent RT-PCR kit for 2019nCoV (BGI) / LightCycler 480 (ROCHE).

# Frecuencia de actualización

1 vez por semana (cada viernes).

# Elaboración

El semáforo Poop COVID-19, iniciativa de la Seremi de Ciencias de la Macrozona Centro Sur Paulina Assmann, es elaborado por Alejandro Jara, Isabelle Beaudry, José Verschae y Mauricio Castro, miembros del Núcleo Milenio Centro para el Descubrimiento de Estructuras en Datos Complejos - MiDaS y académicos de la Pontificia Universidad Católica de Chile. También participan los estudiantes de la Pontificia Universidad Católica de Chile, Felipe Gutierrez, José Baboun, Benjamín Rubio, Alberto Moenne-Loccoz y Eduardo Vásquez, este último responsable de la visualización del semáforo. Los académicos Matías Hepp y Andressa Reis pertenecientes al Laboratorio de Investigación en Ciencias Biomédicas, Universidad Católica de la Santísima Concepción son quienes procesan las muestras de aguas servidas.
---
---
<br><br><br>

# DP87 - Exámenes Ag por región de toma de muestra: Descripción
Set de 3 archivos que dan cuenta del número de exámenes Ag realizados por región reportados diariamente por el Ministerio de Salud, desde el 5 de junio de 2021. 

El proceso ocurre hasta la fecha de la siguiente manera: 1) Hay centros de testeo móviles en todo el territorio nacional 2) personas se realizan test voluntariamente 3) el resultado se informa en 1 a 2 horas, se contabiliza en este reporte durante el día.

# Columnas y valores
El archivo (Ag.csv) contiene las columnas ‘Región’, ‘Código Región’ y ‘Población’, seguidas por columnas correspondientes a ‘[Fecha]’. Estas últimas columnas, ‘[Fecha]’ indican el número de exámenes realizados por región. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Reporte diario del Ministerio de Salud. Ver en: https://www.gob.cl/coronavirus/cifrasoficiales/#reportes

# Frecuencia de actualización
Actualización diaria. 

# Notas aclaratorias

**Nota aclaratoria 1:** Los reportes del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

---
---
<br><br><br>

# DP88 - Avance en Campaña de Vacunación COVID-19 por laboratorio fabricante
Este producto da cuenta del avance en la campaña de vacunación contra Sars-Cov-2. 

# Columnas y valores
El archivo .csv tiene las columnas 'Fabricante', que indica el laboratorio productor, 'Dosis', que indica si es la primera o la segunda, y la serie de columnas correspondientes a la fecha, que indica la cantidad administrada por edad.

# Fuente
Ministerio de Salud. Ver en:
https://informesdeis.minsal.cl/SASVisualAnalytics/

# Frecuencia de actualización
Actualización diaria. 


---
---
<br><br><br>

# DP - Incidencia de casos según estado de vacunación, grupo de edad, y semana epidemiológica. 

El producto contiene información sobre los casos confirmados, ingresos a hospitalización, ingreso a UCI y defunciones, según estado de vacunación, grupo de edad y semana epidemiológica

# Columnas y valores
El archivo 'incidencia_en_vacunados_edad.csv' contiene las siguientes columnas:

- 'semana_epidemiologica' que corresponde a la semana epidemiologica desde el año 2021, 

- 'grupo_edad' incidando el grupo de edad,

- 'estado_vacunacion' corresponde al estado de vacunación la que se clasifica en 
  - Esquema completo entre 14 días y 6 meses: aquellas personas que han sido inoculadas con dos dosis y han transcurrido entre 14 días y 6 meses desde su
  segunda inoculación o han recibido una vacuna de un esquema de vacunación que incluye únicamente una sola dosis y han transcurrido entre 14 días y 6 meses desde la inoculación,
  - Esquema completo mayor a 6 meses: personas 
  que han sido inoculadas con dos dosis y han transcurrido más de 6 meses desde su segunda inoculación o han recibido una vacuna de un esquema de vacunación que incluye únicamente una sola dosis y han transcurrido de más 6 meses desde la
  inoculación, 
  - 1° dosis refuerzo entre 14 días y 6 meses: aquellas personas que han recibido una dosis de refuerzo a su esquema completo y han transcurrido entre 14 días y 6 meses desde su inoculación, 
  - 1° dosis refuerzo mayor a 6 meses
  para aquellas personas que han recibido una dosis de refuerzo a su esquema completo y han transcurrido más de 6 meses desde su inoculación, 
  - 2° dosis refuerzo entre 14 días y 6 meses para aquellas personas que han recibido la segunda de 
  dosis de refuerzo a su esquema completo y han transcurrido entre 14 días y 6 meses desde su inoculación, 
  - 2° dosis refuerzo más de 6 meses para aquellas personas que han recibido la segunda de dosis de refuerzo a su esquema completo y han
  transcurrido más de 6 meses desde su inoculación. 
  - Esta variable toma el valor "sin esquema completo" si las personas no tienen un esquema completo de vacunación.

- 'casos_confirmados' indicando el número de casos confirmados del grupo de edad y estado de vacunación correspondiente, y reportados durante la semana epidemiológica correspondiente.

- 'casos_hospi' indicando el número de casos confirmados del grupo de edad y estado de vacunación correspondiente, y que ingresaron a hospitalización durante la semana epidemiológica correspondiente.

- 'casos_uci' indicando el número de casos confirmados del grupo de edad y estado de vacunación correspondiente, y que ingresaron a UCI durante la semana epidemiológica correspondiente.

- 'casos_def' indicando el número de casos confirmados del grupo de edad y estado de vacunación correspondiente, y que fallecieron de COVID-19 durante la semana epidemiológica correspondiente.

- 'poblacion' corresponde al total de personas que cumplen con el estado de vacunación correspodiente en la semana epidemiológica en consideración.

- 'incidencia_cruda_confirmados' corresponde a la tasa de incidencia (por cada 100 mil habitantes) para el grupo de edad, estado de vacunación correspondiente y semana epidemiológica correspondiente.

- 'incidencia_cruda_hospi' corresponde a la tasa de incidencia hospitalización (por cada 100 mil habitantes) para el grupo de edad, estado de vacunación correspondiente y semana epidemiológica correspondiente.

- 'incidencia_cruda_uci' corresponde a la tasa de incidencia UCI (por cada 100 mil habitantes) para el grupo de edad, estado de vacunación correspondiente y semana epidemiológica correspondiente.

- 'incidencia_cruda_def' corresponde a la tasa de incidencia de casos fallecidos por cada 100 mil habitantes) para el grupo de edad, estado de vacunación correspondiente y semana epidemiológica correspondiente.

- 'incidencia_ponderada_confirmados' corresponde a la tasa de incidencia cruda ajustada por la población para el grupo de edad, estado de vacunación correspondiente y semana epidemiológica correspondiente.

- 'incidencia_ponderada_hospi' corresponde a la tasa de incidencia cruda ajustada por la población para el grupo de edad, estado de vacunación correspondiente y semana epidemiológica correspondiente.

- 'incidencia_ponderada_uci' corresponde a la tasa de incidencia cruda ajustada por la población para el grupo de edad, estado de vacunación correspondiente y semana epidemiológica correspondiente.

- 'incidencia_ponderada_def' corresponde a la tasa de incidencia cruda ajustada por la población para el grupo de edad, estado de vacunación correspondiente y semana epidemiológica correspondiente.

Todos estos valores están separados entre sí por comas (csv).

# Fuente
Departamento de Epidemiología, Ministerio de Salud de Chile. 

# Frecuencia de actualización
Asociado a los informes semanales, publicados por el Ministerio de Salud de Chile.


# NOTA ACLARATORIA:
- El producto 89 presenta los eventos de casos, ingresos UCI y defunciones, según ocurrencia en la semana de reporte. Estos son consolidados sin una actualización retrospectiva, por lo cual podría presentar diferencias con otros reportes que se emiten en paralelo.

- El producto 90 presenta las cifras de casos, ingresos UCI y defunciones según semana de inicio de síntomas, no por  ocurrencia del evento, con actualización retrospectiva semanal, por lo cual podría presentar diferencias con otros reportes que se emiten en paralelo.

- Los casos confirmados de SARS-CoV-2 totales, sintomáticos, ingresados hospitalizaión, ingreso a UCI y fallecidos reportados en este informe incorporan las modificaciones señaladas en el Ordinario B51/N°4518 del 15 de noviembre del 2021, lo que podría explicar variaciones en el número de casos por semanas epidemiológicas presentado en versiones previas. La información corresponde a data provisoria,en proceso de validación.

- Para generar la categorización de estado de vacunación, se calcula el tiempo transcurrido entre la fecha de inicio síntomas y la última fecha de vacunación

---
---
<br><br><br>

# DP - Distribución de casos según antecedentes de vacunación y semana epidemiológica. 

El producto contiene información sobre los casos confirmados, ingresos a hospitalización, ingresos a UCI y defunciones, según el estado de vacunación y semana epidemiológica.

# Columnas y valores
El archivo 'carga_vacunacion_sem_epi.csv' contiene las columnas 

- 'semana_epidemiologica' que corresponde a la semana epidemiologica desde el año 2021, 

- 'sin_vac_casos'  indicando el número de casos confirmados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) no ha recibido ninguna dosis de vacuna,

- 'esq_comp_entre14diasy6meses_casos' indicando el  número casos confirmados durante la semana epidemiológica correspondiente,  y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han sido inoculada con dos dosis y han transcurrido entre 14 días y 6 meses desde su segunda inoculación o ha recibido una vacuna de un esquema de vacunación que incluye únicamente una sola dosis y han transcurrido entre 14 días y 6 meses desde la inoculación,

- 'esq_comp_mayora6meses_casos' indicando el número de casos confirmados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han sido inoculada con dos dosis y han transcurrido más de 6 meses desde su segunda inoculación o ha recibido una vacuna de un esquema de vacunación que incluye únicamente una sola dosis y han transcurrido más de 6 meses desde la inoculación,

- 'primer_ref_entre14diasy6meses_casos' indicando el número de casos confirmados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido una dosis de refuerzo a su esquema completo y han transcurrido entre 14 días y 6 meses desde la tercera dosis,

- 'primer_ref_mayora6meses_casos' indicando el número de casos confirmados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o  al momento de la toma de muestra (asintomáticos) han recibido una dosis de refuerzo a su esquema completo y han transcurrido más de 6 meses desde la tercera dosis,

- 'segunda_ref_entre14diasy6meses_casos' indicando el numero de casos confirmados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o  al momento de la toma de muestra (asintomáticos) han recibido su segunda dosis de refuerzo a su esquema completo y han transcurrido entre 14 días y 6 meses desde la cuarta dosis,

- 'segunda_ref_mayora6meses_casos' indicando el numero de casos confirmados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o toma de muestra (asintomáticos) han recibido su segunda dosis de refuerzo a su esquema completo y han transcurrido más de 6 meses desde la cuarta dosis,

- 'sin_vac_hospi' indicando el número de casos confirmados que ingresaron a hospitalización durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momentro de la toma de muestra (asintomáticos) no ha recibido ninguna dosis de vacuna,

- 'esq_comp_entre14diasy6meses_hospi' indicando el  número casos confirmados que ingresaron a hospitalización durante la semana epidemiológica correspondiente,  y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han sido inoculada con dos dosis y han transcurrido entre 14 días y 6 meses desde su segunda inoculación o ha recibido una vacuna de un esquema de vacunación que incluye únicamente una sola dosis y han transcurrido entre 14 días y 6 meses desde la inoculación,

- 'esq_comp_mayora6meses_hospi' indicando el número de casos confirmados que ingresaron a hospitalización durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han sido inoculada con dos dosis y han transcurrido más de 6 meses desde su segunda inoculación o ha recibido una vacuna de un esquema de vacunación que incluye únicamente una sola dosis y han transcurrido más de 6 meses desde la inoculación,

- 'primer_ref_entre14diasy6meses_hospi' indicando el número de casos confirmados que ingresaron a hospitalización durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido una dosis de refuerzo a su esquema completo y han transcurrido entre 14 días y 6 meses desde la tercera dosis,

- 'primer_ref_mayora6meses_hospi' indicando el número de casos confirmados que ingresaron a hospitalización durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o  al momento de la toma de muestra (asintomáticos) han recibido una dosis de refuerzo a su esquema completo y han transcurrido más de 6 meses desde la tercera dosis,

- 'segunda_ref_entre14diasy6meses_hospi' indicando el numero de casos confirmados que ingresaron a hospitalización durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o  al momento de la toma de muestra (asintomáticos) han recibido su segunda dosis de refuerzo a su esquema completo y han transcurrido entre 14 días y 6 meses desde la cuarta dosis,

- 'segunda_ref_mayora6meses_hospi' indicando el numero de casos confirmados que ingresaron a hospitalización durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o toma de muestra (asintomáticos) han recibido su segunda dosis de refuerzo a su esquema completo y han transcurrido más de 6 meses desde la cuarta dosis,

- 'sin_vac_uci' indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momentro de la toma de muestra (asintomáticos) no ha recibido ninguna dosis de vacuna,

- 'esq_comp_entre14diasy6meses_uci' indicando el  número casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente,  y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han sido inoculada con dos dosis y han transcurrido entre 14 días y 6 meses desde su segunda inoculación o ha recibido una vacuna de un esquema de vacunación que incluye únicamente una sola dosis y han transcurrido entre 14 días y 6 meses desde la inoculación,

- 'esq_comp_mayora6meses_uci' indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han sido inoculada con dos dosis y han transcurrido más de 6 meses desde su segunda inoculación o ha recibido una vacuna de un esquema de vacunación que incluye únicamente una sola dosis y han transcurrido más de 6 meses desde la inoculación,

- 'primer_ref_entre14diasy6meses_uci' indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido una dosis de refuerzo a su esquema completo y han transcurrido entre 14 días y 6 meses desde la tercera dosis,

- 'primer_ref_mayora6meses_uci' indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o  al momento de la toma de muestra (asintomáticos) han recibido una dosis de refuerzo a su esquema completo y han transcurrido más de 6 meses desde la tercera dosis,

- 'segunda_ref_entre14diasy6meses_uci' indicando el numero de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o  al momento de la toma de muestra (asintomáticos) han recibido su segunda dosis de refuerzo a su esquema completo y han transcurrido entre 14 días y 6 meses desde la cuarta dosis,

- 'segunda_ref_mayora6meses_uci' indicando el numero de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o toma de muestra (asintomáticos) han recibido su segunda dosis de refuerzo a su esquema completo y han transcurrido más de 6 meses desde la cuarta dosis,

- 'sin_vac_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momentro de la toma de muestra (asintomáticos) no ha recibido ninguna dosis de vacuna,

- 'esq_comp_entre14diasy6meses_fall' indicando el  número casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente,  y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han sido inoculada con dos dosis y han transcurrido entre 14 días y 6 meses desde su segunda inoculación o ha recibido una vacuna de un esquema de vacunación que incluye únicamente una sola dosis y han transcurrido entre 14 días y 6 meses desde la inoculación,

- 'esq_comp_mayora6meses_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han sido inoculada con dos dosis y han transcurrido más de 6 meses desde su segunda inoculación o ha recibido una vacuna de un esquema de vacunación que incluye únicamente una sola dosis y han transcurrido más de 6 meses desde la inoculación,

- 'primer_ref_entre14diasy6meses_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido una dosis de refuerzo a su esquema completo y han transcurrido entre 14 días y 6 meses desde la tercera dosis,

- 'primer_ref_mayora6meses_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o  al momento de la toma de muestra (asintomáticos) han recibido una dosis de refuerzo a su esquema completo y han transcurrido más de 6 meses desde la tercera dosis,

- 'segunda_ref_entre14diasy6meses_fall' indicando el numero de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o  al momento de la toma de muestra (asintomáticos) han recibido su segunda dosis de refuerzo a su esquema completo y han transcurrido entre 14 días y 6 meses desde la cuarta dosis,

- 'segunda_ref_mayora6meses_fall' indicando el numero de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o toma de muestra (asintomáticos) han recibido su segunda dosis de refuerzo a su esquema completo y han transcurrido más de 6 meses desde la cuarta dosis,


Todos estos valores están separados entre sí por comas (csv).

# Fuente
Departamento de Epidemiología, Ministerio de Salud de Chile. 

# Frecuencia de actualización
Asociado a los informes semanales, publicados por el Ministerio de Salud de Chile.

# NOTA ACLARATORIA
Los casos confirmados de SARS-CoV-2 totales, sintomáticos, ingresados hospitalización, ingreso a UCI y fallecidos reportados en este informe incorporan las modificaciones señaladas en el Ordinario B51/N°4518 del 15 de noviembre del 2021, lo que podría explicar variaciones en el número de casos por semanas epidemiológicas presentado en versiones previas.La información corresponde a data provisoria,en proceso de validación.



---
---
<br><br><br>

# DP91 - Evolución semanal de ingresos UCI pacientes COVID-19

Archivo que da cuenta del número de ingresos en el sistema integrado COVID-19. Se considera el promedio móvil de los últimos 7 días.

Se entiende por ingreso, pacientes que comienzan a ocupar una cama UCI de un establecimiento autorizado para tal fin, tanto de establecimientos privados y públicos del sistema integrado y reportado por la Unidad de Gestión de Camas Críticas (UGCC).

# Columnas y valores
El archivo Ingresos_UCI.csv contiene las columnas 'Media Móvil Ingresos a UCI por COVID-19' presenta una serie de columnas con '[Fecha]' con la media móvil de los últimos 7 días para ingresos reportados.

# Fuente
Unidad de Gestión de Camas Críticas, Subsecretaría de Redes Asitenciales, Ministerio de Salud de Chile
 
# Frecuencia de actualización
Actualización semanal.

---
---
<br><br><br>

# DP92 - Evolución semanal de ingresos a hospitalización de pacientes COVID-19

Archivo que da cuenta del número de ingresos en el sistema integrado COVID-19. Se considera el promedio móvil de los últimos 7 días.

Se entiende por ingreso, pacientes que comienzan a ocupar una cama de un establecimiento autorizado para tal fin, tanto de establecimientos privados y públicos del sistema integrado y reportado por la Unidad de Gestión de Camas Críticas (UGCC).

# Columnas y valores
El archivo “Ingresos-Hospital.csv” contiene las columnas 'Media Móvil Ingresos  hospitalización por COVID-19' presenta una serie de columnas con '[Fecha]' con la media móvil de los últimos 7 días para ingresos reportados.

# Fuente
Unidad de Gestión de Camas Críticas, Subsecretaría de Redes Asitenciales, Ministerio de Salud de Chile
 
# Frecuencia de actualización
Actualización semanal.

# Nota aclaratoria
Los datos se van actualizando retroactivamente a medida que los establecimientos de salud van reportando de forma individualizada a los pacientes que se confirman como paciente Covid, es por esto que no se consideran los 6 días más cercanos a la fecha de reporte ya que se podrían presentar sub-registros.


---
---
<br><br><br>

# DP93 - Contactos Estrechos por Caso Notificado Por Comuna: Descripción
Archivo que da cuenta del promedio de contactos estrechos de los casos nuevos confirmados por laboratorio.

# Columnas y valores

El archivo 'ContactosPorComuna.csv' tiene las columnas 'Región', 'Código región', 'Comuna', 'Código comuna', 'Población', y una serie de columnas '[Fecha]', donde en cada una están la Cantidad promedio de contactos estrechos a la fecha. Todos estos valores están separados entre sí por comas (csv).

# Fuente
* Informe de Indicadores de Testeo y Trazabilidad, departamento de Epidemiología, Ministerio de Salud

# Frecuencia de actualización
Semanal

# Notas aclaratorias

**Nota aclaratoria 1:** Los informes emanados del departamento de epidemiología del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 6 hrs.

**Nota aclaratoria 2:** Los informes de Indicadores de Testeo y Trazabilidad se han publicado a partir del 24 de Agosto 2020.

**Nota aclaratoria 3:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

**Nota aclaratoria 4:** En consideración del Ord. 105/N°3857 que "informa actualización sobre acciones de seguimiento y APS en marco de la estrategia TTA", los indicadores de trazabilidad (correspondientes a los indicadores 5, 6, 7 y Razón de contactos) se presentan basados según región de asignación FONASA. Lo anterior significa que el total regional publicado podría presentar diferencias respecto al detalle a nivel comunal, debido a que el primero es presentado por región de asignación y segundo por comuna de residencia, los cuales no necesariamente coincidirán, y por tanto, no son comparables.

**Nota aclaratoria 5:** Desde el informe publicado el 2 de febrero de 2022, el periodo de análisis de todos los indicadores TTA se basa en semanas epidemiológicas (SE), es decir, abarca de domingo a sábado de la semana previa a la publicación.

Basado en las nuevas definiciones de caso, señaladas en el Ord B51/N°269 del 19 de enero de 2022, los indicadores de trazabilidad, correspondientes a “Oportunidad de la investigación epidemiológica y registro del primer seguimiento de casos”, “Identificación de contactos”, “Oportunidad de la investigación epidemiológica y registro del primer seguimiento de en contactos” e “Indicador global de la estrategia testeo y trazabilidad” fueron adaptados. La descripción de cada uno de ellos se encuentra en el apartado metodológico del informe, disponible en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/, y están abordados dentro de los siguientes ámbitos según las gestiones realizadas en el contexto de la estrategia de trazabilidad, siendo éstas:

- Primer contacto de casos nuevos.
- Estudio de contactos estrechos en contexto de brotes investigados
- Manejo de contactos estrechos y testeo en contexto de brotes
- Investigación de nexo epidemiológico, respectivamente.

Debido a lo anteriormente señalado, el indicador “Relación de contactos por caso” fue suprimido.
---
---
<br><br><br>

# DP94 - Casos considerados en TTA Por Comuna: Descripción
Archivo que da cuenta del promedio de contactos estrechos de los casos nuevos confirmados por laboratorio.

# Columnas y valores

El archivo 'CasosNuevosTotales.csv' tiene las columnas 'Región', 'Código región', 'Comuna', 'Código comuna', 'Población', y una serie de columnas '[Fecha]', donde en cada una están la Cantidad de casos considerados en TTA por comuna. Todos estos valores están separados entre sí por comas (csv).

# Fuente
* Informe de Indicadores de Testeo y Trazabilidad, departamento de Epidemiología, Ministerio de Salud

# Frecuencia de actualización
Semanal

# Notas aclaratorias

**Nota aclaratoria 1:** Los informes emanados del departamento de epidemiología del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 6 hrs.

**Nota aclaratoria 2:** Los informes de Indicadores de Testeo y Trazabilidad se han publicado a partir del 24 de Agosto 2020.

**Nota aclaratoria 3:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).

**Nota aclaratoria 4:** En consideración del Ord. 105/N°3857 que "informa actualización sobre acciones de seguimiento y APS en marco de la estrategia TTA", los indicadores de trazabilidad (correspondientes a los indicadores 5, 6, 7 y Razón de contactos) se presentan basados según región de asignación FONASA. Lo anterior significa que el total regional publicado podría presentar diferencias respecto al detalle a nivel comunal, debido a que el primero es presentado por región de asignación y segundo por comuna de residencia, los cuales no necesariamente coincidirán, y por tanto, no son comparables.

**Nota aclaratoria 5:** Desde el informe publicado el 2 de febrero de 2022, el periodo de análisis de todos los indicadores TTA se basa en semanas epidemiológicas (SE), es decir, abarca de domingo a sábado de la semana previa a la publicación.

Basado en las nuevas definiciones de caso, señaladas en el Ord B51/N°269 del 19 de enero de 2022, los indicadores de trazabilidad, correspondientes a “Oportunidad de la investigación epidemiológica y registro del primer seguimiento de casos”, “Identificación de contactos”, “Oportunidad de la investigación epidemiológica y registro del primer seguimiento de en contactos” e “Indicador global de la estrategia testeo y trazabilidad” fueron adaptados. La descripción de cada uno de ellos se encuentra en el apartado metodológico del informe, disponible en: https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/, y están abordados dentro de los siguientes ámbitos según las gestiones realizadas en el contexto de la estrategia de trazabilidad, siendo éstas:

- Primer contacto de casos nuevos.
- Estudio de contactos estrechos en contexto de brotes investigados
- Manejo de contactos estrechos y testeo en contexto de brotes
- Investigación de nexo epidemiológico, respectivamente.

Debido a lo anteriormente señalado, el indicador “Relación de contactos por caso” fue suprimido.
---
---
<br><br><br>

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
---
---
<br><br><br>

# DP96 - Estimación de exceso de mortalidad elaborado DEIS (datos abiertos DEIS): Descripción.

Modelo elaborado por el DEIS para estimar el exceso de mortalidad utilizando la serie de defunciones 2016-2022 publicada en la página del DEIS (http://deis.minsal.cl)
El modelo ajusta por tendencia y estacionalidad usando media armónica.

# Fuente
Departamento de Estadísticas e Información de Salud. Ver _"Defunciones por Causa (actualización semanal)"_ en:
https://deis.minsal.cl/#datosabiertos 
 
# Frecuencia de actualización
Semanal

---
---
<br><br><br>

