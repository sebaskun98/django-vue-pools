## Django App + Libs

### Summary

Back-end Django POC project to practice some libraries for a future professional project like: 
- django-adminactions
- django-auditlog
- django-cors-headers
- django-debug-toolbar
- django-filter
- django-import-export
- django-jazzmin
- djangorestframework
- drf-yasg

Project upload to Vercel and PostgreSQL hosted in Supabase. Used by Vue.js front-end.

### How to use it

Create a virtual environment to install dependencies in and activate it:

```sh
virtualenv2 --no-site-packages env
source env/bin/activate
```

Then install the dependencies:

```sh
pip install -r requirements.txt
```

Env file example:

```sh
SECRET_KEY=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASS=
DATABASE_HOST=
DEBUG=False
```

Then simply apply the migrations:
```sh
python manage.py migrate
```    

Run the server:

```sh
python manage.py runserver
```


