"""
Module for calculating statistics for Bitbucket data.

Charting algorithm workflow:
    1. Write methods for getting the data in the proper form.
    2. For line charts, the input is a CSL (Comma Seperated List)
    3. Pass the data into the views and render it through the 
       templates.

* Might be a good idea to be able to filter the data from a general
  list, this might limit the requests to the server and client-side
  computation.

DAVID'S NOTES
-------------
I took a further look into Bitbucket's API. It provides a method for 
getting the LOC (lines of code) changed for each commit. The resource URL
is: 

GET https://bitbucket.org/api/1.0/repositories/{accountname}/{repo_slug}/
changesets/{node}/diffstat 

Where {node} is the commit number. We can use this to get the statistics on
number of lines of code added by a user on average.

DOWNSIDE: Bitbucket reports that if the DIFF number is too large, then the
JSON will return a NULL value for the LOC added/removed. They do not state a
concrete value for what this value is, so we will have to figure it out through
experiments.

"""