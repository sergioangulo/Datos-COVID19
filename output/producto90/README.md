# DP - Distribución de casos según antecedentes de vacunación y semana epidemiológica. 

El producto contiene información sobre los casos confirmados, ingresos a UCI y defunciones, según el estado de vacunación y semana epidemiológica.

# Columnas y valores
El archivo 'incidencia_en_vacunados.csv' contiene las columnas 

- 'semana_epidemiologica' que corresponde a la semana epidemiologica del año 2021, según el inicio de síntomas, 

- 'sin_vac_casos'  indicando el número de casos confirmados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) no ha recibido ninguna dosis de vacuna,

- 'una_dosis_casos' indicando el  número casos confirmados durante la semana epidemiológica correspondiente,  y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido la primera dosis y no la segunda dosis, en un esquema que incluye dos dosis,

- 'dos_dosis_casos' indicando el número de casos confirmados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos)  han recibido dos dosis, en un esquema de que incluye dos dosis, y han transcurrido 14 días o menos desde la segunda dosis,

- 'dos_dosis_comp_casos' indicando el número de casos confirmados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido dos dosis y han transcurrido más de 14 días desde la segunda dosis,

- 'dosis_unica_casos' indicando el número de casos confirmados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o  al momento de la toma de muestra (asintomáticos) han recibido una dosis de una vacuna de un esquema de vacunación que incluye una sola dosis y han transcurrido 14 días o menos desde la vacunación,

- 'dosis_unica_comp_casos' indicando el numero de casos confirmados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o  al momento de la toma de muestra (asintomáticos) han recibido una dosis de una vacuna de un esquema de vacunación que incluye una sola dosis y han transcurrido más de 14 días desde la vacunación,

- 'dosis_ref_comp_casos' indicando el numero de casos confirmados durante la semana epidemiológica correspondiente, y que al iniciar síntomas (sintomáticos) o toma de muestra (asintomáticos) han recibido una dosis de refuerzo a su esquema completo y han transcurrido más de 14 días desde dicha administración,

- 'sin_vac_uci' indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momentro de la toma de muestra (asintomáticos) no ha recibido ninguna dosis de vacuna,

- 'una_dosis_uci' indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido la primera dosis y no la segunda dosis, en un esquema que incluye dos dosis,

- 'dos_dosis_uci' indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos)  han recibido dos dosis, en un esquema de que incluye dos dosis, y han transcurrido 14 días o menos desde la segunda dosis,

- 'dos_dosis_comp_uci'  indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido dos dosis y han transcurrido más de 14 días desde la segunda dosis,

- 'dosis_unica_uci' indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o  al momento de la toma de muestra (asintomáticos) han recibido una dosis de una vacuna de un esquema de vacunación que incluye una sola dosis y han transcurrido 14 días o menos desde la vacunación,

- 'dosis_unica_comp_uci' indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido una dosis de una vacuna de un esquema de vacunación que incluye una sola dosis y han transcurrido más de 14 días desde la vacunación,

- 'dosis_ref_comp_uci' indicando el número de casos confirmados que ingresaron a UCI durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido una dosis de refuerzo a su esquema completo y han transcurrido más de 14 días desde dicha administración,

- 'sin_vac_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momentro de la toma de muestra (asintomáticos) no ha recibido ninguna dosis de vacuna,

- 'una_dosis_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido la primera dosis y no la segunda dosis, en un esquema que incluye dos dosis,

- 'dos_dosis_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos)  han recibido dos dosis, en un esquema de que incluye dos dosis, y han transcurrido 14 días o menos desde la segunda dosis,

- 'dos_dosis_comp_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido dos dosis y han transcurrido más de 14 días desde la segunda dosis,

- 'dosis_unica_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o  al momento de la toma de muestra (asintomáticos) han recibido una dosis de una vacuna de un esquema de vacunación que incluye una sola dosis y han transcurrido 14 días o menos desde la vacunación,

- 'dosis_unica_comp_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido dos dosis de una vacuna de un esquema de vacunación que incluye una sola dosis y han transcurrido más de 14 días desde la vacunación,

- 'dosis_ref_comp_fall' indicando el número de casos confirmados que fallecieron de COVID-19 durante la semana epidemiológica correspondiente y que al iniciar síntomas (sintomáticos) o al momento de la toma de muestra (asintomáticos) han recibido una dosis de refuerzo a su esquema completo y han transcurrido más de 14 días desde dicha administración,

Todos estos valores están separados entre sí por comas (csv).

# Fuente
Departamento de Epidemiología, Ministerio de Salud de Chile. 

# Frecuencia de actualización
Asociado a los informes semanales, publicados por el Ministerio de Salud de Chile.

# NOTA ACLARATORIA
Los casos confirmados de SARS-CoV-2 totales, sintomáticos, ingresados a UCI y fallecidos reportados en este informe incorporan las modificaciones señaladas en el Ordinario B51/N°4518 del 15 de noviembre del 2021, lo que podría explicar variaciones en el número de casos por semanas epidemiológicas presentado en versiones previas. La información corresponde a data provisoria, en proceso de validación.

El producto 89 presenta los eventos de casos, ingresos UCI y defunciones, según ocurrencia en la semana de reporte. Estos son consolidados sin una actualización retrospectiva, por lo cual podría presentar diferencias con otros reportes que se emiten en paralelo.

El producto 90 presenta las cifras de casos, ingresos UCI y defunciones según semana de inicio de síntomas, no por  ocurrencia del evento, con actualización retrospectiva semanal, por lo cual podría presentar diferencias con otros reportes que se emiten en paralelo.
 
