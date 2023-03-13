## Django App + DRF

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


