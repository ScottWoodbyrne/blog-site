# Powerful Fortrace

A Blog created in Django using PyCharm. Deployed version hosted on heroku available @ https://powerful-fortress-80635.herokuapp.com/

## Requirements

```
* arrow==0.8.0
* boto==2.42.0
* dj-database-url==0.4.1
* Django==1.9.8
* django-disqus==0.5
* django-forms-bootstrap==3.0.1
* django-gravatar2==1.4.0
* django-storages==1.5.0
* funcsigs==1.0.2
* gunicorn==19.6.0
* mock==2.0.0
* pbr==1.10.0
* Pillow==2.9.0
* python-dateutil==2.5.3
* requests==2.10.0
* six==1.10.0
* sqlparse==0.2.0
* stripe==1.37.0
* wheel==0.24.0
* mysql-python==1.2.5
```

## Install requirements via pip:

```
    pip install -r requirements.txt
```

## Run database migrations:

```
    python manage.py migrate
```

## Add local gitrepo

```
    $ git init
    $ git add -A
    $ git commit -m "Initial commit"
```

## Deployment to Heroku

```
    $ heroku create
    $ git push heroku master
```

## Migrate on Heroku

```
    $ heroku run python manage.py migrate
```

## Automated testing

```
    Blog/test.py
```

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
