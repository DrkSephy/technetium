Technetium
----------

## What is Technetium?


> [Technetium](http://technetium.herokuapp.com/) is a data aggregation web application built using the Bitbucket API.
It features an all-in-one issue tracker across multiple repositories, along with
both visualization and statistical reports of data pertaining to a repository.


#### Installation and Running Django

1. Setup and workon your python virtualenv
2. Clone this repository
3. Install python packages: `pip install -r requirements.txt`
4. Sync database and add models: `python manage.py syncdb`
5. Run app server: `python manage.py runserver`
6. Go to: `http://127.0.0.1:8000`


### Unit Testing

1. Go to the `technetium/technetium/bitbucket` directory
2. Run `nosetests -v`
