#!/usr/bin/env python
# coding: utf-8

#========================================================
# Funciones empleadas para la implementación del proyecto
#========================================================



def sigmoide(z):
    '''

    Función que devuelve el sigmoide de un vector

        - Parámetros:

            -- z (vec): vector numérico de m entradas

        - Salidas

            -- sig (vec): vector númerico de m entradas, cada entrada tiene

                         un valor entre -1 y 1
    '''
    # Se revisa que los parámetros de entrada sean congruentes con la funcionalidad
    if type(z) is not np.ndarray:
        sys.exit('Error: la entrada debe ser de tipo numpy.ndarray')

    sig = 1/(1+ np.exp(-z))

    return sig

def calc_mu(X,beta):
    '''

    Función que calcula la media para una variable aleatoria con distribución bernoulli.

        - Parámetros:

            -- X (mat): matriz de mxp entradas

            -- beta (vec): vector con p entradas

        - Salidas

            -- mu (vec): vector de m entradas
    '''
    a = np.matmul(beta,np.transpose(X))
    mu = sigmoide(a)

    return mu

def f(X,y,beta):
    '''

    Función que computa la log-verosimilitud negativa

        - Parámetros:

            -- X (mat): matriz de mxp entradas

            -- y (vec): vector de de m entradas de la variable output

            -- beta (vec): vector de p entradas

        - Salidas

            -- lvn (int): log-verosimilitud negativa
    '''


    # Se revisa que los parámetros de entrada sean congruentes con la funcionalidad
    m,p = X.shape
    if y.shape[0]!= m:
        sys.exit('Error:  El número de renglones de X debe ser igual al número de entradas del vector y.')
    if beta.shape[0]!= p:
        sys.exit('Error:  El número de columnas de X debe ser igual al número de entradas del vector beta.')

    prob = calc_mu(X,beta)
    # Log-verosimilitud negativa
    lvn = -sum(y*np.log(prob)+(1-y)*(np.log(1-prob)))
    return lvn


def gradiente_f(X,y,beta):
    '''

    Función que calcula el gradiente asociado la log-verosimilitud negativa del

    problema de regresión logística

        ** Parámetros:

            - X (mat): matriz de mxp entradas

            - y (vec): vector de de m entradas de la variable output

            - beta (vec): vector de p entradas

        ** Salidas

            - grad (vec): vector de m entradas
    '''

    # Se revisa que los parámetros de entrada sean congruentes con la funcionalidad
    m,p = X.shape
    if y.shape[0]!= m:
        sys.exit('Error:  El número de renglones de X debe ser igual al número de entradas del vector y.')
    if beta.shape[0]!= p:
        sys.exit('Error:  El número de columnas de X debe ser igual al número de entradas del vector beta.')

    mu = calc_mu(X,beta)
    grad = np.matmul(np.transpose(X), mu-y)
    return grad


def hessiana_f(X,y,beta):
    '''

    Función que calcula la matriz Hessiana asociada a la log-verosimilitud negativa del

    problema de regresión logística

        ** Parámetros:

            - X (mat): matriz de mxp entradas

            - y (vec): vector de de m entradas de la variable output

            - beta (vec): vector de p entradas

        ** Salidas

            - hes (vec): vector de m entradas
    '''
    # Se revisa que los parámetros de entrada sean congruentes con la funcionalidad
    m,p = X.shape
    if y.shape[0]!= m:
        sys.exit('Error:  El número de renglones de X debe ser igual al número de entradas del vector y.')
    if beta.shape[0]!= p:
        sys.exit('Error:  El número de columnas de X debe ser igual al número de entradas del vector beta.')

    mu = calc_mu(X,beta)
    S = np.diag(mu*(1-mu))
    hes = np.matmul(np.transpose(X),np.matmul(S,X))
    return hes


