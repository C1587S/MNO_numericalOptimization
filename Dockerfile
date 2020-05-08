# base con scipy
FROM jupyter/scipy-notebook:dc9744740e12
# copia archivos en repositorio
COPY . .
# instala lista de paqueterías
RUN pip install -r requirements.txt
