# MODELO PARA ESTIMAR EXCESO DE MORTALIDAD ELABORADO EN DEIS CON BASE DE DEFUNCIONES (DATOS ABIERTOS) DISPONIBLE EN: https://deis.minsal.cl/

# El modelo ajusta por tendencia y estacionalidad utilizando media armónica.
# Para hacer comparables los años se eliminó la semana 53
# Para hacer comparables las semanas incompletas se aplicó una ponderación al valor observado para esa semana
# Para el análisis se excluye región "Ignorada", sexo "Indeterminado" y edad "999"
# Grupos con estimaciones similares:
# COVID-19 Excess Mortality Collaborators: https://www.thelancet.com/article/S0140-6736(21)02796-3/fulltext
# Technical Advisory Group (TAG) on COVID-19 Mortality Assessment: https://www.who.int/data/sets/global-excess-deaths-associated-with-covid-19-modelled-estimates
# Ariel Karlinsky and Dmitry Kobak (2021): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8331176/
# The Economist: https://www.economist.com/graphic-detail/coronavirus-excess-deaths-tracker

library(readr)
library(dplyr)
library(tidyr)
library(lubridate)
library(MASS)
library(mgcv)
library(ggplot2)
library(visreg)
library(httr)
png("../output/producto96/Exceso_Mortalidad.png")


# Descargar información directamente desde DatosAbiertos DEIS
for (x in 0:7) {
  fecha <- Sys.Date() - x
  fecha <- paste( sprintf("%02d", day(fecha)), sprintf("%02d", month(fecha)),year(fecha), sep="")
  print("Intentando fecha:")
  print(fecha)
  r <- GET(paste("https://repositoriodeis.minsal.cl/DatosAbiertos/VITALES/DEFUNCIONES_FUENTE_DEIS_2016_2022_", fecha, ".zip", sep=""))
  if(r$status_code == 200) {
     print("Se encontró información")
     archivo <- paste("DEFUNCIONES_FUENTE_DEIS_2016_2022_", fecha, ".csv", sep="")
     break
  }
}

# Descomprimir archivos
bin <- content(r, "raw")
writeBin(bin, "DEFUNCIONES_FUENTE_DEIS.zip")
unzip("DEFUNCIONES_FUENTE_DEIS.zip")

file.copy(from = archivo,
          to   = "DEFUNCIONES_FUENTE_DEIS.csv")
file.remove(archivo)
file.remove("DEFUNCIONES_FUENTE_DEIS.zip")

if(file.exists("Diccionario de Datos BBDD-COVID19 liberada.xlsx")){
   file.remove("Diccionario de Datos BBDD-COVID19 liberada.xlsx")
}


def_nac <- read.csv("DEFUNCIONES_FUENTE_DEIS.csv", header=FALSE, sep=";")
file.remove("DEFUNCIONES_FUENTE_DEIS.csv")

def_nac <- def_nac[complete.cases(def_nac), ]

def_nac <- def_nac %>%
  rename(fecha = V2,
         sexo = V3,
         edad= V5,
         region = V8,
         cie = V16, 
         lugar =V27)

def_nac <- def_nac[(def_nac$region != "Ignorada"),]
def_nac <- subset(def_nac, sexo != "Indeterminado")
def_nac <- subset(def_nac, edad != "999")

def_nac$fecha <- ymd(def_nac$fecha)
def_nac$semana <- epiweek(def_nac$fecha)
def_nac$año <- year(def_nac$fecha)

def_nac$defunciones <- 1

descripcion <- def_nac %>% 
  group_by(año) %>%
  summarise(conteo = sum(defunciones)) 

# Crear base de datos para todas las defunciones

def_nac.ag <- def_nac %>% 
  complete(año, semana, fill = list(defunciones = 0)) %>% 
  group_by(año, semana) %>%
  summarise(conteo = sum(defunciones))

def_nac.ag <- def_nac.ag[(def_nac.ag$semana != 53),] # Elimitar la semana 53 del registro

def_nac.ag$t <- rep(c(1:(length(def_nac.ag$semana)))) # Crear variable para tendencia secular

def_nac.ag <- def_nac.ag[!(def_nac.ag$t %in% c(338:364)),] # Eliminar período con registro incompleto para el año 2022

# Crear serie COVID

def_covid <- subset(def_nac, cie == "U071" | cie == "U072") # Seleccionar casos COVID

def_covid_nac.ag <- def_covid %>% 
  complete(año, semana, fill = list(defunciones = 0)) %>% 
  group_by(año, semana) %>%
  summarise(conteo = sum(defunciones))

descripcion_covid <- def_covid %>% 
  summarise(conteo = sum(defunciones)) 

def_covid_nac.ag <- def_covid_nac.ag[(def_covid_nac.ag$semana != 53),]

def_nac.ag <- merge(x = def_nac.ag, y = def_covid_nac.ag, by = c("año", "semana"), all.x = TRUE) # Juntar conteo de defunciones totales y defunciones por COVID

def_nac.ag <- def_nac.ag %>%
  rename(defunciones = conteo.x,
         covid = conteo.y)

# Crear ponderador para semanas incompletas

def_nac.ag$ponderador <- 1

def_nac.ag <- def_nac.ag %>%
  mutate(ponderador = ifelse(año == 2018 & semana == 1, 6/7, ponderador),
         ponderador = ifelse(año == 2020 & semana == 1, 4/7, ponderador),
         ponderador = ifelse(año == 2021 & semana == 52, 6/7, ponderador))

def_nac.ag$defunciones <- round(def_nac.ag$defunciones/def_nac.ag$ponderador, digits = 0)
def_nac.ag$covid <- round(def_nac.ag$covid/def_nac.ag$ponderador, digits = 0)

