# DP - Distribución de casos según antecedentes de vacunación y semana epidemiológica. 

El producto contiene información sobre los casos confirmados, ingresos a UCI y defunciones, según el estado de vacunación y semana epidemiológica según el inicio de síntomas.

# Columnas y valores
El archivo 'incidencia_en_vacunados.csv' contiene las columnas 

- 'semana_epidemiologica' que corresponde a la semana epidemiologica del año 2021 según el inicio de síntomas, 

- 'sin_vac_casos'  indicando el número de casos confirmados, reportados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) no ha recibido ninguna dosis de vacuna,

- 'una_dosis_casos' indicando el  número casos confirmados, reportados durante la semana epidemiológica correspondiente,  y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido la primera dosis y no la segunda dosis, en un esquema que incluye dos dosis,

- 'dos_dosis_casos' indicando el número de casos confirmados, reportados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos)  han recibido dos dosis, en un esquema de que incluye dos dosis, y han transcurrido 14 días o menos desde la segunda dosis,

- 'dos_dosis_comp_casos' indicando el número de casos confirmados, reportados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido dos dosis y han transcurrido más de 14 días desde la segunda dosis,

- 'dosis_unica_casos' indicando el número de casos confirmados, reportados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o  al momento de la toma de muestra (asintomáticos) han recibido una dosis de una vacuna de un esquema de vacunación que incluye una sola dosis y han transcurrido 14 días o menos desde la vacunación,

- 'dosis_unica_comp_casos' indicando el numero de casos confirmados, reportados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o  al momento de la toma de muestra (asintomáticos) han recibido una dosis de una vacuna de un esquema de vacunación que incluye una sola dosis y han transcurrido más de 14 días desde la vacunación,

- 'sin_vac_uci' indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momentro de la toma de muestra (asintomáticos) no ha recibido ninguna dosis de vacuna,

- 'una_dosis_uci' indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido la primera dosis y no la segunda dosis, en un esquema que incluye dos dosis,

- 'dos_dosis_uci' indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos)  han recibido dos dosis, en un esquema de que incluye dos dosis, y han transcurrido 14 días o menos desde la segunda dosis,

- 'dos_dosis_comp_uci'  indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido dos dosis y han transcurrido más de 14 días desde la segunda dosis,

- 'dosis_unica_uci' indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o  al momento de la toma de muestra (asintomáticos) han recibido una dosis de una vacuna de un esquema de vacunación que incluye una sola dosis y han transcurrido 14 días o menos desde la vacunación,

- 'dosis_unica_comp_uci' indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido una dosis de una vacuna de un esquema de vacunación que incluye una sola dosis y han transcurrido más de 14 días desde la vacunación

- 'sin_vac_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momentro de la toma de muestra (asintomáticos) no ha recibido ninguna dosis de vacuna,

- 'una_dosis_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido la primera dosis y no la segunda dosis, en un esquema que incluye dos dosis,

- 'dos_dosis_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos)  han recibido dos dosis, en un esquema de que incluye dos dosis, y han transcurrido 14 días o menos desde la segunda dosis,

- 'dos_dosis_comp_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido dos dosis y han transcurrido más de 14 días desde la segunda dosis,

- 'dosis_unica_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o  al momento de la toma de muestra (asintomáticos) han recibido una dosis de una vacuna de un esquema de vacunación que incluye una sola dosis y han transcurrido 14 días o menos desde la vacunación,

- 'dosis_unica_comp_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido una dosis de una vacuna de un esquema de vacunación que incluye una sola dosis y han transcurrido más de 14 días desde la vacunación,

Todos estos valores están separados entre sí por comas (csv).

# Fuente
Departamento de Epidemiología, Ministerio de Salud de Chile. 

# Frecuencia de actualización
Asociado a los informes semanales, publicados por el Ministerio de Salud de Chile.



