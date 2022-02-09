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