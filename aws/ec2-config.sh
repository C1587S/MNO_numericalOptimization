#!/bin/bash

#instalacio de paquetes
apt-get update
apt-get install git
apt install docker.io

#creacion de usuarios
adduser --gecos --disabled-login --force-badname "JP"
usermod -aG sudo JP
echo "User created"

adduser --gecos --disabled-login --force-badname "Dani"
usermod -aG sudo Dani
echo "User Created"

adduser --gecos --disabled-login --force-badname "Sebastian"
usermod -aG sudo Sebastian
echo "User created"
