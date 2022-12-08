# KUI App (Kubernetes User Interface)

## Documentación 📖

[Documentacion](2ASIR_B_FERRER_ZAMBRANO_ABRAHAM_KUI.pdf)

---

## Instalaciones 💻

- Poetry
```
poetry install
```

- Python3 y pip
```
apt-get install python3-pip
```

- Librerias
```
pip install "cualquier libreria"
```

- Nautilus
```
apt-get install nautilus
```

- Saber la version de Python
```
python --version
```
---

## Instalacion para crear contenedores 📦

- [Docker](https://help.wnpower.com/hc/es/articles/360048910771-C%C3%B3mo-instalar-Docker-en-tu-servidor-con-Ubuntu)

- [Go](https://ubunlog.com/go-instala-este-lenguaje-de-programacion-ubuntu-20-04/)

- [Kind](https://kind.sigs.k8s.io/)

---

## Cómo usar este programa ⚙️

```
poetry run "./carpeta/Lo que sea"
```

---

## Solucion de posibles errores 🎊

```
python3 -m pip install --upgrade requests
```

```
pip install requests
```

- Problemas con el [PATH](https://askubuntu.com/questions/250929/pythonpath-environment-variable)
- Problemas con [RequestsDependencyWarning](https://stackoverflow.com/questions/50202238/python-pip-requestsdependencywarning-urllib3-1-9-1-or-chardet-2-3-0-doe)

---

## Funcionalidades 🎞️

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

## Diario 📓

- Dia 28/10/2022

Realizado varias busquedas y pensamiento de como va a ser la aplicacion, tambien se han resuelto algunos fallos con python y poetry.

[Instalacion de WSL](https://learn.microsoft.com/es-es/windows/wsl/tutorials/gui-apps) (Ya que solo se puede realizar en linux).

![Descripcion de la App](./img/UserInterface.jpeg)

---

- Dia 30/10/2022

Para hacer los commandos desde el WSL tengo que utilizar service.

- Comandos interesantes para docker 
    - docker run
    - service docker start/status/stop/restart
    - docker info 

- Intalacion go [aquí](https://tecadmin.net/how-to-install-go-on-ubuntu-20-04/).

- Comandos para clusters [aquí](https://kind.sigs.k8s.io/).
  

- Dia 31/10/2022

Documentacion de [kubernetes](https://kubernetes.io/es/docs/_print/).

- Dia 03/11/2022

Comandos [kubectl](https://geekflare.com/es/kubectl-examples/).

Configuracion [Kind](https://kind.sigs.k8s.io/docs/user/configuration/).


- Dia 03/11/2022

Buscando informacion de como realizar las graficas 

Dividiendo el código en clases


- Dia 05/11/2022

[Inmplementando los botones a los namespaces](img/botones.png)

Buscando informacion de como guardar la iformacion de los botones

- Dia 06/11/2022

Creo la hoja de estilos y sigo pensando en la estructura de la aplicacion

- Dia 08/11/2022

Estudiando la libreria [Textual](https://github.com/Textualize/textual) 

- Dia 10/11/2022

Implementando el modo oscuro a la aplicación

Solucionando fallos con las depedencias del WSL 

- Dia 15/11/2022

Implementando estilos al footer 

Implementando estilos a los namespaces 

- Dia 16/11/2022
  
  Se ha roto la app, tengo que volver a empezar desde 0 😭😭

- Dia 17/11/2022
  
  Comienzo de nuevo la app y encuentro los fallos que me estaba dando 😊

  [El principio](img/1.jpeg)

  Sigo con el curso de Python para poder continuar con la app, ya que se esta complicando la cosa

  Comienzo un curso de CSS para poder mejorar la hoja de estilos

- Dia 20/11/2022

  Sigo desarrollando....

  [Sigo dandole vueltas a la cabeza](img/2.jpeg)

  Comienzo un curso de Docker

- Dia 22/11/2022

Implementando los Pods, con sus respectivos botones 

Implementando estilos a los Pods

Solucionando fallos con el WSL

Buscando informacion de como abrir otra terminal mediante comandos

- Dia 23/11/2022

  Buscando informacion sobre los subprocesos

  Implementando los comandos 

- Dia 25/11/2022

  Solucionando errores con los pods

  No funcionan los botones de Pods 😭

- Dia 29/11/2022

  Arreglando posibles fallos al conectarse con los Dockers

  Soluciono los botones :)

- Dia 01/12/2022

  Implemento los logs

- Dia 02/12/2022

    Implemento los Plots

    Configuro los Plots para que coja os recursos de los contenedores 

    He conseguido que se muestre en directo y si se produce un cambio se actualize 

- Dia 03/12/2022

  Comienzo la documentación del proyecto

- Dia 05/12/2022

  Termino la funcionalidades de la app

  Retoco los estilos 

- Dia 06/12/2022

  Termino los estilos 

  Sigo con la documentación
- Dia 07/11/2022

  Termino la documentación 

  Comienzo con la presentacion y la defensa del proyecto

- Dia 08/11/2022

  🎊¡Ya esta todo acabado!🎊

  [Video de KUI en acción](img/Animation4.gif)