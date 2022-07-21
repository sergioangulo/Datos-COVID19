'''
MIT License

Copyright (c) 2021 Ministerio de Ciencia, Conocimiento, Tecnología e Innovación

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

"""
Los productos que salen de este código son:
89
90
"""

from googleapiclient.discovery import build
from utils import *
from shutil import copyfile
from os import listdir
from os.path import isfile, join
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import pickle
import os.path


def prod89(fte, producto):
    df_output_file = pd.read_csv(fte + 'incidencia_estado_vacunacion.csv', encoding = "ISO-8859-1")
    df_output_file.replace('Ã±','ñ', regex=True, inplace = True)
    df_output_file.replace('Â°','°', regex=True, inplace = True)
    df_output_file.replace('Ã¡','á', regex=True, inplace = True)
    df_output_file.replace('Ã­','í', regex=True, inplace = True)

    # df_output_file['incidencia_casos'] = ((df_output_file['casos_confirmados'] / df_output_file['poblacion'] ) * 100000).astype(float)
    # df_output_file['incidencia_uci'] = ((df_output_file['casos_uci'] / df_output_file['poblacion'] ) * 100000).astype(float)
    # df_output_file['incidencia_def'] = ((df_output_file['casos_def'] / df_output_file['poblacion'] ) * 100000).astype(float)
    df_output_file.to_csv(producto, index=False)


def prod90(fte, producto):
    # carga totales para juntar
    totales = pd.read_csv('../output/producto76/vacunacion_t.csv')
    totales = totales[2:]
    totales.set_index('Region',inplace=True)
    totales['personas_con_pauta_completa'] = pd.to_numeric(totales['Total.1']) + pd.to_numeric(totales['Total.2'])
    totales['personas_con_una_dosis'] = pd.to_numeric(totales['Total'])
    totales['personas_con_refuerzo'] = pd.to_numeric(totales['Total.3'])
    totales_pauta_completa = agrupaporSemanaEpi(totales,'personas_con_pauta_completa')
    totales_una_dosis = agrupaporSemanaEpi(totales,'personas_con_una_dosis')
    totales_refuerzo = agrupaporSemanaEpi(totales, 'personas_con_refuerzo')

    #carga input y agrega totales vacunados
    df_output_file = pd.read_csv(fte + 'carga_vacunacion_sem_epi.csv',index_col='semana_epidemiologica')
    df_output_file = pd.concat([df_output_file, totales_una_dosis], axis=1, join="inner")
    df_output_file = pd.concat([df_output_file, totales_pauta_completa], axis=1, join="inner")
    df_output_file = pd.concat([df_output_file, totales_refuerzo], axis=1, join="inner")
    df_output_file.to_csv(producto, index=True, sep=',')


def agrupaporSemanaEpi(producto,serie):
    df = producto
    df['semana_epidemiologica'] = pd.to_datetime(df.index)
    df['semana_epidemiologica'] = df['semana_epidemiologica'].dt.strftime('%Y-%W')
    df['semana_epidemiologica'].replace('2021-00', '2020-52', inplace=True)
    df['semana_epidemiologica'].replace('2022-00', '2021-52', inplace=True)
    try:
        output = df.groupby(['semana_epidemiologica'])['semana_epidemiologica',serie].max()
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    output.set_index('semana_epidemiologica', inplace=True)
    return output


if __name__ == '__main__':
    print('Generando producto 89 por grupo etario')
    prod89('../input/Vacunacion/', '../output/producto89/incidencia_en_vacunados_edad.csv')

    print('Generando producto 90 incidencia en vacunandos')
    prod90('../input/Vacunacion/', '../output/producto90/incidencia_en_vacunados.csv')

