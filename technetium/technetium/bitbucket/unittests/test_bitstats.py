"""
Test Technetium Bitbucket: bitstats
"""

from mock import Mock, patch
import unittest

import technetium.bitbucket.bitstats as bitstats
import technetium.bitbucket.bitmethods as bitmethods

class BitstatsTests(unittest.TestCase):

    def setUp(self):
        # Public user repository
        self.pub_user = 'DrkSephy'
        self.pub_repo = 'smw-koopa-krisis'
        self.data = [{'author': 'Kevin Chan'}, {'author': 'Kevin Chan'}]
        self.data2 = [{'author': 'Kevin Chan'}, {'author': 'DrkSephy'}]
        self.data3 = {'DrkSephy': 29, 'Kevin Chan': 11}
        self.data4 = {'David Leonard': {'changesets': 1}}

    

    def test_commit_counter(self):
        """
        Tests that commit counter returns valid data for single user
        """

        pass
    def test_commit_counter_multiple_users(self):
        """
        Tests that commit counter returns valid data for multiple users
        """
        
        pass

    def test_commit_counter_empty(self):
        """
        Tests that an empty list returns an empty dictionary
        """
        self.assertEqual(bitstats.tally_changesets([]), {})



    def test_list_non_empty_commits(self):
        """
        Tests that a non-empty dictionary returns a list of commits.
        """

        pass
        
    @patch.object(bitmethods, 'send_async_bitbucket_requests')
    def test_parse_issues_for_tallying(self, mock_async):
        self.req_urls = [u'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues?limit=50&start=0', u'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues?limit=50&start=50', u'https://bitbucket.org/api/1.0/repositories/technetiumccny/technetium/issues?limit=50&start=100']
        self.raw_issues = [{
          "count": 104,
          "issues": [
            {
              "status": "new",
              "priority": "major",
              "title": "Download reports as pdf",
              "reported_by": {
                "username": "accountname",
                "first_name": "Jorge",
                "last_name": "Yau",
                "display_name": "Jorge Yau",
                "avatar": "https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/accountname"
              },
              "utc_last_updated": "2013-12-11 02:54:09+00:00",
              "metadata": {
                "kind": "proposal"
              },
              "content": "Following a suggestion made by Grossberg, we may want to consider making reports downloadable in pdf form. It would certainly be very nice.\r\n\r\n[Django pdf tutorial](https://github.com/chrisglass/xhtml2pdf/blob/master/doc/usage.rst)\r\n\r\n[Stackoverflow: html to pdf](http://stackoverflow.com/questions/1377446/html-to-pdf-for-a-django-site)",
              "created_on": "2013-12-11T03:54:09.059",
              "local_id": 104,
              "utc_created_on": "2013-12-11 02:54:09+00:00",
              "resource_uri": "/1.0/repositories/technetiumccny/technetium/issues/104",
   
            }
          ]
        }, 

        {
          "count": 104,
          "filter": {},

          "issues": [
            {
              "status": "resolved",
              "priority": "major",
              "title": "functional test to parse changesets",
              "reported_by": {
                "username": "achieu00",
                "first_name": "Albert",
                "last_name": "Chieu",
                "display_name": "Albert Chieu",

                "avatar": "https://secure.gravatar.com/avatar/b313cc54c8f455f358dc1dda9e302d95?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/achieu00"
              },
              "utc_last_updated": "2013-11-14 13:13:54+00:00",
              "responsible": {
                "username": "DrkSephy",
                "first_name": "David",
                "last_name": "Leonard",
                "display_name": "David Leonard",
           
                "avatar": "https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/DrkSephy"
              },
              "metadata": {
                "kind": "task"
              },
              "content": "",
              "created_on": "2013-11-01T06:03:37.867",
              "local_id": 37,
              "utc_created_on": "2013-11-01 05:03:37+00:00",
              "resource_uri": "/1.0/repositories/technetiumccny/technetium/issues/37"
            }
          ]
        }]
    
        mock_async.return_value = self.raw_issues
        self.auth_tokens = {}
        self.assertEqual(bitstats.parse_issues_for_tallying(self.req_urls, self.auth_tokens), [{'status': 'new', 'opened_by': 'Jorge Yau', 'issue_id': 104, 'assigned': None, 'timestamp': '2013-12-11 02:54:09+00:00'}, {'status': 'resolved', 'opened_by': 'Albert Chieu', 'issue_id': 37, 'assigned': 'David Leonard', 'timestamp': '2013-11-14 13:13:54+00:00'}])

    def test_tally_issue_comments(self):
        self.tallied = {'David Leonard': {'issues_assigned': 23, 'issues_comments': 46, 'issues_opened': 15, 'issues_completed': 20}, 'Albert Chieu': {'issues_assigned': 22, 'issues_comments': 126, 'issues_opened': 79, 'issues_completed': 13}, 'Jorge Yau': {'issues_assigned': 42, 'issues_comments': 42, 'issues_opened': 10, 'issues_completed': 35}}
        self.all_issues = [
          {
            "content": "already decided on http://startbootstrap.com/templates/sb-admin/",
            "author_info": {
              "username": "achieu00",
              "first_name": "Albert",
              "last_name": "Chieu",
              "display_name": "Albert Chieu",
              "avatar": "https://secure.gravatar.com/avatar/b313cc54c8f455f358dc1dda9e302d95?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
              "resource_uri": "/1.0/users/achieu00"
            },
            "comment_id": 6608556,
            "utc_updated_on": "2013-10-24 21:36:47+00:00",
            "utc_created_on": "2013-10-24 21:36:47+00:00",
          },
          {
            "content": "I like the fantastic interface. It is black and simple. My vote (so far) goes to that.",
            "author_info": {
              "username": "accountname",
              "first_name": "Jorge",
              "last_name": "Yau",
              "display_name": "Jorge Yau",
              "avatar": "https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
              "resource_uri": "/1.0/users/accountname"
            },
            "comment_id": 6604308,
            "utc_updated_on": "2013-10-24 18:27:30+00:00",
            "utc_created_on": "2013-10-24 18:27:30+00:00",
          },
          {
            "content": "Here is another fantastic interface: http://startbootstrap.com/templates/sb-admin/",
            "author_info": {
              "username": "DrkSephy",
              "first_name": "David",
              "last_name": "Leonard",
              "display_name": "David Leonard",
              "avatar": "https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
              "resource_uri": "/1.0/users/DrkSephy"
            },
            "comment_id": 6603739,
            "utc_updated_on": "2013-10-24 17:32:22+00:00",
            "utc_created_on": "2013-10-24 17:32:22+00:00",
          },
          {
            "content": "Also, [1] has examples of generating line charts, bar and pie charts using a JavaScript library. Seems perfect to me. ",
            "author_info": {
              "username": "DrkSephy",
              "first_name": "David",
              "last_name": "Leonard",
              "display_name": "David Leonard",
              "avatar": "https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
              "resource_uri": "/1.0/users/DrkSephy"
            },
            "comment_id": 6592608,
            "utc_updated_on": "2013-10-24 02:49:05+00:00",
            "utc_created_on": "2013-10-24 02:49:05+00:00",
          },
          {
            "content": "I personally like [1], but I also like how the sidebar on the left functions in [2]. When you click links in [2], they cascade down to another set of links. I'd love to get that integrated into [1]. Other opinions are welcome.",
            "author_info": {
              "username": "DrkSephy",
              "first_name": "David",
              "last_name": "Leonard",
              "display_name": "David Leonard",
              "avatar": "https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
              "resource_uri": "/1.0/users/DrkSephy"
            },
            "comment_id": 6592563,
            "utc_updated_on": "2013-10-24 02:43:39+00:00",
            "utc_created_on": "2013-10-24 02:43:39+00:00",
          },
          {
            "content": "Also, here is another one which uses Twitter bootstrap: http://demo.onokumus.com/metis/",
            "author_info": {
              "username": "DrkSephy",
              "first_name": "David",
              "last_name": "Leonard",
              "display_name": "David Leonard",
              "avatar": "https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
              "resource_uri": "/1.0/users/DrkSephy"
            },
            "comment_id": 6592534,
            "utc_updated_on": "2013-10-24 02:39:24+00:00",
            "utc_created_on": "2013-10-24 02:39:24+00:00",
          },
          {
            "content": "Here is one very decent UI: https://github.com/VinceG/Bootstrap-Admin-Theme",
            "author_info": {
              "username": "DrkSephy",
              "first_name": "David",
              "last_name": "Leonard",
              "display_name": "David Leonard",
              "avatar": "https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
              "resource_uri": "/1.0/users/DrkSephy"
            },
            "comment_id": 6592531,
            "utc_updated_on": "2013-10-24 02:38:27+00:00",
            "utc_created_on": "2013-10-24 02:38:27+00:00",
          }
        ],
        
        self.assertEqual(bitstats.tally_issue_comments(self.tallied, self.all_issues), {'David Leonard': {'issues_assigned': 23, 'issues_comments': 5, 'issues_opened': 15, 'issues_completed': 20}, 'Albert Chieu': {'issues_assigned': 22, 'issues_comments': 1, 'issues_opened': 79, 'issues_completed': 13}, 'Jorge Yau': {'issues_assigned': 42, 'issues_comments': 1, 'issues_opened': 10, 'issues_completed': 35}})
    
    def test_combine_tallies_empty(self):
        self.issues_tallied =  {'Albert Chieu': {'issues_assigned': 22, 'issues_opened': 79, 'issues_completed': 13}}
        self.changesets_tallied2 = {}
        self.assertEqual(bitstats.combine_tallies(self.changesets_tallied2, self.issues_tallied), 
            {'Albert Chieu': {'issues_assigned': 22, 'changesets': 0, 'issues_opened': 79, 'issues_completed': 13}})

    def test_combine_tally(self):
        self.changesets_tallied = {'David Leonard': {'changesets': 245}, 'accountname': {'changesets': 1}, 'Albert Chieu': {'changesets': 95}, 'Jorge Yau': {'changesets': 321}}
        self.issues_tallied = {'David Leonard': {'issues_assigned': 23, 'issues_comments': 46, 'issues_opened': 15, 'issues_completed': 20}, 'Albert Chieu': {'issues_assigned': 22, 'issues_comments': 126, 'issues_opened': 79, 'issues_completed': 13}, 'Jorge Yau': {'issues_assigned': 42, 'issues_comments': 42, 'issues_opened': 10, 'issues_completed': 35}}
        self.assertEqual(bitstats.combine_tallies(self.changesets_tallied, self.issues_tallied), {'David Leonard': {'issues_assigned': 23, 'changesets': 245, 'issues_comments': 46, 'issues_opened': 15, 'issues_completed': 20}, 'Jorge Yau': {'issues_assigned': 42, 'changesets': 321, 'issues_comments': 42, 'issues_opened': 10, 'issues_completed': 35}, 'Albert Chieu': {'issues_assigned': 22, 'changesets': 95, 'issues_comments': 126, 'issues_opened': 79, 'issues_completed': 13}, 'accountname': {'issues_assigned': 0, 'changesets': 1, 'issues_comments': 0, 'issues_opened': 0, 'issues_completed': 0}})

    def test_combine_tallies(self):
        self.changesets_tallied = {'Albert Chieu': {'changesets': 85}}
        self.issues_tallied =  {'Albert Chieu': {'issues_assigned': 22, 'issues_opened': 79, 'issues_completed': 13}}
        self.assertEqual(bitstats.combine_tallies(self.changesets_tallied, 
            self.issues_tallied), {'Albert Chieu': {'issues_assigned': 22, 'changesets': 85, 'issues_opened': 79, 'issues_completed': 13}})

    def test_tally_changesets(self):

        self.tally = {}
        self.changesets = [{'timestamp': '2013-12-01 06:51:30', 'parsed_author': 'Jorge Yau'}, {'timestamp': '2013-12-01 06:53:34', 'parsed_author': 'Jorge Yau'}, {'timestamp': '2013-12-01 16:50:13', 'parsed_author': 'Jorge Yau'}, {'timestamp': '2013-12-01 17:01:51', 'parsed_author': 'Jorge Yau'}, {'timestamp': '2013-12-01 17:10:55', 'parsed_author': 'Jorge Yau'}]
        self.assertEqual(bitstats.tally_changesets(self.changesets), {'Jorge Yau': {'changesets': 5}})

    def test_tally_issues(self):

        self.tally = {}
        self.issues = [{'status': 'new', 'opened_by': 'Albert Chieu', 'issue_id': 102, 'assigned': 'Jorge Yau', 
            'timestamp': '2013-12-06 05:07:11+00:00'}]
        self.assertEqual(bitstats.tally_issues(self.issues), {'Albert Chieu': {'issues_assigned': 0, 'issues_comments': 0, 'issues_opened': 1, 'issues_completed': 0}, 'Jorge Yau': {'issues_assigned': 1, 'issues_comments': 0, 'issues_opened': 0, 'issues_completed': 0}})


