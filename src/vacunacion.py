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
import sys

import boto3
import pandas as pd
from utils import *

class vacunacion:
    def __init__(self, input, output):
        self.input = input
        self.output = output


    def get_last(self):

        self.last_added = pd.read_csv('https://raw.githubusercontent.com/juancri/covid19-vaccination/master/output/chile-vaccination.csv')
        #print('last added file is: ' + self.last_added.max(axis=0))



    def last_to_csv(self):

        self.last_added.rename(columns={'Dose': 'Dosis'}, inplace=True)
        regionName(self.last_added)

        self.last_added["Dosis"] = self.last_added["Dosis"].replace({"First": "Primera",
                                             "Second": "Segunda"
                                             })

        identifiers = ['Region','Dosis']
        variables = [x for x in self.last_added.columns if x not in identifiers]

        self.last_added = self.last_added[identifiers + variables]
        self.last_added.to_csv(self.output + '.csv', index=False)

        df_t = self.last_added.T
        df_t.to_csv(self.output + '_t.csv', header=False)

        df_std = pd.melt(self.last_added, id_vars=identifiers, value_vars=variables, var_name=['Fecha'],
                         value_name='Cantidad')

        df_std.to_csv(self.output + '_std.csv', index=False)

if __name__ == '__main__':

    my_vacunas = vacunacion('https://raw.githubusercontent.com/juancri/covid19-vaccination/master/output/chile-vaccination.csv','../output/producto76/vacunacion')
    my_vacunas.get_last()
    my_vacunas.last_to_csv()

