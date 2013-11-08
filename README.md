Technetium Description
----------------------

Technetium is a data aggregration tool built using the Bitbucket API.

Technetium is deployed here: [Technetium](http://technetium.herokuapp.com/)

Technetium Features
-------------------
1. Single-page Admin Application for viewing bitbucket data.
2. Simple API calls to grab changesets (including wiki, and issues),
   and any relevant data needed by the user.
3. Visual representations of any and all bitbucket data. Examples include
   line charts which show average commits over a period of time for one
   or more users in a repository.

Goals/Tasks [ 11/5/13 ---> 11/14/13 ]
-------------------------------------
1. Finish subscription functionality. [ Jorge ]

  
      STATUS: In progress.

2. Add AJAX to all requests. [ Jorge ]

      STATUS: In progress.

3. Write tests. [ Albert ]

      STATUS: In progress.

4. Write methods for statistics/reports. [ David ]

      - [A] Method for getting all changeset tallies for a repository.
      - [B] Method for getting all pull request tallies for a repository.
      - [C] Method for getting all closed issues from a repository.
  
      STATUS: In progress.

5. Continue to work on getting proper data for D3 graphs. [ David ]

      - [A] Display all commits for all users in a repository.

Goals/Tasks [ 10/30/13 ---> 11/5/13 ]
-------------------------------------

1. Write tests for subscription methods. [ Albert? Henry?]


2. Create subscription methods. [ Jorge ]
    
      - [A] Create database model for Subscriptions.
      - [B] Write the URL dispatch and the views for repository subscriptions.
      - [C] Write a method for inserting new subscriptions into database.
      - [D] Render the template UI for subscription interface. 
      
      STATUS: COMPLETED.

3. Create Changesets view. [ David ]

      - [A] Create template for changesets module.
      - [B] URL dispatch for the view of changesets.
      - [C] Render the template for viewing changesets.

      STATUS: COMPLETED.

4. Work on Manager module. [ Jorge ]

      - [A] Obtain a list of repositories that a User has access to.
      - [B] Add method for adding/removing repositories to follow.

      STATUS: COMPLETED.

5. Work on Statistics/Graphs module. [ David ]

      - [A] Figure out what input data is needed to use third-party libraries.
      - [B] Obtain data and render through graphs.

      STATUS: In progress.

Finished Tasks [10/22/13 --> 10/29/13]
---------------------------------------

1. Work on Bitauth module. [ Jorge ]

    - A common method needed for all Bitbucket API calls to be
      successful.

    - STATUS: COMPLETED.

2. Work on Changesets module. [ David ]

    - One of the main modules for Technetium.

    - STATUS: COMPLETED.

3. Set up Admin theme on Technetium. [ David ]

    - Currently, logging in with Bitbucket returns the user to
      the done page. We would like to return the user to a
      dashboard page. This requires altering the views.py file
      to redirect the user.

    - The admin theme is located here:
      http://startbootstrap.com/templates/sb-admin/

    - STATUS: COMPLETED.


###Future Tasks

#####Filter module
Handles actions allowing the user to filter issues and changesets.

* Issues can be filtered by user, date, priority, status, and type.
* Changesets can be filtered by user and date.


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
