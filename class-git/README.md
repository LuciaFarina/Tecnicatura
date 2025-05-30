# Git

## CLASE 1

Abrimos la terminal de Git Bash en Window o la terminal de Ubuntu, tambien la terminal de Mac, y comenzamos con los siguientes comandos y creación de directorios

```sh
pwd
```

> Vemos la ruta de la carpeta en la que estamos

```sh
cd
```

> Es para navegar a una carpeta: change directory -> cambiar de directorio

```sh
cd /
```

> Nos lleva al home, en la raíz del disco

```sh
cd ~
```

> La virgulilla significa que estamos en el lugar de los documentos o del usuario

```sh
ls
```

> Esto es listar los archivos, nos muestra todos los archivos en la raíz

```sh
ls -al
```

> El espacio -al significa que es un argumento especial para ver archivos ocultos

> Usar la flecha hacía arriba nos muestra el último comando utilizado

```sh
ls -l
```

> Muestra casi todos los archivos sin los que están ocultos

```sh
ls -a
```

> Muestra el grupo de archivos pero no en una lista

```sh
clear
```

> Limpia la consola o ctrl + l

```sh
cd ..
```

> Nos devuelve a la carpeta anterior

```sh
cd U + tab
```

> Esto se usa para un autocompletado o para buscar una referencia

```sh
cd /D
```

> Cambiamos de disco en window

```sh
df -h
```

> Muestra todos los directorios en Ubuntu

```sh
cd /mnt/d
```

> Cambia de directorio usando WSL Ubuntu en window

### AHORA COMENZAMOS CON LA CREACIÓN DE CARPETAS

```sh
cd ..

cd ..

cd /mnt/c

cd ~
```

> Vamos a la raíz

```sh
mkdir Tecnicatura
```

> Recordar que en window las mayúsculas no tienen relevancia, pero si en Linux

```sh
cd tecnicatura

mkdir Python

mkdir Java

mkdir JavaScript
```

> Revisar y ejecutar cada comando, hacerlo como practica

## CLASE 2 MIÉRCOLES

Abrir git bash en Window o la terminal de Linux o de Mac: al abrir Git Bash hacerlo como administrador

```sh
touch vacio.txt #Crea un archivo con su extención: ESCRIBIR DENTRO

ctrl + s #Guardamos lo que escribimos en el archivo

./ #Significa la carpeta actual

../ #Significa la carpeta anterior

cat vacio.txt #Vemos el contenido del archivo

history #Veremos la historia completa de los comandos que hemos utilizado

!72 + enter #Veremos el comando que utilizamos en ese número

rm vacio.txt #Borra el archivo seleccionado, ¡¡¡¡CUIDADO!!!!

rm --help #Muestra como funciona el comando
```

### CREAR UN REPOSITORIO DE GIT Y HAZ TU PRIMER COMMIT

```sh
cd tecnicatura

mkdir class-git

cd class-git #Entramos en la carpeta que necesitamos trabajar

git init #Creamos un repositorio en la carpeta central, se crea el archivo .git

code .  #Abrimos VSC, el punto hace que se abra el archivo en el que estamos situados

ctrl + n #Creamos un archivo nuevo y escribimos en el, como lo hicimos antes

ctrl + s #Guardamos poniendo el nombre: historia.txt

git status #Vemos el estado del proyecto en tiempo real, esta en el área de trabajo

git add historia.txt #Enviamos el archivo al área de preparación

git status #Para ver el estado de cambios

git rm --cached historia.txt #Quitamos el archivo del área de preparación, cached significa que esta en memoria ram

git config #Tendremos la lista de como funciona la configuración

git config --list #Configuraciones por defecto, faltan cosas importantes

git config --list --show-origin #Veremos donde están las configuraciones guardadas

git config --global user.name "Ariel Betancud"

git config --global user.email "betancudariel@gmail.com" #El correo debe ser el mismo que usaremos en GitHub

git config --list #Ahora veremos que ya están todos los datos completos

git add . #Ingresamos todos los archivos al área de preparación (ram)

git commit -m "Mensaje importante del commit" #El primer commit esta hecho

code . #Hacemos cambios en el archivo y guardamos

git status #Hay cambios para commitear

git add .

git commit -m "Mi segundo commit"

git log historia.txt #Vemos toda la historia de este archivo, el número largo es el hash del commit
```

