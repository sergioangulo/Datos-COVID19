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
El producto 89 presenta los eventos de casos, ingresos UCI y defunciones, según ocurrencia en la semana de reporte. Estos son consolidados sin una actualización retrospectiva, por lo cual podría presentar diferencias con otros reportes que se emiten en paralelo.

El producto 90 presenta las cifras de casos, ingresos UCI y defunciones según semana de inicio de síntomas, no por  ocurrencia del evento, con actualización retrospectiva semanal, por lo cual podría presentar diferencias con otros reportes que se emiten en paralelo.

Los casos confirmados de SARS-CoV-2 totales, sintomáticos, ingresados hospitalizaión, ingreso a UCI y fallecidos reportados en este informe incorporan las modificaciones señaladas en el Ordinario B51/N°4518 del 15 de noviembre del 2021, lo que podría explicar variaciones en el número de casos por semanas epidemiológicas presentado en versiones previas. La información corresponde a data provisoria,en proceso de validación.


