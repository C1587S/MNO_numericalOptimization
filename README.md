# Implementación de métodos de optimización numérica en un modelo de aprendizaje

## Objetivo

Tomando como referencia el trabajo de investigación realizado por [Colubri et. al (2019)](https://www.thelancet.com/action/showPdf?pii=S2589-5370%2819%2930096-3), se busca entrenar un modelo de regresión logística que permite pronosticar la supervivencia a enfermedad por virus del ébola. Para tal propósito, se utilizan datos recolectados por el Cuerpo Internacional de Medicina (IMC, por sus siglas en inglés) durante 2014 y 2016 en Liberia y Sierra Leona. _El fin del presente proyecto es evaluar el desempeño de diferentes métodos de optimización numérica en un contexto de machine learning utilizando cómputo en paralelo. En particular, se mide el desempeño tanto en términos del uso y tiempo de recursos computacionales para lograr convergencia, como con relación a métricas de desempeño del modelo. Finalmente, se realiza un análisis de los resultados en torno a la pregunta planteada inicialmente._

### Datos

### Modelo

### Algoritmos

### Implementación




La implementación de este ejercicio se realizará por medio de código escrito en lenguaje Python. En particular, con el fin de minimizar la función de pérdida de log-verosimilitud negativa (y el riesgo empírico en SGD), se incluirán módulos propios para resolver el problema. Los pasos a seguir son los siguientes:

- Implementar `grad_F` y `hess_F` en `python`.
- Implementar el método de máximo descenso para minimizar <img src="https://render.githubusercontent.com/render/math?math=F(\beta)">
. Elegimos un <img src="https://render.githubusercontent.com/render/math?math=\beta^{0}"> aleatorio y una tolerancia de <img src="https://render.githubusercontent.com/render/math?math=\epsilon = 10^{-8}">.
- Implementar un clasificador de regresión logística para obtener <img src="https://render.githubusercontent.com/render/math?math=\hat{y}">.
- Implementar el método de Newton para minimizar <img src="https://render.githubusercontent.com/render/math?math=F(\beta)">
- Implementar el método BFGS
- Implementar el método SGD
- Implementar variabilidad en tasa de aprendizaje (condición de Armijo).
- Paralelizar procesos; por ejemplo: resolver en paralelo la dirección del descenso.
- Dockerizar ambiente
- Comparar tiempos de ejecución
- Pruebas Unitarias

### Herramientas a utilizar

Con el fin de generar un entorno aislado que permita evaluar el desempeño del proceso de entrenamiento en término de recursos computacionales, se utilizará una instancia EC2 de Amazon Web Services (`AWS`). Adicionalmente, para tener un control del entorno virtual asociado, se creará una imagen de `docker` asociada al repositorio donde se encontrarán todos los códigos de este proyecto.

### Referencias

- Nocedal, J., & Wright, S. (2006). Numerical optimization. Springer Science & Business Media.
- Colubri, A., Hartley, M. A., Siakor, M., Wolfman, V., Felix, A., Sesay, T., ... & Sabeti, P. C. (2019). Machine-learning Prognostic Models from the 2014–16 Ebola Outbreak: Data-harmonization Challenges, Validation Strategies, and mHealth Applications. EClinicalMedicine, 11, 54-6º4.
