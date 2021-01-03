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





