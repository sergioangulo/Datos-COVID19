'''
MIT License

Copyright (c) 2020 Sebastian Cornejo

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

'''
1.- RM, con archivos xlsx, cada uno corresponde a una particula, y el archivo tiene un tab por año.
2.-SIVICA, con 2 sub directorios:
 2.1.- meteorologia, con 2 sub directorios:
     2.1.1.- humedad, con 2 archivos: datos crudos y validados
     2.1.2.- temperatura, con 2 archivos: datos crudos y validados
 2.2.- gases para estaciones fuera de santiago
Dado el volumen (un dato por hora) y complejidad de los datos, la primera separacion sera por años.
yo creo que es sensato mantener la separacion entre datos crudos y validados, como un flag o como series separadas.
'''

import pandas as pd
import sys
import glob


def prod43_no_header(fte, prod, year='2019'):
    print('Generando producto 43')
    particles = ['CO', 'MP2.5', 'MP10', 'NO2', 'O3', 'SO2']
    #particles = ['SO2']
    for each_particle in particles:
        input_path = fte + each_particle
        print('Processing ' + each_particle + ' from  ' + input_path + ' for year ' + year)
        xlsx_file = glob.glob(input_path + '/' + each_particle + '-' + year + '*.xlsx')
        # fail if there's no file or more than one per year
        if len(xlsx_file) > 1:
            print('Got more than one file for ' + year)
            return
        elif len(xlsx_file) == 0:
            print('No files for ' + year)
            return
        # otherwise process
        elif len(xlsx_file) == 1:
            print(xlsx_file[0])
            # encontramos solo un archivo para el año
            df = pd.read_excel(xlsx_file[0], header=None)

            #separamos header y datos

            # Asumo que despues de UTM_Norte vienen fechas
            last_header_row = df.index[df[0] == 'UTM_Norte'].tolist()[0]
            print('Data starts after row ' + str(last_header_row))
            #en header boto date y time, por eso el slice cuenta desde la columna 2
            header = df.loc[:last_header_row, :]
            header.at[0, 0] = 'Nombre de estacion'
            header.at[2, 0] = 'Codigo region'
            header.at[3, 0] = 'Comuna'
            header.at[4, 0] = 'Codigo comuna'
            #print(header.to_string())

            # guardamos la data
            data = df.loc[last_header_row + 1:, :]
            data = data[data[0].notna()]
            #print(data.head().to_string())
            data[0].replace(to_replace=' 00:00:00', value='', inplace=True, regex=True)
            data[1].replace(to_replace='24:00:00', value='00:00:00', inplace=True, regex=True)
            data[0] = data[0].astype(str)
            data[0] = data[0] + ' ' + data[1]
            #print(data.head().to_string())

            # En header y data podemos botar 1
            header = header.drop(columns=[1])
            data = data.drop(columns=[1])
            #print(header.to_string())

            #print(data.head().to_string())

            df = pd.concat([header, data])

            print(df.head(10).to_string())
            df.to_csv(prod + each_particle + '-' + year + '_std.csv', index=False, header=False)


def prod43_header(fte,prod):
    print('Reading with headers')

    # df = pd.read_excel(xlsx_file[0], header=[0, 1, 2, 3, 4, 5, 6])
    # print(df.columns[0][3])
    # df.rename(columns={'date': 'Nombre estacion',
    #                    'Codigo_comuna': 'Comuna'}
    #           , inplace=True)
    # #region esta repetido :(
    # level4 = df.columns.get_level_values(4).tolist()
    # index = level4.index('Region')
    # level4[index] = 'Codigo comuna'
    # df.columns.set_levels(level4, level=4, inplace=True)
    # print(df.head().to_string())

    # df.columns = df.columns.set_levels(['Comuna'], level=3)


    # print(df.columns)
    # print(df['Region']['Codigo_region']['Codigo_comuna']['Region'])

    # identificamos donde se acaban los headers para poder concatenar las fechas

if __name__ == '__main__':
    history = True
    if history:
        for i in range(2010, 2020):
            prod43_no_header('../input/MMA/', '../output/producto43/', year=str(i))

    else:
        prod43_no_header('../input/MMA/', '../output/producto43/')