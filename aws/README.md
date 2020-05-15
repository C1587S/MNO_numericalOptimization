# Configuración AWS

Esta carpeta contiene los scripts e indicaciones necesarias para la configuración de una instancia EC2 en donde se llevará acabo el procesamiento.

## I. Lenvatar instancia EC2

Por medio de la consola de aws se levanta uns instancia EC2 dentro de una VPC que vive dentro de la VPC 'proyecto-final' con las características necesarias para correr el proyecto. Estamos usando una instancia con ´ubuntu server 18.04´ con ´1 GB´ de memoria RAM y 4 procesadores (por definir)

Se conecta por primera vez a la instancia utilizando el protocolo ssh como sigue:

```
ssh -o "ServerAliveInterval 60" -i /ruta/llave.pem  ubuntu@ip-ec2
```

Para salir, basta con poner exit en el shell de la instancia.

## II. ec2-config.sh

Este script crea los usuarios en la EC2 para los integrantes del equipo.  Es necesario introducir una contraseña a cada uno de ellos, por lo que debemos estar conectados a la instancia. Para poder hacer uso es necesario darle los permisos con el comando

```
chmod +x ec2-config.sh.
```
y corremos el script:

```
./ec2-config.sh
```

En este punto ya tenemos a los usuarios agregados: todos con la misma contraseña y permisos de super usuario.

Además se instala la paquetearía básica necesaria para montar el ambiente virtual dentro de la máquina.

## III. Agregar llaves para conexión de usuarios

Una vez creados los usuarios, copiaremos las llaves públicas de cada uno de los usuarios a su usuario correspondiente.
Para **cada usuario** debemos de seguir el siguiente proceso:  
1. Es necesario modificar el archivo sudo nano /etc/ssh/sshd_config y cambiar los parámetros a la siguiente configuración:
  + PubkeyAuthentication yes
  + PasswordAuthentication yes

2. Reiniciar el servicio sshd:
  + ```sudo service sshd restart```

3. Realizar el copiado de las llaves al bastión, de forma segura con el comando:
  + ```ssh-copy-id -f -i /ruta/llave/id_llave.pub usuario@ip-ec2```

4. Es necesario modificar el archivo sudo nano /etc/ssh/sshd_config y cambiar los parámetros a la siguiente configuración:
  + PasswordAuthentication no

5. Reiniciar el servicio sshd:
  + ```sudo service sshd restart```

6. Finalmente, nos reconectamos a la EC2 con su llave pública usando el comando que se muestra en el punto I.