def normalize(x):
    '''

    Función que normaliza un vector

        ** Parametros:

            - x: vector a normalizar

        ** Salidas:

            - norm : vector x normalizado
    '''
    # Se revisa que los parámetros de entrada sean congruentes con la funcionalidad
    if type(x) is not np.ndarray:
        sys.exit('Error: la entrada debe ser de tipo numpy.ndarray')

    norm = x/np.sqrt(sum(x*x))
    return norm
def clasifica(X, beta_hat,limit=0.5):
    '''

    Función que clasifica la ocurrencia de probabilidades en dos grupos.

    Emplea el parámetro límite para delimitar si se clasifica en el grupo 0 o 1.

        ** Parámetros:

            - X (mat): matriz de mxp entradas

            - beta_hat (array): optimized parameter

            - limit (float64): 0<limit<1: Threshold for each classification


        ** Salidas:

            - yhat: array of classifed data
    '''
    # Se revisa que los parámetros de entrada sean congruentes con la funcionalidad
    if type(X) is not np.ndarray or type (beta_hat) is not np.ndarray:
        sys.exit('Error: X y beta_hat deben ser de tipo numpy.ndarray')
    if limit > 1 or limit < 0:
        sys.exit('Error:  limit es un paramétro que debe estar entre 0 y 1')

    mu = calc_mu(X,beta_hat)
    yhat = mu
    yhat[mu<limit] = 0
    yhat[mu>=limit] = 1
    return yhat

def descent_direction(X, y, beta, method="max",H=None):
    '''

    Función que devuelve vector normalizado (px1) que apunta en la direccion de decenso

        ** Parámetros:

            - X (mat): matriz de mxp entradas

            - y (vec): vector de de m entradas de la variable output

            - beta (vec float64): vector de entradas a optimizar

            - method (str): método que determina la dirección de descenso

                    --Opciones:

                            --- max: método de descenso

                            --- newton: método de Newton

                            --- bfsg: metodo bfsg

            - H (mat pxp): Parámetro para la dirección de decenso del metodo bfgs

        ** Salidas

            - pk (vec): vector normalizado con la direccion del paso
    '''
    if(method == "max"):
        pk = gradiente_f(X,y,beta)

    elif(method == "newton"):
        grad = gradiente_f(X,y,beta)
        hess = hessiana_f(X,y,beta)
        pk = np.linalg.solve(hess,grad)

    elif(method=="bfsg"):
        # Se revisa que los parámetros de entrada sean congruentes con la funcionalidad
        if type(H) is not np.ndarray:
            sys.exit('Error: H debe ser de tipo numpy.ndarray')
        pk = np.matmul(H,gradiente_f(X,y,beta))

    return - normalize(pk)

def calc_H(X,y,beta,beta_new=None,H=None):
    '''

    Función que actualiza los valores de la matriz H del metodo bfgs para cada iteracion

        ** Parametros:

            - X (mat): matriz de mxp entradas

            - y (vec): vector de de m entradas de la variable output

            - beta (array) - valor de cantidad a optimizar en la iteracion actual

            - beta_new (array)- valore de la cantidad a optimizar despues de la actualizacion

            - H (mat)- valor de la matriz H en la iteracion anterior



        ** Salidas:

            - H (mat): valor de la matriz para la siguiente iteracion
    '''

    w = gradiente_f(X,y,beta_new)- gradiente_f(X,y,beta)
    z = beta_new-beta
    Hz = np.matmul(H,z)
    dotwz = np.dot(w,z)
    dotzhz = np.dot(Hz,z)
    H = H+(np.outer(w,w)/dotwz)-(np.outer(Hz,Hz)/dotzhz)

    return H

