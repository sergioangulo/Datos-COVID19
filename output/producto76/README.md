# DP76 - Avance en Campaña de Vacunación COVID-19: Descripción
Este producto da cuenta del avance en la campaña de vacunación contra Sars-Cov-2. Incluye información regional acorde a la residencia reportada y fabricante de la vacuna.

Salvo los archivos vacunacion.csv, el resto han dejado de ser mantenidos en su origen (https://github.com/juancri/covid19-vaccination/issues/34). Pueden obtener la información que entregan de las siguientes fuentes en este repo, que se mantendrán actualizadas:

Fabricante: Por laboratorio que fabrica y ocurrencia de la inoculación https://github.com/MinCiencia/Datos-COVID19/blob/master/output/producto83
Total y avance diario por edad: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto78 
Total por edad y comuna: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto81
Total por edad y región: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto77
Total por grupo prioritario: https://github.com/MinCiencia/Datos-COVID19/tree/master/output/producto79


# Columnas y valores
El archivo vacunacion.csv tiene las columnas 'Region', que indica la ubicación donde se administró la dosis, 'Dosis', que indica si es la primera o la segunda, y la serie de columnas correspondientes a la fecha, que indica la cantidad administrada por día.

El archivo fabricante.csv tiene las columnas 'Fabricante', que indica el fabricantee de la dosis administrada, 'Dosis', que indica si es la primera o la segunda, y la serie de columnas correspondientes a la fecha, que indica la cantidad administrada por día.

# Fuente
Ministerio de Salud. Ver en:
https://informesdeis.minsal.cl/SASVisualAnalytics/

Procesado por Juan Cristobal Olivares
COVID-19 Vaccination (@juancri)

# Frecuencia de actualización
Actualización diaria. 

