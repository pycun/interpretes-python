# Instalación de PyPy en Ubuntu 20.04

## Paso 1: Actualizar el sistema
Antes de comenzar, asegúrate de tener el sistema actualizado.

```bash
sudo apt update && sudo apt upgrade -y
```

## Paso 2: Instalar dependencias
Instala las dependencias necesarias antes de descargar PyPy.

```bash

sudo apt install -y build-essential libffi-dev libssl-dev zlib1g-dev libbz2-dev libsqlite3-dev
```

## Paso 3: Descargar PyPy
Ve al sitio web de PyPy (https://www.pypy.org/) y copia el enlace de descarga de la versión que desees. Luego, utiliza wget para descargar el archivo.

```bash
wget https://downloads.python.org/pypy/pypy3.x-v7.3.7-linux64.tar.bz2
```
Asegúrate de reemplazar pypy3.x-v7.3.7 con la versión más reciente disponible.

## Paso 4: Descomprimir el archivo
Descomprime el archivo descargado.

```bash
tar -xf pypy3.x-v7.3.7-linux64.tar.bz2
```

## Paso 5: Mover PyPy a /opt
Mueve la carpeta PyPy a /opt para tener una instalación global.
```bash
sudo mv pypy3.x-v7.3.7-linux64 /opt/pypy
```

## Paso 6: Crear enlaces simbólicos
Crea enlaces simbólicos para facilitar el acceso a PyPy.

```bash
sudo ln -s /opt/pypy/bin/pypy3 /usr/local/bin/pypy3
sudo ln -s /opt/pypy/bin/pypy3 /usr/local/bin/pypy
```
## Paso 7: Verificar la instalación

Verifica que PyPy se haya instalado correctamente.

``` bash
pypy3 --version
```
## Paso 7: Ejecutamos el ejemplo con pypy

Nos posicionamos en donde este nuestro archivo a ejecutar y ejecutamos el ejemplo con pypy

``` bash
pypy3 ejemplo_pypy.py
```