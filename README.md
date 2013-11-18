Technetium
----------

## What is Technetium?


See: [Technetium](http://technetium.herokuapp.com/)

> Technetium is a data aggregation web application built using the Bitbucket API.
It features an all-in-one issue tracker across multiple repositories, along with
both visualization and statistical reports of data pertaining to a repository.

Goals/Tasks [ 11/14/13 --> 11/21/13 ]
-------------------------------------
1. Finish Issue Tracker functionality. [ Jorge ]
    
      - [A] Add functionality to get all issues in all repositories.
      - [B] Finish AJAX calls for the "Show more" option.
          - Ideally, we might want to show 10-20 more issues at a time.

2. Continue working on Reports module (changesets). [ David ]

      - [A] Complete methods for getting commit data.
      - [B] Add functionality to get all changesets in a repository.
      - [C] Write the view, template and URL dispatch for Reports.

3. Work on Reports module (issues). [ Jorge ]

      - [A] Use a method described in TASK [1][A] to get all issues.
            From these issues, extract the number of comments for 
            each user.
      - [B] From the data above, use it to create a tally of all comments.
      - [C] Add functionality to also create a tally of all issues that
            were completed by its assignee.
      - [D] Add functionality to get number of issues opened by each user.
            (Even though the Scrum master is the one who should open 
            issues, this feature is useful in general for other users).

4. Write unit tests. [ Albert ]

      - [A] Continue to write unit tests for anything that isn't 100% 
            covered yet. Start with the filter first.
      - [B] Take a look at application testing using Selenium. Try and see
            if you can write a system test.

5. Using data in TASK [2], display real graphs. [ David ]
      
      - [A] Using methods in TASK[2][B], display a graph using this returned
            data. 
      - [B] Create a Pie Graph with actual data. Requires the following:
          - A Python list of all of the users in the repository.
          - A Python list of all the commits in the repository.
      - [C] Create a line graph with actual data. Requires the following:
          - A Python list of all of the users in the repository.
          - A Python list of all the commits in the repository. 
          - A Python list of all the dates for commits.

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
