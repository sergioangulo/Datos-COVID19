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
from datetime import datetime

'''
1.- RM, con archivos xlsx, cada uno corresponde a una particula, y el archivo tiene un tab por año.
2.- gases para estaciones fuera de santiago
Dado el volumen (un dato por hora) y complejidad de los datos, la primera separacion sera por años.

'''

import pandas as pd
import sys
import glob
import requests


def prod43_no_header(fte, prod, year='2020'):
    print('Generando producto 43')
    particles = ['CO', 'MP2.5', 'MP10', 'NO2', 'O3', 'SO2']
    # particles = ['SO2']
    for each_particle in particles:
        input_path = fte + each_particle
        print('Processing ' + each_particle + ' from  ' + input_path + ' for year ' + year)
        xlsx_file = glob.glob(input_path + '/' + each_particle + '-' + year + '*.xlsx')
        # fail if there's no file or more than one per year
        if len(xlsx_file) > 1:
            print('Got more than one file for ' + year + ' no processing')

        elif len(xlsx_file) == 0:
            print('No files for ' + year + ' no processing')

        # otherwise process
        elif len(xlsx_file) == 1:
            print(xlsx_file[0])
            # encontramos solo un archivo para el año
            df = pd.read_excel(xlsx_file[0], header=None)

            # separamos header y datos

            # Asumo que despues de UTM_Norte vienen fechas
            last_header_row = df.index[df[0] == 'UTM_Norte'].tolist()[0]
            print('Data starts after row ' + str(last_header_row))
            # en header boto date y time, por eso el slice cuenta desde la columna 2
            header = df.loc[:last_header_row, :]
            header.at[0, 0] = 'Nombre de estacion'
            header.at[2, 0] = 'Codigo region'
            header.at[3, 0] = 'Comuna'
            header.at[4, 0] = 'Codigo comuna'
            # print(header.to_string())

            # guardamos la data
            data = df.loc[last_header_row + 1:, :]
            data = data[data[0].notna()]
            # print(data.head().to_string())
            data[0].replace(to_replace=' 00:00:00', value='', inplace=True, regex=True)
            data[1].replace(to_replace='24:00:00', value='00:00:00', inplace=True, regex=True)
            data[0] = data[0].astype(str)
            data[0] = data[0] + ' ' + data[1]
            # print(data.head().to_string())

            # En header y data podemos botar 1
            header = header.drop(columns=[1])
            data = data.drop(columns=[1])
            # print(header.to_string())

            # print(data.head().to_string())

            df = pd.concat([header, data])

            print(df.head(10).to_string())
            df.to_csv(prod + each_particle + '-' + year + '_std.csv', index=False, header=False)


def prod43_from_mma_api(usr, password, auth_url, url, prod):
    '''
    Cosultamos la API por semana, y nos traemos la ultima semana.
    '''
    print('Querying MMA API for daily update of product 43')
    # usr and pass must be retrieve from github secrets
    # auth_url returns a cookie that must be passed then for the query
    data = {
        'username': usr,
        'password': password
    }
    s = requests.Session()
    cookie = s.post(auth_url, data=data)
    cookie = cookie.json()['data']['authenticator']
    # get list of stations and metadata to build queries
    estaciones = pd.read_csv('../input/MMA/Estaciones.csv')
    estaciones = estaciones[estaciones['Key'].notna()]
    print(estaciones.to_string())
    # la consulta es asi: https://sinca.mma.gob.cl/api/domain/SMA/timeserie/117+MPM25VAL
    # SSSRTPPPPLLL, donde:
    # SSS : Estación (código Airviro)
    # R : resolución de tiempo (código Airviro) + es hora, * es dia
    # T : tipo (v: crudo M: validado)
    # PPPP : parámetro (código Airviro)
    # LLL: Instancia, variación de serie de tiempo. Por ejemplo en las meteorológicas se usa para la altura. Pero sirve para diferenciar series de tiempo según se requiera
    particulas = {'MP10': 'MPM10',
                  'MP2.5': 'MPM25'
                  }
    for each_particula in particulas:
        data_particula = []
        for index in estaciones.index:
            print("Querying " + estaciones.loc[index, 'Nombre estacion'])
            api_call = url + '/' + estaciones.loc[index, 'Key'] + '+' + particulas[each_particula] + 'VAL'
            print(api_call)
            response = s.get(api_call)
            if response.status_code == 200:
                print(response.json()['data']['sampleQueries']['links']['lastMonth'])
                # for k in response.json():
                #     print(k)
                #     for l in response.json()[k]:
                #         print('\t' + l)
                proper_data = response.json()['data']['sampleQueries']['links']['lastMonth'] + '/ds61'
                proper_data = s.get(proper_data)
                # print(proper_data.json()['data']['timeserie'])
                # header from local metadata:
                header = {'Nombre de estacion': estaciones.loc[index, 'Nombre estacion'],
                          'Region': estaciones.loc[index, 'Region'],
                          'Region': estaciones.loc[index, 'Region']

                          }
                # put the json above in a dataframe
                data = pd.DataFrame(proper_data.json()['data']['timeserie'])
                print(data.to_string())


            else:
                print('Instead of a status code 200, we got ' + str(response.status_code))
        # read the file

        # append to the file



if __name__ == '__main__':
    history = False
    if history:
        for i in range(2010, 2020):
            prod43_no_header('../input/MMA/', '../output/producto43/', year=str(i))

    else:
        #prod43_no_header('../input/MMA/', '../output/producto43/')
        if len(sys.argv) == 3:
            auth_url ='https://sinca.mma.gob.cl/api/auth.cgi'
            url = 'https://sinca.mma.gob.cl/api/domain/SMA/timeserie'
            prod43_from_mma_api(sys.argv[1], sys.argv[2], auth_url, url, 'test.lala')
