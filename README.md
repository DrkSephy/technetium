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

* Bitgraphs.py (Module for greping graphs of all activities in repos)
* Bitstats.py (Module for greping all code statistics)
* Bitmanager.py (Module for greping all repo data)
* Bitchangesets.py (Module for greping all changesets)
* Bitissues.py (Module for greping all issues)
	`https://github.com/Sheeprider/BitBucket-api`
* Bitfilter.py (Module for filtering changesets and issues)
* Bitdashboard.py (Module for overview page after login)
* A JSON Parser to present API data to user
* Admin UI Bootstrap (already decided to match `http://startbootstrap.com/templates/sb-admin/`) 
* 100% code coverage for all modules (PyLint is also recommended) 


###Installation and Running Django
1. Setup and workon your python virtualenv
2. Clone this repository
3. Install python packages: `pip install -r requirements.txt`
4. Run app server: `python manage.py runserver`
5. Go to: `http://127.0.0.1:8000`
