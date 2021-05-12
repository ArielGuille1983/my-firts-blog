## Instalación

```
pip install -r requirements.txt

```
## Consola virtual

```
myvenv\Scripts\activate

```
## Lanzar servidor

```
python manage.py runserver --settings=mysite.local_settings

```

## Shell (InteractiveConsole)

```

python manage.py shell --settings=mysite.local_settings

from blog.factories import *
PostFactory.create()
PostFactory.create_batch(10) 

```
**probando algunas cosas(negrita)**

~~probando el tachado~~

## Heroku

```
heroku run python manage.py shell -a arieleduardo83blog

```

```

## Actualizar Models 

python manage.py makemigrations

python manage.py migrate --settings=mysite.local_settings


```
## Logs

```
heroku logs -a arieleduardoblog

heroku ps -a arieleduardoblog

```






