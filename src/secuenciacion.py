# by MinCiencia,

import time
import pandas as pd
import numpy as np
import requests
import io
import sys

class genomica:
    def __init__(self):
        # url for data
        self.my_files = {
            'perCountry':
                'https://raw.githubusercontent.com/hodcroftlab/covariants/master/web/data/perCountryData.json',
            'perCluster':
                'https://raw.githubusercontent.com/hodcroftlab/covariants/master/web/data/perClusterData.json'
        }

    def get_data(self):
        #to pandas
        self.perCountry = pd.read_json(self.my_files['perCountry'])
        self.perCluster = pd.read_json(self.my_files['perCluster'])

    def data_to_product(self):
        #per counrtry
        dirPerCountry = '../output/producto95/por_pais.csv'
        dirPerCluster = '../output/producto96/por_cluster.csv'
        self.perCountry.to_csv(dirPerCountry, index=False)
        self.perCluster.to_csv(dirPerCluster, index=False)
        self.perCluster_T = self.perCluster.T
        self.perCountry_T =  self.perCountry.T
        self.perCountry.to_csv(dirPerCountry.replace('.csv', '_T.csv'), header=False)
        self.perCluster_T.to_csv(dirPerCluster.replace('.csv', '_T.csv'), header=False)
        # identifiers = ['Fabricante']
        # variables = [x for x in outputDF2.columns if x not in identifiers]
        # outputDF2_std = pd.melt(outputDF2, id_vars=identifiers, value_vars=variables, var_name='Edad',
        #                         value_name='Dosis Refuerzo')
        # outputDF2_std.to_csv(name.replace('.csv', '_std.csv'), index=False)

if __name__ == "__main__":
    my_secuenciacion = genomica()
    my_secuenciacion.get_data()
    my_secuenciacion.data_to_product()