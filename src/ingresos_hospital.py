'''
MIT License

Copyright (c) 2021 Minciencia

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

class IngresosHospital_local:
    def __init__(self, bucket, folder, access_key, secret_key, output):
        self.bucket = bucket
        self.folder = folder
        self.access_key = access_key
        self.secret_key = secret_key


        # store used variables
        self.output = output
        self.last_added = None
        self.date = None
        self.tables = None
        self.dataframes = None
        print('The folder is ' + self.folder)

    def get_last_camas_xlsx(self):
        self.df_uci_habilitada = pd.read_excel('../input/Camas_uci/last_ingresos.xlsx', sheet_name='Hoja1')

    def last_file_to_csv(self):

        self.df_uci_habilitada['Serie'] = 'Ingresos a HOSPITAL por COVID-19'
        result =self.df_uci_habilitada

        identifiers = ['Fecha', 'Serie']
        variables = [x for x in result.columns if x not in identifiers]

        for i in range(len(variables)):
            result.rename(columns={variables[i]: variables[i].date()}, inplace=True)
            variables[i] = variables[i].date()

        result = result[identifiers + variables]
        result.to_csv(self.output + '.csv', index=False)

        df_t = result.T
        df_t.to_csv(self.output + '_t.csv', header=False)

        df_std = pd.melt(result, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                         value_name='Casos')

        df_std.to_csv(self.output + '_std.csv', index=False)


class IngresosHospital_ftp:
    def __init__(self, bucket, folder, access_key, secret_key, output):
        self.bucket = bucket
        self.folder = folder
        self.access_key = access_key
        self.secret_key = secret_key


        # store used variables
        self.output = output
        self.last_added = None
        self.date = None
        self.tables = None
        self.dataframes = None
        print('The folder is ' + self.folder)

    def get_last_camas_xlsx(self):
        # init session
        self.session = boto3.Session(
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            region_name='us-east-1')
        self.s3 = self.session.resource('s3')
        self.actual_bucket = self.s3.Bucket(self.bucket)

        get_last_modified = lambda obj: int(obj.last_modified.strftime('%m%d'))

        objs = [obj for obj in self.actual_bucket.objects.filter(Prefix=self.folder) if 'xlsx' in obj.key]

        objs = [obj for obj in sorted(objs, key=get_last_modified)]

        self.last_added = objs[-1]
        print('last added file is: ' + self.last_added.key)
        file_path = self.last_added.key
        s3_client = boto3.client('s3',
                                 aws_access_key_id=self.access_key,
                                 aws_secret_access_key=self.secret_key)

        obj = s3_client.get_object(Bucket=self.bucket, Key=file_path)
        self.df_uci_habilitada = pd.read_excel(obj['Body']._raw_stream.data, sheet_name='Hoja1')


    def last_file_to_csv(self):

        self.df_uci_habilitada.rename(columns={'Fecha':'Serie'},inplace=True)
        self.df_uci_habilitada['Serie'] = 'Media Móvil Ingresos a Hospital por COVID-19'
        result =self.df_uci_habilitada
        identifiers = ['Serie']
        variables = [x for x in result.columns if x not in identifiers]

        for i in range(len(variables)):
            result.rename(columns={variables[i]: variables[i].date()}, inplace=True)
            variables[i] = variables[i].date()

        result = result[identifiers + variables]
        result.to_csv(self.output + '.csv', index=False)

        df_t = result.T
        df_t.to_csv(self.output + '_t.csv', header=False)

        df_std = pd.melt(result, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                         value_name='Casos')

        df_std.to_csv(self.output + '_std.csv', index=False)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        my_bucket_name = sys.argv[1]
        my_access_key = sys.argv[2]
        my_secret_key = sys.argv[3]
        my_IngresosHospital = IngresosHospital_ftp(my_bucket_name, 'ingresosHospital', my_access_key, my_secret_key, '../output/producto92/Ingresos_Hospital')
        my_IngresosHospital.get_last_camas_xlsx()
        my_IngresosHospital.last_file_to_csv()


    else:
        my_bucket_name = 'local'
        my_access_key = 'sys.argv[2]'
        my_secret_key = 'sys.argv[3]'
        my_IngresosHospital = IngresosHospital_local(my_bucket_name, 'ingresosHospital', my_access_key, my_secret_key, '../output/producto92/Ingresos_Hospital')
        my_IngresosHospital.get_last_camas_xlsx()
        my_IngresosHospital.last_file_to_csv()