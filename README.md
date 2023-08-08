# FinanzasWP

## Table of Contents

* [Descripción](#descripción)
* [Requisitos](#requisitos)
* [Docker](#docker)
* [Instalación](#instalación)
* [Uso](#uso)
* [Debbug in VSCode](#debbug-in-vscode)
* [Tests](#tests)
* [Cómo contribuir](#cómo-contribuir)
* [Notas](#notas)

## Descripción

Este proyecto esta destinado a realizar un repositorio de ejemplo con la utilizacion de FastAPI y el uso de una arquitectura hexagonal
o arquitectura domain-adapter.
Como caso de uso se realizo una aplicacion de finanzas personales con la particularidad que recibe y envia informacion por Whatsapp.
Para ello se creo una cuenta de Meta con el objetivo de interactuar con la API de Whatsapp.
Esta aplicacion requiere de una cuenta verificada de Meta Buisness con datos legales de la empresa para ponerla en funcionamiento pleno, por ello es que no se encuentra en produccion. (Cualquier ayuda es bienvenida)

## Requirements

* Python 3.10
* Docker
* Docker Compose

## Docker

Descarga la imagen

    docker pull ezemarcel/finanzaswp:latest

Ahora corre la imagen

    docker run --name finanzaswp --rm -p 8000:80 ezemarcel/talana_app

## Instalación

Clone el repositorio: 

    git clone https://github.com/Ezek10/interview_1.git

Cree una unidad virtual: 

    python -m venv .venv

Activar ambiente virtual:

    .\.venv\Scripts\activate

Instale las dependencias:

    pip install -r requirements.txt

## Uso

Para correr el programa corra:

    uvicorn src.app:app

o

    make run

y luego realice la siguiente request:

    curl --location 'localhost:8000/fight' \
    --header 'Content-Type: application/json' \
    --data '{
        "player1":
            {
                "movimientos": ["SDa", "DSD", "SA", "DSD"],
                "golpes":["K", "P", "K", "P"]
            }, 
        "player2":
            {
                "movimientos":["DSD", "WSA", "ASA", "", "ASA", "SA"],
                "golpes":["P", "K", "K", "K", "P", "k"]
            }
    } '


respuesta esperada:

    []


## Debbug in VSCode

Copiar el siguiente codigo en .vscode/launch.json

    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Uvicorn run",
                "type": "python",
                "cwd": "${workspaceFolder}/",
                "request": "launch",
                "program": "${workspaceFolder}/.venv/Scripts/uvicorn.exe",
                "args": [
                    "src.app:app"
                ],
                "console": "integratedTerminal",
                "justMyCode": true,
                "envFile": "${workspaceFolder}/.env-dev"
            }
        ]
    }

## Tests

Para correr los tests de esta aplicacion se recomienda usar el siguiente comando 

    pytest --cov --cov-config=.coveragerc --cov-report=html

o

    make test

puede abrir el archivo **htmlcov/index.html** para ver el coverage generado de los tests

## Cómo contribuir

Si bien este proyecto solo implica los conocimientos al momento de hacer esta entrevista creo que siempre puede ser bueno saber como se puede mejorar una entrega de este tipo, desde la funcionalidad del codigo, los tests hasta la documentacion o la presentacion del corriente archivo.

Si alguien se siente en capacidad de aportar sientase libre de crear una rama nueva y con un PR aportar sus ideas para mejorar esta presentacion

## Notas

- En la documentacion del ejercicio, el primer ejemplo aportado considere que tiene un error en el 3 comando de ataque del player 1, ya que menciona un ataque mientras que en los comandos no aporta ningun ataque

- Si bien hay algunas cosas que se podrian implementar no se hizo debido al alcance del ejercicio como Github Actions para realizar un Coverage Badge
