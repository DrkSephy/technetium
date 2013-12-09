Technetium
----------

## What is Technetium?


See: [Technetium](http://technetium.herokuapp.com/)

> Technetium is a data aggregation web application built using the Bitbucket API.
It features an all-in-one issue tracker across multiple repositories, along with
both visualization and statistical reports of data pertaining to a repository.

Goals/Tasks [ 12/05/13 --> 12/12/13 ]
-------------------------------------
1. Render Issue Comments on Reports page. [ Jorge ]
    - Create the method needed for getting the comment data.
    - Write a parser method and tally method for this data.
    - Lastly, render the comments on the reports. 
        - Possibly put a spinning progress bar in that spot to denote loading time.

2. Update our PyLint scores to be as high as possible. [ Albert ]


3. Finish up unit testing. [ David ]


###Installation and Running Django
1. Setup and workon your python virtualenv
2. Clone this repository
3. Install python packages: `pip install -r requirements.txt`
4. Sync database and add models: `python manage.py syncdb`
5. Run app server: `python manage.py runserver`
6. Go to: `http://127.0.0.1:8000`


###Unit Testing
1. Go to the 'technetium/technetium/bitbucket' directory
2. Run `nosetests -v`
