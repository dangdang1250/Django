# Django
Learning Django, Create my web apps

## Packages:
django-mixins

```bash
#init
django-admin startproject mysite # will create mysite folder

cd mysite
python manage.py runserver 8001

# create new app under mysite
python manage.py startapp nailit # will create nailit folder

# Create superuser
python manage.py createsuperuser

# run tests
python manage.py test
```

## How to remove an app in Django
(How to remove an app in Django)[https://techstream.org/Bits/Remove-App-From-Django-Project]

more steps:
```shell
# do a git clean
git clean -dfx 
```