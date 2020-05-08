## Docker - documentación


Ejecución del entorno de `docker` de forma **local** para este repositorio.

En la línea de comandos ejecutar:

1. versiones y entorno local:

```{bash}
VERSION=v1
REPO_URL=c1587s/mno_numopt:v1
BUILD_DIR=<directorio_local>
```


Note que `directorio_local` va a ser una carpeta disponible en la CPU local que va tener interacción directa (y sus archivos) con la imagen de `docker`.

2. Descargar imagen

```{bash}
docker pull $REPO_URL:$VERSION
```

3. Ejecutar

```{bash}
docker run --rm -it --name jupyterlab-local -p 8888:8888 -v $BUILD_DIR:/home/jovyan/work $REPO_URL:$VERSION 
```

4. Se abre un navegador y se entra a `localhost:8888`

(Opcional)
Con _jupyter lab corriendo en localhost:8888_

Para entrar al contenedor:

```{bash}
docker exec -it -u=miuser jupyterlab-local bash
```

Detener:

```{bash}
docker stop jupyterlab-local
```

Para borrar contenedor en caso de no haber activado la bandera `--rm` en el paso 3.
```{bash}
docker rm jupyterlab-local
```
