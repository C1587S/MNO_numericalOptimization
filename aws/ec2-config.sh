#!/bin/bash

#instalacio de paquetes
apt-get update
#apt-get install docker-ce docker-ce-cli containerd.io
apt-get install git
apt install docker.io

#creacion de usuarios
adduser --gecos --disabled-login --force-badname "JP"
#usermod -p 'saoW8Z/xz5qko' JP
usermod -aG sudo JP
echo "User created"

adduser --gecos --disabled-login --force-badname "Dani"
#usermod -p 'saoW8Z/xz5qko' Dani
usermod -aG sudo Dani
echo "User Created"

adduser --gecos --disabled-login --force-badname "Sebastian"
#usermod -p 'saoW8Z/xz5qko' Sebastian
usermod -aG sudo Sebastian
echo "User created"

#creacion folders de llaves
#su JP
#mkdir /home/JP/.ssh
#chmod 770 /home/JP/.ssh
#su Sebastian
#mkdir /home/Sebastian/.ssh
#chmod 770 /home/Sebastian/.ssh
#su Dani
#mkdir home/Dani/.ssh
#chmod 770 home/Dani/.ssh
