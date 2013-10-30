Technetium Description
----------------------

Technetium is a data aggregration tool built using the Bitbucket API.

Technetium Features
-------------------
1. Single-page Admin Application for viewing bitbucket data.
2. Simple API calls to grab changesets (including wiki, and issues),
   and any relevant data needed by the user.
3. Visual representations of any and all bitbucket data. Examples include
   line charts which show average commits over a period of time for one
   or more users in a repository.

Technetium Modules
------------------
The following is a list of planned modules:

1. Issues.py : Module for handling all issue related data. This includes (but
   is not limited to):

    - Handling issues based on time issued.
    - Handling issues based on creator/resolver.
    - Handling issues based on type (blocker, etc).

2. Changesets.py: Module for handling all changeset related data. This
   included (but is not limited to):

    - Handling changesets based on date/time created.
    - Handling changesets based on user.

3. Manager.py: Module for handling the repositories that the user is
   interested in.

4. Statistics.py: Module for handling visual representations of all
   aquired data from Bitbucket.

5. Dashboard.py: Module for handling the dashboard views.


Goals/Tasks [ 10/30/13 ---> 11/5/13 ]
-------------------------------------

1. Write tests for subscription methods. [ Albert? Henry?]

2. Create subscription methods. [ Jorge ]
    
      - [A] Create database model for Subscriptions.
      - [B] Write the URL dispatch and the views for repository subscriptions.
      - [C] Write a method for inserting new subscriptions into database.
      - [D] Render the template UI for subscription interface. 

3. Create Changesets view. [ David ]

      - [A] Create template for changesets module.
      - [B] URL dispatch for the view of changesets.
      - [C] Render the template for viewing changesets.


Finished Tasks [10/22/13 --> 10/29/13]
---------------------------------------

1. Work on Bitauth module. [ Jorge, David ]

    - A common method needed for all Bitbucket API calls to be
      successful.

    - STATUS: COMPLETED.

2. Work on Changesets module. [ David ]

    - One of the main modules for Technetium.

    - STATUS: IN PROGRESS.

3. Set up Admin theme on Technetium. [ Albert ]

    - Currently, logging in with Bitbucket returns the user to
      the done page. We would like to return the user to a
      dashboard page. This requires altering the views.py file
      to redirect the user.

    - The admin theme is located here:
      http://startbootstrap.com/templates/sb-admin/


###Future Tasks

#####Manager module
Handles actions allowing the user to add/remove a repository from a list
of desired repositories to track.

#####Methods module
A collection of common methods which will be used across other modules.

Proposed methods:

* Method for getting all repositories that a user has access to.

#####Statistics module
Handles visual representation of bitbucket data in various forms.

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
