# Flask Microservice Boilerplate

An awesome REST boilerplate that uses Flask-RESTX (formerly Flask-RESTPlus).
It has the usual API features to get us started and off the ground,
it's also designed to be easily scalable and extendable.


# Features

* Full-featured framework for fast, easy, and documented API with [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/)
* JSON Web Token Authentication with [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
* Swagger Documentation (Part of Flask-RESTX).
* Unit Testing.
* Database ORM with [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* Database Migrations using [Flask-Migrate](https://github.com/miguelgrinberg/flask-migrate)
* Object serialization/deserialization with [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
* Data validations with Marshmallow [Marshmallow](https://marshmallow.readthedocs.io/en/stable/quickstart.html#validation)


## Flask CLI help command output:

```sh
Usage: flask [OPTIONS] COMMAND [ARGS]...

  A general utility script for Flask applications.

  Provides commands from Flask, extensions, and the application. Loads the
  application defined in the FLASK_APP environment variable, or from a
  wsgi.py file. Setting the FLASK_ENV environment variable to 'development'
  will enable debug mode.

[...]

Commands:
  db      Perform database migrations.
  routes  Show the routes for the app.
  run     Run a development server.
  shell   Run a shell in the app context.
  test    Run unit tests
```


# Pre-requisites

This boilerplate uses `SQLite` as its database, make sure you have it installed.
`Pipenv` is recommended to help manage the dependencies and virtualenv.

You can also use other DBs like `PostgreSQL`, make sure you have it setup and update your 
`DATABASE_URL` in your configs.
Read more at [Flask-SQLAlchemy's](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) documentations.


# Usage

## Notes

By default, the `/` route is used by the `auth` blueprint.

The rest of the resources are found in `/api` (This is the docs route by default, this can be changed easily).

## Installing
```sh
# Clone the repo
$ git clone https://github.com/X1Zeth2X/flask-restx-boilerplate.git

# Install packages with pipenv
$ pipenv install
```

## Running
Please specify your app's environment variables in a `.env` file, otherwise Flask CLI won't find your app.

```sh
# .env file example
SECRET_KEY=UnC@lYub3AoPySykNeB00na!

FLASK_APP=run
FLASK_ENV=development
```

```sh
# Enter the virtualenv
$ pipenv shell

# (Optional for development, recommended)
$ flask db init  # Initializes a new SQLite database.
$ flask db migrate -m "message here"  # Creates the tables in the database.
$ flask db upgrade

# Run the app
$ flask run
```

## Unit testing
This boilerplate has some unit tests written, and I encourage adding more unit tests as you scale.

```sh
# Unit testing
$ flask test

# Run specific unit test(s)
$ flask test tests.test_auth_api tests.test_user_model ...
```