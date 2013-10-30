"""
Run with Django shell:

(venv) $ python manage.py shell
> from technetium.bitbucket import example_bitissues
> example_bitissues.run_issue_1()
"""
import bitmethods
import bitauth
import bitissues

def run_issue_1():
    """
    Runs OAuth authorization to access private
    technetium repository and return JSON of issues.
    """
