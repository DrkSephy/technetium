"""
Module for calculating statistics for Bitbucket data.

Proposed methods:

    - Create line/bar/pie charts for issues and changesets data.
    - Create line/bar/pie charts for lines of code added by user.

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