> Revisar y ejecutar cada comando, hacerlo como practica

## CLASE 3

Analizar cambios en los archivos de tu proyecto Git parte 3

Ingresamos de la siguiente manera:

Abrir git bash en Window o la terminal de Linux o de Mac: al abrir Git Bash hacerlo como administrador, en terminal también o usar sudo para permisos especiales.

```sh
cd tecnicaturagit #Ingresamos al directorio donde están nuestras carpetas de trabajo

ls #Vemos los archivos y directorios que ya tenemos

cd git #No hay nada

cd .. #Salimos

rm historia.txt #Eliminamos el archivo que habíamos hecho, esto en git bash (window) esto es para practica

rm Git #rm: cannot remove 'Git': Is a directory

rm --recursive -R Git #By default, rm does not remove directories.  Use the --recursive (-r or -R) arguments

option to remove each listed directory, too, along with all of its contents. #Esto es para practica

rm --help #Nos muestra lo que les puse arriba como documentación en Inglés.

mkdir class-git #Creamos la carpeta o directorio para trabajar en Git local por ahora.

cd class-git #Entramos para crear el README.md para este sector.

touch README.md #Vamos a crear un archivo nuevo, md significa markdown y se pueden trabajar con editores de texto, este es un lenguaje que transforma el texto a html.
```

