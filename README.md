# instalación

```
pip install -r requirements.txt

```
# Consola virtual

```
myvenv\Scripts\activate

```
# Lanzar servidor

```
python manage.py runserver --settings=mysite.local_settings

```

# Shell (InteractiveConsole)

```
python manage.py shell --settings=mysite.local_settings

from blog.factories import *
PostFactory.create()
PostFactory.create_batch(10)

```


