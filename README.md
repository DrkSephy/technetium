Technetium
----------

## What is Technetium?


See: [Technetium](http://technetium.herokuapp.com/)

> Technetium is a data aggregation web application built using the Bitbucket API.
It features an all-in-one issue tracker across multiple repositories, along with
both visualization and statistical reports of data pertaining to a repository.

Goals/Tasks [ 11/21/13 --> 11/14/13 ]
-------------------------------------
1. Continue working on Reports module. [ Jorge ]
    - [A] Write methods for handling all issues. With these issues, we need to:
        - Get all the issues that were opened by a user.
        - Get all the issues that were completed by a user.
        - Get the number of comments that users have made in a repository.

2. Finish the graphs for Technetium. [ David ]
    - [A] Write the last methods for getting more data for graphs.
    - [B] Update existing graphs with real data using existing methods.

3. Start the Sphinx Documentation. [ David ]

4. Write Application Tests. [ Albert ]

5. Write unit test code. [ Albert, David, Jorge ]
    - [A] Everyone can pitch in and contribute to test code.

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