> Enlace a la documentación en GitHub de [MARKDOWN](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

> Leemos la documentación para ir creando en README.md como lo enseña GitHub.

```sh
code . #Abrimos VSC para editar el archivo.
```

> Empezamos a cargar lo visto en las clases anteriores (Comandos) en el README y pasamos a commitear

```sh
git status

git add .

git status

git commit -m "Cargamos el README dentro del directorio class-git"

git status

git log #Para ver los dos commits hechos: Si tienes commiteada alguna clase anterior veras mas commits de los que yo tengo.

cd ..

cd ..
```

> Revisar y ejecutar cada comando, hacerlo como practica

## CLASE 4

Analizar cambios en los archivos de tu proyecto Git parte 4

Ingresamos de la siguiente manera:

Abrir git bash en Window o la terminal de Linux o de Mac: al abrir Git Bash hacerlo como administrador, en terminal también o usar sudo para permisos especiales.

TAREA -> AGREGAR LOS COMENTARIOS EN LOS COMANDOS, PARA SABER QUE PASA CON CADA UNO.

```sh
cd tecnicatura

cd class-git #Nos metemos hasta la carpeta class-git

ls # Listamos todos los archivos y carpetas

touch historia.txt #Crea un archivo vacío

code . #Abre el editor de codigo

#Modificamos el archivo historia.txt colocando lo siguiente: Bienvenido     mi nombre es Ariel (coloca tu nombre)

ctrl + s #Guardamos los cambios

git status #Vemos el estado actual

git add . #Agrega el archivo modificado

git status #Vemos el estado actual

git commit #Sin agregar -m veremos que pasa


#Agregar mensaje y salir con

Esc #Presionamos Escape

:wq! + enter #Y ya salimos si estamos en git bash con window

Esc + shift + z + z #Salimos del mensaje para el commit, en linux, esto anda en algunas terminales

#Agregamos otra línea de mensaje en historia.txt desde VSC: estoy estudiando programación

ctrl + s #Guard #Agrega el archivo modificado

git commit #Se abre un editor de código basado en línea de comandos, editor de texto como VSC llamado vim

Esc + i #Para comenzar a escribir mensaje del commit, no suele ser necesario

ctrl + x #Para salir en linux

s + enter #Para decir si al cambio y aceptar el nombre, ósea no cambiamos el nombre, la (s) es de si y la (y) es de yes, no olvidar enter en linux

git show #Vemos todos los cambios en el último commit

git log historia.txt #Vemos todos los commit

q #Para salir del registro de commits

#Copiamos un hash mas antiguo y otro reciente, ingresamos el siguiente comando

git diff hash_commit_numerico hash_commit_numerico #Comparamos diferentes commits y sus cambios, poner la versión mas vieja primero, luego la mas nueva

q #Para salir

cd ..

cd ..
```

La tarea de hoy, agregar esta clase al README.md con el lenguaje de markdown, como lo hicimos en la clase pasada, luego deben hacer el commit correspondiente al cambio agregado.

> Revisar y ejecutar cada comando, hacerlo como practica

## CLASE 5

¿Qué es el staging?

Tienes una carpeta donde están los archivos de tu proyecto o un directorio y allí tenemos el archivo historia.txt, cuando entramos por consola a ese archivo y creamos el git init, se crea un área en memoria ram que se llama staging, y el otro es el repositorio esta es la carpeta .git donde estarán todos los cambios al final del proyecto.

Entonces tenemos el área de trabajo, cuando colocamos git add historia.txt pasamos al staging o área de preparación, que hay que recordar que esto es en la memoria ram y luego con git commit -m "Mensaje" pasa al repositorio en la rama master, allí se genera un nombre llenos de letras y números, es el hash, el nombre del commit.

![branch master](img/image.png)

¿Qué es Gitflow? Gitflow es un modelo alternativo de creación de ramas en Git en el que se utilizan ramas de función y varias ramas principales. Fue Vincent Driessen en nvie quien lo publicó por primera vez y quien lo popularizó.

¿Qué es branch (rama) y cómo funciona un merge en git?

Tenemos una rama llamada master y es donde están los cambios de nuestros archivos, con cada commit creamos una nueva versión

Vamos a crear una rama experimental para otras versiones que suele llamarse development, al encontrar bug, se crea otra rama que suele llamarse hotfix para hacer reparaciones, siempre que ya tengamos resultados favorables, es donde decidimos hacer un merge, es unir los resultados de las ramas a la rama master.

La principal característica de las ramas principales es que solo existe una de cada tipo. El objetivo es que no se instancien y que no reciban código de forma directa a través de commit, siempre tienen que recibir código a través de ramas de tipo Feature, Release y Hotfix, siempre a través de ramas auxiliares.

Es un riesgo recibir código directamente en la rama Master, porque puede generar defectos en el repositorio en las subidas a producción, que no contemplemos o que no preveamos, por lo que siempre es mejor integrar código en otras ramas antes de integrar con las ramas Master y Develop.

Esta es una metodología estricta pero que da lugar a diferentes interpretaciones o diferentes formas de llevarla en cada equipo, por lo que en algunos casos, algún experto puede permitirse no seguir esa norma, pero son casos muy específicos y siempre de personas de confianza.

En las ramas auxiliares tenemos la rama Feature, la rama Release y la Rama Hotfix, que puede instanciarse todas las veces que se consideren necesarias:

La rama Feature, para nuevas características, nuevos requisitos o nuevas historias de usuario.
La rama Release, para estandarizar o cortar una serie de código que ha estado desarrollándose en la rama Develop, se saca una rama de este tipo, se mergea y ahí se depura.
La rama Hotfix, que habitualmente se utiliza para código para depurar el código que venga de producción, por haberse detectado un defecto crítico en producción que deba resolverse, al que se le va a hacer una Release puntual para corregirlo.
Estas ramas tienen un principio y un fin, ya que son ramas que se mergean con las ramas Master y Develop y desaparecen.

Podemos tener tantas ramas como queramos, tantos repositorios como queramos, lo más importante es saber cuando hacemos un merge, porque es posible que hayan archivos que rompan otros archivos, a esto se lo llama conflicto o bug.

## CLASE 6

Volver en el tiempo en nuestro repositorio utilizando reset y checkout parte 6

Ingresamos de la siguiente manera:

Abrir git bash en Window o la terminal de Linux o de Mac: al abrir Git Bash hacerlo como administrador, en terminal también o usar sudo para permisos especiales.

TAREA -> AGREGAR LOS COMENTARIOS EN LOS COMANDOS, PARA SABER QUE PASA CON CADA UNO.

```sh
cd tecnicatura
```

> Entra en la carpeta `tecnicatura`.

```sh
cd class-git
```

> Entra en la carpeta `class-git`.

```sh
ls
```

> Lista los archivos y carpetas dentro del directorio actual.

```sh
touch historia.txt
```

> Crea un archivo vacío llamado `historia.txt`.

```sh
cd ..
```

> Vuelve a `tecnicatura`.

```sh
code .
```

> Abre Visual Studio Code en la carpeta actual para editar archivos.

```sh
git commit -a
```

> Realiza un commit de todos los archivos ya versionados que hayan sido modificados; se abre Vim para escribir el mensaje.

```sh
esc + i
```

> Presiona `Esc` y luego `i` para entrar en modo de inserción en Vim.

```sh
esc
```

> Sal del modo de inserción para poder escribir comandos en Vim.

```sh
:wq!
```

> Guarda el archivo y sale de Vim.

```sh
git log
```

> Muestra el historial de commits completos realizados.

```sh
git show
```

> Muestra los detalles del último commit (contenido, autor, fecha, etc.).

```sh
git log --oneline
```

> Muestra el historial de commits de forma resumida (una línea por commit).

```sh
git reset <hash-del-commit>
```

> Vuelve el repositorio al estado de un commit anterior. Puede ser un **reset suave** o **duro**.

```sh
git status
```

> Muestra el estado actual del repositorio (archivos modificados, en staging, etc.).

```sh
git add .
```

> Agrega todos los archivos modificados al staging area.

```sh
git commit -m "Agregamos datos de estudios en historia.txt"
```

> Realiza un commit con un mensaje personalizado.

```sh
git config --list
```

> Muestra la configuración actual de Git (nombre de usuario, correo, etc.).

```sh
git reset --hard <hash>
```

> **Reseteo duro**: descarta todo y vuelve exactamente al estado de ese commit (borra cambios locales).

> Crear, modificar y commitear de nuevo el archivo `historia.txt`.

```sh
git reset --soft <hash>
```

> **Reseteo suave**: mueve el puntero del commit pero deja los cambios en staging.

```sh
git diff
```

> Muestra las diferencias entre los archivos modificados y los últimos commits.

```sh
git add .
```

> Agrega los cambios al staging.

```sh
git status
```

> Muestra que ya está todo en staging. Git solo guarda archivos, no carpetas vacías.

```sh
git commit -m "Commiteamos lo último de hoy"
```

> Realiza el commit con un mensaje.

```sh
git log
```

> Revisa los commits recientes.

> Realizar cambios en `historia.txt`.

`ctrl + s`

> Guarda los cambios en el editor (por ejemplo, en VS Code).

```sh
git diff
```

> Muestra los cambios realizados antes de agregar al staging.

```sh
git commit -am "cambio en la última línea del historia.txt"
```

> Agrega y commitea directamente los archivos modificados (ya versionados).

```sh
git log
```

> Muestra el historial de commits.

```sh
q
```

> Salir de la vista del log o del show (cuando estás en modo vista).

```sh
git log --stat
```

> Muestra un resumen de los archivos modificados en cada commit y el número de líneas cambiadas.

```sh
q
```

> Salir del log con estadísticas.

```sh
git checkout <hash>
```

> Revisa cómo era el archivo en ese commit (estado anterior).

```sh
git status
```

> Revisa el estado del repositorio.

```sh
git checkout master
```

> Vuelve a la rama principal `master`.

```sh
git checkout <hash>
```

> Vuelve a un commit anterior y modifica desde allí.

```sh
git commit -am "Reemplazo de una versión por otra de la historia"
```

> Commit con cambios desde una versión anterior.

```sh
git log
```

> Vemos el nuevo commit generado.

> Se recomienda crear ramas para probar cambios sin afectar la rama principal.

```sh
git branch cambios
```

> Crea una nueva rama llamada `cambios`.

```sh
git checkout master
```

> Cambia de nuevo a la rama principal `master`.

> Las ramas primarias no se deben modificar directamente. Se sugiere usar nombres como `second`, `develop`, `release`, `hotfix`, etc.

```sh
git branch second
```

> Crea una rama secundaria `second`.

```sh
git branch tuNombre
```

> Crea una rama con tu nombre.

```sh
git branch hotfix
```

> Crea una rama para aplicar un arreglo rápido.

```sh
git branch
```

> Lista todas las ramas disponibles.

```sh
git branch -d cambios
```

> Elimina la rama `cambios` (solo si ya fue fusionada).

```sh
git branch -D cambios
```

> Fuerza la eliminación de la rama `cambios`.

```sh
cd ..
cd ..
```

> Sube dos niveles en el sistema de carpetas, saliendo de los directorios.
