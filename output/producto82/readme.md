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
- **paso:** etapa del plan paso a paso en la que se encontró la comuna durante la mayor parte de la semana (sólo producto 16).

## Más información en:

- [https://covidanalytics.isci.cl/movilidad/visor-movilidad/](https://covidanalytics.isci.cl/movilidad/visor-movilidad/)
- [https://covidanalytics.isci.cl/movilidad/reportes/](https://covidanalytics.isci.cl/movilidad/reportes/)
- [https://isci.cl/wp-content/uploads/2020/06/Social-Cuarentenas-v6-ISCI.pdf](https://isci.cl/wp-content/uploads/2020/06/Social-Cuarentenas-v6-ISCI.pdf)
