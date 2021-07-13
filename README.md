# kevr.0cost.org

An *all-in-one* Django web application which implements a portfolio
for [Kevin Morris](https://github.com/kevr).

## Install Dependencies

All dependencies required for this application are contained
in [requirements.txt](requirements.txt):

    $ pip install -I -r requirements.txt

## Configuration

This application uses the `postgresql` Django backend for
database connectivity by default, but supports any type.

See [portfolio/settings.py](portfolio/settings.py) to configure
Django's `DATABASES` dictionary for your personal setup.

## Preparation

Before the web application can be run, a database must be created
and migrated to.

If using our default `postgresql` configuration, you'll need to first create
a role matching your postgres user.
 
Create a role for your specific user with `CREATEDB` permissions.

    $ sudo -u postgres psql -c "CREATE ROLE your_user WITH LOGIN CREATEDB INHERIT"

Once you have a valid role setup, you can create the database and
run Django migrations.

    $ createdb zc_portfolio
    $ python3 manage.py migrate

## Administration

This application uses various database models to keep track of data
about its content. The deployer can create a superuser account
and browse the models through `/admin`.

    $ python3 manage.py createsuperuser

## Serve The App

For development, users can start a local web server with
hot reload capabilities.

    $ python3 manage.py runserver

For production, you'll want to utilize **uwsgi** to run the application,
in addition to:

- Generating a truly secret `SECRET_KEY` for [portfolio/settings.py](portfolio/settings.py).
- Setting `DEBUG` to `False` in [portfolio/settings.py](portfolio/settings.py).

Before you run a server in production, you'll need to collect staticfiles
for **nginx** to use.

    $ python3 manage.py collectstatic

## License

This project operates under the [MIT Public License](LICENSE).

## Authors

| Name         | Email          |
|--------------|----------------|
| Kevin Morris | kevr@0cost.org |