def calc_lr(X, y, beta, lr, pk, c1=10**(-4), tao=0.5, reset_lr=False):
    '''

    Función que calcula el tamaño del paso para cada iteración utilizando la condicion de armijo.

    La tasa de aprendizaje minima es la que tenia en el paso anterior.

        ** Parámetros:

            - X (mat): matriz de mxp entradas

            - y (vec): vector de de m entradas de la variable output

            - lr (float64): tasa de aprendizaje

            - pk (array px1 float64): direccion de decenso

            - c1 (float64) 0<c1<1: parametro de control

            - tao (float64) 0<tao<1: parametro de decrecimiento de lr

        ** Salidas

            - lr (float64): tamaño de paso
    '''
    # Se revisa que los parámetros de entrada sean congruentes con la funcionalidad
    if tao > 1 or tao < 0:
        sys.exit('Error:  tao es un parámetro que debe estar entre 0 y 1')
    if c1 > 1 or c1 < 0:
        sys.exit('Error:  c1 es un paramétro que debe estar entre 0 y 1')

    # Inicializamos
    tao = 0.9
    max_iter = 100
    iter = 0

    # Inicializa lr
    if reset_lr==True: lr = 1

    # Evaluaciones periódicas
    grad = gradiente_f(X,y,beta)
    eval_f = f(X,y, beta)

    # Primera iteracion
    f_x =  f(X,y, beta + lr*pk) #en nocedal es phi(alpha)
    f_x1 = eval_f + c1 * lr *  np.dot(grad,pk) # en nocedal es l(alhpa)

    while ((f_x > f_x1) & (iter < max_iter)):
        lr = lr*tao
        f_x =  f(X,y, beta + lr*pk)
        f_x1 = eval_f + c1 * lr *  np.dot(grad,pk)
        iter+=1

    return lr

def gradient_descent(X, y, lr=1, tol=10**(-7), max_iter=10**5, method="max", reset_lr=False, verbose_n=1000):
    '''

    Función que devuelve vector de parámetros beta (px1) resultante del proceso

    de optimización por descenso de gradiente

        ** Parámetros:

            - X (mat): matriz de mxp entradas

            - y (vec): vector de de m entradas de la variable output

            - lr (float64): valor inicial de la tasa de aprendizaje

            - tol (float64): criterio de convergencia

            - max_iter (int): número máximo de iteraciones

            - method (str): método que determina la dirección de descenso

                Opciones:

                    -- max: método de descenso

                    -- newton: método de Newton

                    -- bfsg

        ** Salidas

            - beta_new (vec): vector de p entradas con parámetros que minimizan la función de pérdida
    '''
    # Se revisa que los parámetros de entrada sean congruentes con la funcionalidad
    m,p = X.shape
    if y.shape[0]!= m:
        sys.exit('Error:  El número de renglones de X debe ser igual al número de entradas del vector y.')


    # Inicializa
    iteraciones=0
    H = None
    dims = X.shape[1]
    tol = tol*dims

    # Inicializamos beta aleatoria
    beta = np.random.normal(1,3,dims)
    if method =="bfsg": H = np.identity(dims)

    # Primera iteracion
    pk =  descent_direction(X, y, beta, method,H)
    beta_new = beta + lr*pk
    if method == "bfsg": H=calc_H(X,y,beta,beta_new,H)

    # Condición de paro.
    while ((np.linalg.norm(gradiente_f(X,y,beta_new)) > tol) & (iteraciones < max_iter)):
        iteraciones+=1 #contador de ciclo

        beta = beta_new
        pk =  descent_direction(X,y,beta,method,H)
        lr = calc_lr(X, y, beta, lr, pk, reset_lr = reset_lr)

        beta_new = beta + lr*pk

        if method == "bfsg": H=calc_H(X,y,beta,beta_new,H)

        # Imprime

        if iteraciones % verbose_n == 0:
            print("************************************************************************")
            grad=np.linalg.norm(gradiente_f(X,y,beta_new))
            print(f'GRADIENTE: {grad:.7E}, LEARNING RATE: {lr:.4E}, Nº ITERACIONES: {iteraciones}')


    print("*========================================================================*")
    if iteraciones == max_iter:print("Alcanzó el número máximo de iteraciones")

    print("ITERACIONES: ",iteraciones)
    print("GRADIENTE DE F: ",np.linalg.norm(gradiente_f(X,y,beta_new)))
    print("*========================================================================*")

    return beta_new
