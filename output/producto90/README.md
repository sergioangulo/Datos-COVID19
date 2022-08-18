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


