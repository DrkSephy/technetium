Technetium Description
----------------------

Technetium is a data aggregration tool built using the Bitbucket API.

Please add to this README as you work on this project.

Technetium Features
-------------------
1. Single-page Application for viewing bitbucket data.
2. Simple API calls to grab changesets (including wiki, and issues), 
   and any relevant data needed by the user.


Technetium Modules/Tasks
------------------------
The following is a list of tasks needed to be done:

1. wiki.py (Module for greping all wiki data)
2. repo.py (Module for greping all repo data)
3. changesets.py (Module for greping all changesets)
4. issues.py (Module for greping all changesets)
   `https://github.com/Sheeprider/BitBucket-api`
5. OAuth login page for users of Technetium
   `https://pypi.python.org/pypi/python-social-auth/#auth-providers`
6. A JSON Parser to present API data to user 
7. Front-end stuff (AngularJS? BackboneJS?)
8. 100% code coverage for all modules (PyLint is also recommended) 


###Installation and Running Django
1. Setup and workon your python virtualenv
2. Clone this repository
3. Install python packages: `pip install -r requirements.txt`
4. Run app server: `python manage.py runserver`
5. Go to: `http://127.0.0.1:8000`
