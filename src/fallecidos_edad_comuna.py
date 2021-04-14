'''
MIT License

Copyright (c) 2020 Minciencia

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
import requests
import utils
import pandas as pd
import datetime as dt
import numpy as np
from itertools import groupby


class p84:
    def __init__(self,output):
        self.output = output
        self.path = '../input/DistribucionDEIS'

    def get_last(self):
        self.last_added = pd.read_csv('../input/DistribucionDEIS/df_deis_edad.csv')

    def last_to_csv(self):
        df_base = pd.read_csv('../input/DistribucionDEIS/baseFiles/DEIS_template.csv')
        df_base['Codigo region'] = df_base['Codigo region'].fillna(0)
        df_base['Codigo comuna'] = df_base['Codigo comuna'].fillna(0)
        todrop = df_base.loc[df_base['Comuna'] == 0]
        df_base['Comuna'] = df_base['Comuna'].fillna(0)
        df_base.drop(todrop.index, inplace=True)
        df_base['Codigo region'] = df_base['Codigo region'].astype(int)
        df_base['Codigo comuna'] = df_base['Codigo comuna'].astype(int)

        desconocido = df_base['Codigo comuna'] != 0
        df_base['Codigo comuna'].where(desconocido, '', inplace=True)

        Comp = df_base.loc[df_base['Comuna'] != 'Total']
        Comp.reset_index(inplace=True)
        utils.desconocidoName(Comp)
        for k in range(len(Comp)):
            if Comp.loc[k, 'Codigo region'] < 10:
                Comp.loc[k, 'Codigo region'] = '0' + str(Comp.loc[k, 'Codigo region'])
            else:
                Comp.loc[k, 'Codigo region'] = str(Comp.loc[k, 'Codigo region'])

            if Comp.loc[k, 'Codigo comuna'] != '':
                if Comp.loc[k, 'Codigo comuna'] < 10000:
                    Comp.loc[k, 'Codigo comuna'] = '0' + str(Comp.loc[k, 'Codigo comuna'])
                else:
                    Comp.loc[k, 'Codigo comuna'] = str(Comp.loc[k, 'Codigo comuna'])

        comuna = Comp['Comuna']

        self.last_added = self.last_added.dropna(subset=['Fecha defunciones'])
        self.last_added.sort_values(by=['region_residencia','comuna_residencia','edad'], inplace=True)
        self.last_added.rename(columns={'comuna_residencia': 'comuna'}, inplace=True)
        self.last_added.rename(columns={'region_residencia': 'Region'}, inplace=True)
        self.last_added = utils.normalizaNombreCodigoRegionYComuna(self.last_added)
        df_sup = Comp[['Codigo comuna', 'Comuna']]
        df_sup['Codigo comuna'] = df_sup['Codigo comuna'].replace('', 0)
        self.last_added.drop(columns={'Comuna'}, inplace=True)
        for k in range(len(self.last_added)):
            if self.last_added.loc[k, 'Codigo comuna'] != '':
                if self.last_added.loc[k, 'Codigo comuna'] < 10000:
                    self.last_added.loc[k, 'Codigo comuna'] = '0' + str(self.last_added.loc[k, 'Codigo comuna'])
                else:
                    self.last_added.loc[k, 'Codigo comuna'] = str(self.last_added.loc[k, 'Codigo comuna'])
        self.last_added = self.last_added.merge(df_sup, on="Codigo comuna", how="left")
        self.last_added.set_index('Comuna', inplace=True)

        columns_name = self.last_added.columns.values

        maxSE = self.last_added[columns_name[4]].max()
        minSE = self.last_added[columns_name[4]].min()

        print(minSE, maxSE)
        lenSE = (pd.to_datetime(maxSE) - pd.to_datetime(minSE)).days + 1
        startdate = pd.to_datetime(minSE)
        date_list = pd.date_range(startdate, periods=lenSE).tolist()
        date_list = [dt.datetime.strftime(x, "%Y-%m-%d") for x in date_list]
        print(date_list)

        #vector con las variables
        SE_comuna = self.last_added[columns_name[4]]


        for edad in ['-39','40-49','50-59','60-69','70-79','80-89','90-']:
            if edad == '-39':
                df_edad = self.last_added[self.last_added['edad'] <= 39]
            if edad == '40-49':
                df_edad = self.last_added[self.last_added['edad'] <= 49]
                df_edad = df_edad[df_edad['edad'] >= 40]
            if edad == '50-59':
                df_edad = self.last_added[self.last_added['edad'] <= 59]
                df_edad = df_edad[df_edad['edad'] >= 50]
            if edad == '60-69':
                df_edad = self.last_added[self.last_added['edad'] <= 69]
                df_edad = df_edad[df_edad['edad'] >= 60]
            if edad == '70-79':
                df_edad = self.last_added[self.last_added['edad'] <= 79]
                df_edad = df_edad[df_edad['edad'] >= 70]
            if edad == '80-89':
                df_edad = self.last_added[self.last_added['edad'] <= 89]
                df_edad = df_edad[df_edad['edad'] >= 80]
            if edad == '90-':
                df_edad = self.last_added[self.last_added['edad'] >= 90]

            for k in [5,6,7]:
                df = pd.DataFrame(np.zeros((len(comuna), lenSE)))

                dicts = {}
                keys = range(lenSE)
                # values = [i for i in range(lenSE)]

                for i in keys:
                    dicts[i] = date_list[i]

                df.rename(columns=dicts, inplace=True)
                value_comuna = df_edad[columns_name[k]]
                value_comuna.fillna(0,inplace=True)
                i=0
                for row in df_edad.index:
                    idx = comuna.loc[comuna == row].index.values
                    if idx.size > 0:
                        col = SE_comuna[i]
                        df[col][idx] = value_comuna[i].astype(int)

                    i += 1


                df_output = pd.concat([Comp, df], axis=1)
                df_output.drop(columns=['index'], axis=1, inplace=True)

                nComunas = [len(list(group)) for key, group in groupby(df_output['Codigo region'])]

                identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna']
                variables = [x for x in df_output.columns if x not in identifiers]

                begRow = 0

                for i in range(len(nComunas)):

                    endRow = begRow + nComunas[i]

                    firstList = df_output[identifiers].iloc[endRow - 1].values.tolist()
                    firstList[2] = 'Total'
                    firstList[3] = ''

                    valuesTotal = df_output[variables][begRow:endRow].sum(axis=0).tolist()

                    regionTotal = pd.DataFrame((firstList + valuesTotal), index=df_output.columns.values).transpose()

                    if i < len(nComunas) - 1:
                        blank_line = pd.Series(np.empty((len(regionTotal), 0)).tolist())

                        regionTotal = pd.concat([regionTotal, blank_line], axis=0)
                        regionTotal.drop(columns=0, axis=1, inplace=True)

                    temp = pd.concat([df_output.iloc[begRow:endRow], regionTotal], axis=0)
                    if i == 0:
                        outputDF2 = temp
                    else:
                        outputDF2 = pd.concat([outputDF2, temp], axis=0)

                    if i < len(nComunas) - 1:
                        begRow = endRow

                    outputDF2.reset_index(inplace=True)
                    outputDF2.drop(columns=['index'], axis=1, inplace=True)
                    outputDF2[variables] = outputDF2[variables].dropna()  # .astype(int)

                    print(outputDF2.head(20))

                    outputDF2.dropna(how='all', inplace=True)
                    todrop = outputDF2.loc[outputDF2['Comuna'] == 'Total']
                    outputDF2.drop(todrop.index, inplace=True)

                if k == 5:
                    name = self.output + '_'+str(edad)+'_confirmadas.csv'
                    outputDF2.to_csv(name, index=False)
                    outputDF2_T = outputDF2.T
                    outputDF2_T.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna']
                    variables = [x for x in outputDF2.columns if x not in identifiers]
                    outputDF2_std = pd.melt(outputDF2, id_vars=identifiers, value_vars=variables, var_name='Fecha', value_name='Confirmada')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)

                elif k == 6:
                    name = self.output + '_'+str(edad)+'_sospechosas.csv'
                    outputDF2.to_csv(name, index=False)
                    outputDF2_T = outputDF2.T
                    outputDF2_T.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna']
                    variables = [x for x in outputDF2.columns if x not in identifiers]
                    outputDF2_std = pd.melt(outputDF2, id_vars=identifiers, value_vars=variables, var_name='Fecha', value_name='Sospechosa')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)

                elif k == 7:
                    name = self.output + '_'+str(edad)+'_totales.csv'
                    outputDF2.to_csv(name, index=False)
                    outputDF2_T = outputDF2.T
                    outputDF2_T.to_csv(name.replace('.csv', '_T.csv'), header=False)
                    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna']
                    variables = [x for x in outputDF2.columns if x not in identifiers]
                    outputDF2_std = pd.melt(outputDF2, id_vars=identifiers, value_vars=variables, var_name='Fecha', value_name='Total')
                    outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)

if __name__ == '__main__':

    print('Actualizamos fallecidos por edad y comuna')
    my_comunas = p84('../output/producto84/fallecidos_comuna_edad')
    my_comunas.get_last()
    my_comunas.last_to_csv()