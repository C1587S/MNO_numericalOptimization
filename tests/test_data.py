
#!/usr/bin/env python
# coding: utf-8

#=====================================
# Unittest for data retrieved
#=====================================

import unittest
import pandas as pd

url = "https://raw.githubusercontent.com/afcarl/ebola-imc-public/master/data/kenema/test/pres-kgh/imputation-50.csv"

df=pd.read_csv(url,sep=",")

colnames = list(df)

class DataTestCase(unittest.TestCase):


    def test_retrieved_data(self):
        '''
        Test para evaluar si el insumo principal para correr la regresión logística es adecuado. 
        En este caso, se prueba si todas las columnas tienen más de un valor único (para ser consideradas
        variables)
        '''
  
        for i in colnames:
            with self.subTest(i=i):
                self.assertTrue(len(df[i].unique())>1)



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
