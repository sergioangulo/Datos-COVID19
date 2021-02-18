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
import requests
from utils import *

class vacunacion:
    def __init__(self, input, output,indicador):
        self.input = input
        self.output = output
        self.indicador = indicador
        self.my_files = {
            'vacunacion_fabricante':
                'https://raw.githubusercontent.com/juancri/covid19-vaccination/master/output/chile-vaccination-type.csv',
            'vacunacion_region':
                'https://raw.githubusercontent.com/juancri/covid19-vaccination/master/output/chile-vaccination.csv',
            'vacunacion_edad':
                'https://github.com/juancri/covid19-vaccination/raw/master/output/chile-vaccination-ages.csv',
            'vacunacion_grupo':
                'https://github.com/juancri/covid19-vaccination/raw/master/output/chile-vaccination-groups.csv',
        }
        self.path = '../input/Vacunacion'

    def get_last(self):

        ## selecciona el archivo que corresponde
        if self.indicador == 'fabricante':
            print('Retrieving files')
            print('vacunacion_fabricante')
            r = requests.get(self.my_files['vacunacion_fabricante'])
            content = r.content
            csv_file = open(self.path + '/' + 'vacunacion_fabricante' + '.csv', 'wb')
            csv_file.write(content)
            csv_file.close()
            self.last_added = pd.read_csv('../input/Vacunacion/vacunacion_fabricante.csv')

        elif self.indicador == 'campana':
            print('Retrieving files')
            print('vacunacion_region')
            r = requests.get(self.my_files['vacunacion_region'])
            content = r.content
            csv_file = open(self.path + '/' + 'vacunacion_region' + '.csv', 'wb')
            csv_file.write(content)
            csv_file.close()
            self.last_added = pd.read_csv('../input/Vacunacion/vacunacion_region.csv')

        elif self.indicador == 'edad':
            print('Retrieving files')
            print('vacunacion_edad')
            r = requests.get(self.my_files['vacunacion_edad'])
            content = r.content
            csv_file = open(self.path + '/' + 'vacunacion_edad' + '.csv', 'wb')
            csv_file.write(content)
            csv_file.close()
            self.last_added = pd.read_csv('../input/Vacunacion/vacunacion_edad.csv')

        elif self.indicador == 'caracteristicas_del_vacunado':
            print('Retrieving files')
            print('vacunacion_grupo')
            r = requests.get(self.my_files['vacunacion_grupo'])
            content = r.content
            csv_file = open(self.path + '/' + 'vacunacion_grupo' + '.csv', 'wb')
            csv_file.write(content)
            csv_file.close()
            self.last_added = pd.read_csv('../input/Vacunacion/vacunacion_grupo.csv')

    def last_to_csv(self):
        if self.indicador == 'fabricante':
            ## campana por fabricante

            self.last_added.rename(columns={'Dose': 'Dosis'}, inplace=True)
            self.last_added.rename(columns={'Type': 'Fabricante'}, inplace=True)

            self.last_added["Dosis"] = self.last_added["Dosis"].replace({"First": "Primera",
                                                                         "Second": "Segunda"
                                                                         })

            identifiers = ['Fabricante', 'Dosis']
            variables = [x for x in self.last_added.columns if x not in identifiers]

            self.last_added = self.last_added[identifiers + variables]
            self.last_added.to_csv(self.output + '.csv', index=False)

            df_t = self.last_added.T
            df_t.to_csv(self.output + '_t.csv', header=False)

            df_std = pd.melt(self.last_added, id_vars=identifiers, value_vars=variables, var_name=['Fecha'],
                             value_name='Cantidad')

            df_std.to_csv(self.output + '_std.csv', index=False)

        elif self.indicador == 'campana':
            ## campana por region

            self.last_added.rename(columns={'Dose': 'Dosis'}, inplace=True)
            regionName(self.last_added)

            self.last_added["Dosis"] = self.last_added["Dosis"].replace({"First": "Primera",
                                                                         "Second": "Segunda"
                                                                         })

            identifiers = ['Region', 'Dosis']
            variables = [x for x in self.last_added.columns if x not in identifiers]

            self.last_added = self.last_added[identifiers + variables]
            self.last_added.to_csv(self.output + '.csv', index=False)

            df_t = self.last_added.T
            df_t.to_csv(self.output + '_t.csv', header=False)

            df_std = pd.melt(self.last_added, id_vars=identifiers, value_vars=variables, var_name=['Fecha'],
                             value_name='Cantidad')

            df_std.to_csv(self.output + '_std.csv', index=False)

        elif self.indicador == 'edad':
            ## campana por edad

            self.last_added.rename(columns={'Dose': 'Dosis',
                                            'Age':'Rango_etario'}, inplace=True)

            self.last_added["Dosis"] = self.last_added["Dosis"].replace({"First": "Primera",
                                                                         "Second": "Segunda"
                                                                         })

            identifiers = ['Rango_etario', 'Dosis']
            variables = [x for x in self.last_added.columns if x not in identifiers]

            self.last_added = self.last_added[identifiers + variables]
            self.last_added.to_csv(self.output + '.csv', index=False)

            df_t = self.last_added.T
            df_t.to_csv(self.output + '_t.csv', header=False)

            df_std = pd.melt(self.last_added, id_vars=identifiers, value_vars=variables, var_name=['Fecha'],
                             value_name='Cantidad')

            df_std.to_csv(self.output + '_std.csv', index=False)

        elif self.indicador == 'caracteristicas_del_vacunado':
            ## campana por caracter del vacunado

            self.last_added.rename(columns={'Dose': 'Dosis',
                                            'Group':'Grupo'}, inplace=True)

            self.last_added["Dosis"] = self.last_added["Dosis"].replace({"First": "Primera",
                                                                         "Second": "Segunda"
                                                                         })

            identifiers = ['Grupo', 'Dosis']
            variables = [x for x in self.last_added.columns if x not in identifiers]

            self.last_added = self.last_added[identifiers + variables]
            self.last_added.to_csv(self.output + '.csv', index=False)

            df_t = self.last_added.T
            df_t.to_csv(self.output + '_t.csv', header=False)

            df_std = pd.melt(self.last_added, id_vars=identifiers, value_vars=variables, var_name=['Fecha'],
                             value_name='Cantidad')

            df_std.to_csv(self.output + '_std.csv', index=False)

if __name__ == '__main__':
    print('Actualizamos campana de vacunacion')
    my_vacunas = vacunacion('https://raw.githubusercontent.com/juancri/covid19-vaccination/master/output/chile-vaccination.csv','../output/producto76/vacunacion','campana')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()

    print('Actualizamos dosis por fabricante')
    my_vacunas = vacunacion('https://raw.githubusercontent.com/juancri/covid19-vaccination/master/output/chile-vaccination.csv','../output/producto76/fabricante','fabricante')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()

    print('Actualizamos dosis por edad')
    my_vacunas = vacunacion('https://raw.githubusercontent.com/juancri/covid19-vaccination/master/output/chile-vaccination.csv','../output/producto76/rango_etario','edad')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()

    print('Actualizamos dosis por caracteristicas_del_vacunado')
    my_vacunas = vacunacion('https://raw.githubusercontent.com/juancri/covid19-vaccination/master/output/chile-vaccination.csv','../output/producto76/grupo','caracteristicas_del_vacunado')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()