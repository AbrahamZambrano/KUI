# KUI App (Kubernetes User Interface)


## Instalacion de python, poetry, etc..

```
pip install "cualquier libreria"
```

```
poetry install
```

```
sudo apt-get install python3-pip
```

```
python --version
```

```
sudo apt-get install nautilus
```

## Cómo usar este programa

```
poetry run "./carpeta/Lo que sea"
```

## Solucion de posibles errores

```
python3 -m pip install --upgrade requests
```

```
pip install requests
```
- Problemas con el [PATH](https://askubuntu.com/questions/250929/pythonpath-environment-variable)
- Problemas con [RequestsDependencyWarning](https://stackoverflow.com/questions/50202238/python-pip-requestsdependencywarning-urllib3-1-9-1-or-chardet-2-3-0-doe)


## Funcionalidades

La mayoría está WIP

- [ ] ASCII art para el header.

- [ ] Gráficos con plotext.
  - Utilizar este tipo de graficas con esta [libreria](https://github.com/piccolomo/plotext).
  
  - Podmeos utilizar el código que hemos visto [aquí](https://github.com/mle-infrastructure/mle-monitor/blob/main/mle_monitor/dashboard/components/plots.py).

- [ ] Plotext Utilidades.
    - [Utilidades](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#command-line-tool).
    - [Subplots](https://github.com/piccolomo/plotext/blob/master/readme/subplots.md#subplots).

- [ ] [Textualize](https://github.com/Textualize/textual) (Rama que se esta usando 0.1.9). 
    - [Galeria](https://www.textualize.io/textual/gallery).
 
- [ ] [Guia](https://textual.textualize.io/getting_started/) para utilizar Textualize.

- [ ] [Dive](https://github.com/wagoodman/dive), se intentara si da tiempo introducir esta libreria.
    - Utilizacion de [Dive con ejemplos](https://sleeplessbeastie.eu/2021/10/29/how-to-inspect-and-improve-docker-image-using-dive-utility/) e instalacion para su puesta en ejecucion.


Librerias que podrian interesar
- [gupshup](https://github.com/kraanzu/gupshup)
- [mle-monitor](https://github.com/mle-infrastructure/mle-monitor/blob/main/mle_monitor/dashboard/components/plots.py)

---

## Diario

- Dia 28/10/2022

Realizado varias busquedas y pensamiento de como va a ser la aplicacion, tambien se han resuelto algunos fallos con python y poetry.

[Instalacion de WSL](https://learn.microsoft.com/es-es/windows/wsl/tutorials/gui-apps) (Ya que solo se puede realizar en linux).

![Descripcion de la App](./img/UserInterface.jpeg)


