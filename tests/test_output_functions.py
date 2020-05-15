#!/usr/bin/env python
# coding: utf-8


#================================================================
# Unittest for Checking Ranges and Outputs of Auxiliar Functions
#================================================================




import numpy as np
import unittest



def calc_mu(X,beta):
    '''
    Calcula la media para una variable aleatoria con distribución bernoulli.
        ** Parámetros:
            - X (mat): matriz de mxp entradas
            - beta (vec): vector de p entradas
        ** Salidas
            - mu (vec): vector de m entradas
    '''
    a = np.matmul(beta,np.transpose(X))
    mu = sigmoide(a)

    return mu
   

def sigmoide(z):
    '''
    Devuelve el sigmoide de un vector
        ** Parámetros:
            - z (vec): vector numérico de m entradas
        ** Salidas
            - sig (vec): vector númericos de m entradas con valores entre -1 y 1
    '''
    sig = 1/(1+ np.exp(-z))
    return sig



def clasifica(X, beta_hat,limit=0.5):
    '''
    Función que clasifica la ocurrencia de probabilidades en dos grupos. Emplea el parámetro "límite" para determinar 
    si el punto es asignado al grupo 0 o grupo 1. 
    
        ** Parámetros:
            - X (mat): matriz de mxp entradas
            - beta_hat (vec): vector de p entradas
        ** Salidas:
            - y_hat (vec): vector de p entradas, con valores 0 o 1. 
    '''
    mu=calc_mu(X,beta_hat)
    yhat=mu
    yhat[mu<limit]=0
    yhat[mu>=limit]=1
    return yhat



class OutputValues(unittest.TestCase):
    
    
    def test_sigmoide_range(self):
        '''
        Test para evaluar si la función "sigmoide" retorna vectores con entradas cuyos valores están
        entre el rango -1 y 1.
        '''
        
        for i in range(0, len(sigmoide(z))):
            with self.subTest(i=i):
                self.assertTrue(-1 <= sigmoide(z)[i] <=1)      
    
    
    def test_clasifica_output(self):
        '''
        Test para evaluar si la función "clasifica" retorna un vector con entradas de 0 o 1.
        
        '''
        
        for i in range(0, len(clasifica(X, beta_hat,0.5))):
            with self.subTest(i=i):
                self.assertTrue(1 == clasifica(X, beta_hat, 0.5)[i] or clasifica(X, beta_hat, 0.5)[i] == 0)

    def test_calc_mu_dimension(self):
        
        '''
        Test para evaluar la concordancia entre las dimensiones de entrada de la funcion 
        "calc_mu" y las dimensiones de salida.
        '''

        self.assertEqual(len(calc_mu(X, beta)), np.size(X,0))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

