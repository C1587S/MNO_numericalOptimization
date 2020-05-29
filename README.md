
>Este repositorio puede ser ejecutado interactivamente desde `binder` dando click en el siguiente botón:  [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/C1587S/MNO_numericalOptimization/master)

# Implementación de métodos de optimización numérica en un modelo de aprendizaje

## Objetivo

Tomando como referencia el trabajo de investigación realizado por [Colubri et. al (2019)](https://www.thelancet.com/action/showPdf?pii=S2589-5370%2819%2930096-3), se busca entrenar un modelo de regresión logística que permite pronosticar la supervivencia a enfermedad por virus del ébola. Para tal propósito, se utilizan datos recolectados por el Cuerpo Internacional de Medicina (IMC, por sus siglas en inglés) durante 2014 y 2016 en Liberia y Sierra Leona. _El fin del presente proyecto es evaluar el desempeño de diferentes métodos de optimización numérica en un contexto de machine learning utilizando cómputo en paralelo. En particular, se mide el desempeño tanto en términos del uso y tiempo de recursos computacionales para lograr convergencia, como con relación a métricas de desempeño del modelo. Finalmente, se realiza un análisis de los resultados en torno a la pregunta planteada inicialmente._

**Ligadas asociadas:**

[Trabajo escrito](https://github.com/C1587S/MNO_numericalOptimization/blob/master/reporte/reporte_final.pdf): Reporte parcial de la implementación del trabajo.

[Presentacion](https://github.com/C1587S/MNO_numericalOptimization/blob/master/notebooks/notebook_implementacion.ipynb): Notebook con el desarrollo autocontenido del proyecto.

[Implementacion](https://github.com/C1587S/MNO_numericalOptimization): Misma que se encuentra dispuesta en un repositorio que tiene la siguiente estructura de carpetas:

```
├── aws                    <- Contiene los scripts e indicaciones necesarias
├                             para la configuración de una instancia EC2 en
├                             donde se llevará acabo el procesamiento.
├── data
│   ├── external           <- Data recolectada del repositorio público ebola-imc-public
│   ├── preprocessed       <- Data que ha sido transformada y empleada en el
│                             presente trabajo.
├── docs                   <- documentos asociados a la configuración de la imagen de docker empleada
│
├── images                 <- Imágenes asociadas al proyecto.
│
├── modulos                <- Módulos asociados al proyecto
│
├── notebooks              <- Jupyter notebook autocontenido con todo lo implementado a propósito del proyecto.
│
├── referencias            <- Referencias empleadas.
│
├── reporte                <- Reporte final generado en LaTex y compilado en
├                             PDF.
│   └── figures            <- Gráficas y figuras generadas que son empleadas en
│                             el reporte.
│
├── test                   <- Unittest implementados.
│
├── Dockerfile             
├── LICENSE                <- Licencia
├── README.md              <- Descripción breve del proyecto, estructura de carpetas del repositorio y datos de contacto.
│
└── requirements.txt       <- Las paqueterías y librerías empleadas
```


**Integrantes del equipo:**

- Juan Pablo Herrera Mussi ([Pilo1961](https://github.com/Pilo1961)) – Programador/Revisor
- Daniela Pinto Veizaga ([dapivei](https://github.com/dapivei)) – Team Leader/Revisora
- Sebastián Cadavid-Sánchez ([C1587S](https://github.com/C1587S))– Revisor/Programador

**Referencias:**



+ Colubri, A., Hartley, M. A., Siakor, M., Wolfman, V., Felix, A., Sesay, T., ... & Sabeti, P. C. (2019). Machine-learning Prognostic Models from the 2014–16 Ebola Outbreak: Data-harmonization Challenges, Validation Strategies, and mHealth Applications. EClinicalMedicine, 11, 54-6º4.

+ Murphy, K. P. (2012). Machine learning: a probabilistic perspective. MIT press.

+ Nocedal, J., & Wright, S. (2006). Numerical optimization. Springer Science & Business Media.
