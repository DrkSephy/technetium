Technetium
----------

> [Technetium](http://technetium.herokuapp.com/) is a data aggregation web application built using the Bitbucket API.
It features an all-in-one issue tracker across multiple repositories, along with
both visualization and statistical reports of data pertaining to a repository. **Currently, Technetium only supports generation of reports for Mercurial-based repositories**. 


#### Installation and Running Django

1. Setup and workon your python virtualenv
2. Clone this repository
3. Install python packages: `pip install -r requirements.txt`
4. Sync database and add models: `python manage.py syncdb`
5. Run app server: `python manage.py runserver`
6. Go to: `http://127.0.0.1:8000`

#### Setting up Python Social Auth

You'll need to set the following key-value pairs within `settings.py`:

    SOCIAL_AUTH_BITBUCKET_KEY = ''
	SOCIAL_AUTH_BITBUCKET_SECRET = ''

	BITBUCKET_CONSUMER_KEY = ''
	BITBUCKET_CONSUMER_SECRET = ''

You can learn to get these [keys here](http://django-social-auth.readthedocs.org/en/latest/configuration.html).

#### Setting up PostgreSQL

This project uses PostgreSQL, but you may swap it out for any database of your choice. 

For Linux users (after creating a postgres user on your machine):
	
	$ sudo apt-get install libpq-dev
    $ sudo -u postgres createuser technetium
	[sudo] password for you:

	Shall the new role be a superuser? (y/n) n
	Shall the new role be allowed to create databases? (y/n) y
	Shall the new role be allowed to create more new roles? (y/n) n

	$ psql
	# \password technetium
	Enter new password: ae2cce3603f1913efb36bf39cb20250c
	Enter it again: ae2cce3603f1913efb36bf39cb20250c
	# \q

	$ createdb -U technetium -O technetium technetium

### Unit Testing

1. Go to the `technetium/technetium/bitbucket` directory
2. Run `nosetests -v`