# Análisis de exceso de mortalidad usando modelo GLM con tendencia secular y estacionalidad usando media armónica ####

def_nac.ag_glm <- def_nac.ag %>% 
  group_by(año, semana, t) %>%
  summarise(conteo = sum(defunciones), covid = sum(covid)) 

def_nac.ag_proy <- def_nac.ag_glm[def_nac.ag_glm$t <209,] # Crear base de datos para proyectar los casos

proyeccion_def.ag_glm <- glm.nb(conteo ~ t + sin(2*pi*semana/52) + cos(2*pi*semana/52) + sin(2*pi*semana/(52/2)) + cos(2*pi*semana/(52/2)), data = def_nac.ag_proy) # modelo que ajusta tendencia y estacionalidad

conteo_proyectado_glm <- predict.glm(proyeccion_def.ag_glm, newdata = def_nac.ag_glm, type = "response", se.fit = TRUE) # Proyección de modelo usando base de datos de entrenamiento a la base general

def_nac.ag_glm$fit_glm <- conteo_proyectado_glm$fit # Cálculo de valores proyectados y sus IC
def_nac.ag_glm$se_glm <- conteo_proyectado_glm$se.fit
def_nac.ag_glm$pred_lb_glm <- def_nac.ag_glm$fit_glm - 1.96*def_nac.ag_glm$se_glm
def_nac.ag_glm$pred_ub_glm <- def_nac.ag_glm$fit_glm + 1.96*def_nac.ag_glm$se_glm
def_nac.ag_glm$covid <- def_nac.ag_glm$fit_glm + def_nac.ag_glm$covid

def_nac.ag_glm1 <- def_nac.ag_glm[def_nac.ag_glm$t >=209,] # Selección de años 2020 a 2022
def_nac.ag_glm1$fecha <- seq(ymd('2020-01-02'),ymd('2022-06-19'), by= 'weeks')  # Se genera secuencia temporal para el período

ggplot(data = def_nac.ag_glm1, aes(x = fecha, y = conteo)) +
  geom_point() +
  geom_line(aes(x = fecha, y = covid), linetype = "dashed", color = "red") +
  geom_line(aes(x = fecha, y = fit_glm), linetype = "dashed", color = "blue", alpha = 0.3) +
  labs(title = "Exceso de mortalidad para todos los grupos de edad. Chile, 2020-2022", subtitle = "Defunciones estimadas para el período en línea punteada azul, defunciones observadas en puntos negros y defunciones por COVID-19 (U07.1 y U07.2) por sobre defunciones esperadas en línea roja") +
  geom_vline(xintercept = ymd('2020-03-12')) +
  geom_ribbon(aes(ymin = pred_lb_glm, ymax = pred_ub_glm), alpha = .15) +
  scale_x_date(date_breaks="3 month", date_labels = "%b %Y") +
  xlab("Semana epidemiológica") +
  ylab("N° de defunciones semanales") +
  theme_classic() +
  theme(plot.title = element_text(hjust = 0.5),
        plot.subtitle = element_text(hjust = 0.5),
        axis.title = element_text(size = 10),
        axis.text = element_text(size = 10),
        strip.text = element_text(size = 15))

# Análisis de exceso de mortalidad

def_nac.ag_exc <- subset(def_nac.ag_glm, t >= 220) # Crear base de datos con datos de marzo del 2020 en adelante

def_nac.ag_exc$exceso_mortalidad_glm <- round(def_nac.ag_exc$conteo - def_nac.ag_exc$fit_glm, digits = 0) # Calcular exceso de mortalidad (observado - estimado)
def_nac.ag_exc$exceso_mortalidad_lb_glm <- round(def_nac.ag_exc$conteo - def_nac.ag_exc$pred_ub_glm, digits = 0) # Calcular límite inferior del exceso de mortalidad
def_nac.ag_exc$exceso_mortalidad_ub_glm <- round(def_nac.ag_exc$conteo - def_nac.ag_exc$pred_lb_glm, digits = 0) # Calcular límite superior del exceso de mortalidad
def_nac.ag_exc$covid <- round(def_nac.ag_exc$covid - def_nac.ag_exc$fit_glm, digits = 0) # Calcular mortalidad por COVID
def_nac.ag_exc$porcentaje <- round((def_nac.ag_exc$conteo/def_nac.ag_exc$fit_glm - 1) * 100, digits = 1)

sum(def_nac.ag_exc$exceso_mortalidad_glm) # Exceso de mortalidad
sum(def_nac.ag_exc$exceso_mortalidad_lb_glm) 
sum(def_nac.ag_exc$exceso_mortalidad_ub_glm)
sum(def_nac.ag_exc$covid)

# Crear tabla
if(file.exists("../output/producto96/Exceso_Mortalidad.csv")){
   file.remove("../output/producto96/Exceso_Mortalidad.csv")
}
if(file.exists("../output/producto96/Exceso_Mortalidad_T.csv")){
   file.remove("../output/producto96/Exceso_Mortalidad_T.csv")
}

file.create("../output/producto96/Exceso_Mortalidad.csv")
file.create("../output/producto96/Exceso_Mortalidad_T.csv")

write.csv(def_nac.ag_exc, file = "../output/producto96/Exceso_Mortalidad.csv", row.names = FALSE)

transpuesta <- data.frame(t(def_nac.ag_exc))
colnames(transpuesta) <- paste(transpuesta[1, ], "-" , transpuesta[2, ], sep="")
write.csv(transpuesta, file = "../output/producto96/Exceso_Mortalidad_T.csv")
