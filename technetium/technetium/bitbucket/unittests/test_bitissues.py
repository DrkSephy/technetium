"""
Test Technetium Bitbucket: bitissues
"""
from mock import Mock, patch, MagicMock
import technetium.bitbucket.bitissues as bitissues
import technetium.bitbucket.bitmethods as bitmethods
import unittest


class BitissuesTests(unittest.TestCase):

    def setUp(self):
        """
        Setup example JSON data returned from bitbucket
        """

        # JSON returned from bitbucket with no assignee
        self.dummy_issues = [{
            'title' : 'issue title',
            'status' : 'new',
            'priority' : 'major',
            'utc_last_updated' : '2013-11-17 10:00:01-0400',

            'metadata' : {
                'kind' : 'task',
            }}]


        # JSON returned from bitbucket with responsible
        self.dummy_issues_assignee = [{
            'title' : 'issue title',
            'status' : 'new',
            'priority' : 'major',
            'utc_last_updated' : '2013-11-17 10:00:01-0400',

            'metadata' : {
                'kind' : 'task',
            },

            'responsible' : {
                'display_name' : 'accountname',
                'avatar' : 'http://mygravatar.com',
            }}]

        self.user = 'DrkSephy'
        self.repo = 'smw-koopa-krisis'
        self.endpoint = 'issues'

    ########################################################
    # get_issues_urls(user, repo, endpoint, end, limit=50) #
    ########################################################
    def test_get_issues_urls_empty(self):
        """
        Tests that we can get urls to send to the issue endpoint.
        """
        self.req_urls = []
        self.end = 0
        self.assertEqual(bitissues.get_issues_urls(self.user, self.repo, self.endpoint,
            self.end, limit=50), self.req_urls )
        
    def test_get_issues_urls_not_empty(self):
        self.req_urls = ['https://bitbucket.org/api/1.0/repositories/DrkSephy/smw-koopa-krisis/issues?limit=50&start=0']
        self.count = 0
        self.limit = 50
        self.end = 50

        self.assertEqual(bitissues.get_issues_urls(self.user, self.repo, self.endpoint,
            self.end, self.limit), self.req_urls)

    #################################
    # parse_all_issues(repo_issues) #
    #################################
    def test_parse_all_issues_empty(self):
        """
        Tests that parse all issues returns blank properly
        """
        self.assertEqual(bitissues.parse_all_issues([]), [])

    def test_parse_all_issues(self):
        """
        Tests that parse all issues returns len of correct size
        """
        self.assertEqual(len(bitissues.parse_all_issues(
            self.dummy_issues)), 1)


    ########################
    # parse_issues(issues) #
    ########################
    def test_parse_issues_empty(self):
        """
        Tests that parse issues on empty dict returns empty list
        """
        self.assertEqual(bitissues.parse_issues({}), [])


    def test_parse_issues_no_assignee(self):
        """
        Tests that parses issues with no assignee returns blank
        """
        self.assertEqual(bitissues.parse_issues(
            self.dummy_issues)[0]['assignee'], '')


    def test_parse_issues_with_assignee(self):
        """
        Tests that parses issues with assignee returns correctly
        """
        self.assertEqual(bitissues.parse_issues(
            self.dummy_issues_assignee)[0]['assignee'], 'accountname')


    ##########################################
    # attach_meta(subscription, repo_issues) #
    ##########################################
    def test_attach_meta_empty(self):
        """
        Tests that bitissues attach_meta returns blank list
        """
        self.assertEqual(bitissues.attach_meta([], []), [])

    def test_attach_meta_subscription(self):
        """
        Tests bitissues attach_meta with subscription
        """
        mock_subscription = Mock()
        mock_subscription.repository = 'Technetium'
        mock_subscription.owner = 'technetiumccny'
        mock_subscription.slug_url = 'http://somebitbucketlink.com'
        list_subscriptions = [mock_subscription]
        self.assertEqual(
            len(bitissues.attach_meta(
                list_subscriptions, self.dummy_issues)), 1)


    def test_get_issue_comments_urls(self):
        self.repo_owner = 'DrkSephy'
        self.repo_slug = 'smw-koopa-krisis'
        self.issues = [{
          "count": 13,
          "filter": {},
          "issues": [
            {
              "status": "resolved",
              "priority": "major",
              "title": "Game entities folder is getting cluttered.",
              "reported_by": {
                "username": "chessmasterhong",
                "first_name": "Kevin",
                "last_name": "Chan",
                "display_name": "Kevin Chan",
                "avatar": "https://secure.gravatar.com/avatar/e62e56bdcbafe6b1ad74a0c646f2d8e6?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/chessmasterhong"
              },
              "utc_last_updated": "2013-10-11 01:53:43+00:00",
              "metadata": {
                "kind": "proposal",

              },
              "content": "As our game continues to grow with new enemies, power-ups, objects, etc., the entities folder (/lib/game/entities) will need to be organized/structured better. During my fixing issues with the enemies, I occasionally find it difficult to identify what is an enemy entity file and what isn't. Much like the /media folder where the enemies are categorized under /media/enemies, sounds under /media/sounds, and so on, I suggest we apply a similar structure to the entities folder.\r\n\r\nFor example:\r\n```\r\n#!\r\n/entities\r\n    /ai (for enemy behaviors)\r\n    /generators (such as snow emitter, leaf generator, etc.)\r\n    /enemies (for the actual enemy entities)\r\n    /powerups (such as green mushrooms, fire flowers, etc.)\r\n    /weapons (such as hammers, fireballs, etc.)\r\n    ...\r\n```",
              "created_on": "2013-10-10T03:57:14.888",
              "local_id": 13,
              "utc_created_on": "2013-10-10 01:57:14+00:00",
              "resource_uri": "/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/13",
            },
            {
              "status": "resolved",
              "priority": "major",
              "title": "Jumping on Enemy damages player as well",
              "reported_by": {
                "username": "DrkSephy",
                "first_name": "David",
                "last_name": "Leonard",
                "display_name": "David Leonard",
                "avatar": "https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/DrkSephy"
              },
              "utc_last_updated": "2013-10-10 02:35:34+00:00",
              "metadata": {
                "kind": "bug",
              },
              "content": "Currently, jumping on almost all enemies will damage the player as well. Needs to be fixed globally.",
              "created_on": "2013-10-06T18:43:07.099",
              "local_id": 12,
              "utc_created_on": "2013-10-06 16:43:07+00:00",
              "resource_uri": "/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/12",
            },
            {
              "status": "resolved",
              "priority": "minor",
              "title": "Two Bird entites dropping bombs in same level",
              "reported_by": {
                "username": "accountname",
                "first_name": "Jorge",
                "last_name": "Yau",
                "display_name": "Jorge Yau",
                "avatar": "https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/accountname"
              },
              "utc_last_updated": "2013-09-29 22:42:45+00:00",
              "responsible": {
                "username": "accountname",
                "first_name": "Jorge",
                "last_name": "Yau",
                "display_name": "Jorge Yau",
                "avatar": "https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/accountname"
              },
              "metadata": {
                "kind": "bug",
              },
              "content": "When you have 2+ Birds on the same level, only one bird spawns bombs.",
              "created_on": "2013-09-28T21:50:53.422",
              "local_id": 11,
              "utc_created_on": "2013-09-28 19:50:53+00:00",
              "resource_uri": "/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/11",
            },
            {
              "status": "resolved",
              "priority": "major",
              "title": "Not destroying PlayerEntity upon death",
              "reported_by": {
                "username": "accountname",
                "first_name": "Jorge",
                "last_name": "Yau",
                "display_name": "Jorge Yau",
                "avatar": "https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/accountname"
              },
              "utc_last_updated": "2013-10-04 16:22:19+00:00",
              "metadata": {
                "kind": "enhancement",
              },
              "content": "Right now when a player dies, that entity gets destroyed.\r\n\r\nThis should be recoded so that the player doesn't actually die. This is because AIs can't recognize a newly spawned player. It would be very WET to make every AI re-recognize the player upon death.\r\n\r\n* Instead when a player dies, lower life counter by 1.\r\n* Set the player's health to max.\r\n* set the player's x and y pos to the checkpoint.\r\n\r\nIf life counter is 0 or less, go to gameover screen.",
              "created_on": "2013-09-28T15:18:32.635",
              "local_id": 10,
              "utc_created_on": "2013-09-28 13:18:32+00:00",
              "resource_uri": "/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/10",
            },
            {
              "status": "resolved",
              "priority": "major",
              "title": "Refactoring code for static entities",
              "reported_by": {
                "username": "accountname",
                "first_name": "Jorge",
                "last_name": "Yau",
                "display_name": "Jorge Yau",
                "avatar": "https://secure.gravatar.com/avatar/b0cff0fe6417101f526780df0af3a56d?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/accountname"
              },
              "utc_last_updated": "2013-10-03 21:44:07+00:00",
              "metadata": {
                "kind": "task",
              },
              "content": "### DRY. Don't repeat yourself. ###\r\n\r\nThere's probably an easier fix rather than creating static files.\r\nIt's JavaScript. You can do anything with it.",
              "created_on": "2013-09-28T04:55:56.035",
              "local_id": 9,
              "utc_created_on": "2013-09-28 02:55:56+00:00",
              "resource_uri": "/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/9",
            },
            {
              "status": "resolved",
              "priority": "major",
              "title": "media folder is getting cluttered",
              "reported_by": {
                "username": "ian_s_mcb",
                "first_name": "Ian",
                "last_name": "McBride",
                "display_name": "Ian McBride",
                "avatar": "https://secure.gravatar.com/avatar/32e3370bc0b40a6ff32bf62448990982?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/ian_s_mcb"
              },
              "utc_last_updated": "2013-09-22 03:13:10+00:00",
              "metadata": {
                "kind": "bug",
              },
              "content": "It would be nice if we divided up the pictures into folders for fb and bg.\r\n\r\nMaybe we could also separate the files that were for testing only. Like 'spike.png or 'slime-grenade.png'\r\n\r\nI would also like it if we followed a consistent naming scheme, like 'firstword_secondword.png' or camel case.",
              "created_on": "2013-09-17T05:10:12.079",
              "local_id": 8,
              "utc_created_on": "2013-09-17 03:10:12+00:00",
              "resource_uri": "/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/8",
            },
            {
              "status": "resolved",
              "priority": "major",
              "title": "Music + sound fx don't always play",
              "reported_by": {
                "username": "ian_s_mcb",
                "first_name": "Ian",
                "last_name": "McBride",
                "display_name": "Ian McBride",
                "avatar": "https://secure.gravatar.com/avatar/32e3370bc0b40a6ff32bf62448990982?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/ian_s_mcb"
              },
              "utc_last_updated": "2013-09-28 03:08:22+00:00",
              "metadata": {
                "kind": "bug",
              },
              "content": "Music + sound fx play once, but never again. No music looping and no repeated playback of sound fx.\r\n\r\nIssue occurs on Linux with Chromium (ver. 25). Doesn't occur with Firefox on Linux, and doesn't occur on Mac. Not sure about windows.\r\n\r\n",
              "created_on": "2013-09-17T02:48:27.362",
              "local_id": 7,
              "utc_created_on": "2013-09-17 00:48:27+00:00",
              "resource_uri": "/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/7",
            },
            {
              "status": "resolved",
              "priority": "major",
              "title": "Camera does not follow player after death",
              "reported_by": {
                "username": "DrkSephy",
                "first_name": "David",
                "last_name": "Leonard",
                "display_name": "David Leonard",
                "avatar": "https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/DrkSephy"
              },
              "utc_last_updated": "2013-09-25 02:39:21+00:00",
              "responsible": {
                "username": "DrkSephy",
                "first_name": "David",
                "last_name": "Leonard",
                "display_name": "David Leonard",
                "avatar": "https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/DrkSephy"
              },
              "metadata": {
                "kind": "bug",
              },
              "content": "After the player dies, the camera does not follow the player on respawn.The player respawns successfully, and can still move (although blindly). Also, the map will not scroll any further if the player moves out of the screen boundary.",
              "created_on": "2013-09-14T17:28:09.871",
              "local_id": 6,
              "utc_created_on": "2013-09-14 15:28:09+00:00",
              "resource_uri": "/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/6",
            },
            {
              "status": "resolved",
              "priority": "minor",
              "title": "Muncher collision glitch",
              "reported_by": {
                "username": "DrkSephy",
                "first_name": "David",
                "last_name": "Leonard",
                "display_name": "David Leonard",
                "avatar": "https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/DrkSephy"
              },
              "utc_last_updated": "2013-09-28 03:38:15+00:00",
              "metadata": {
                "kind": "bug",
              },
              "content": "If the player hits the muncher from the sides, the muncher will slightly move in the direction it was collided with. Should be a simple fix, but currently can't figure out the solution.",
              "created_on": "2013-09-14T17:26:49.127",
              "local_id": 5,
              "utc_created_on": "2013-09-14 15:26:49+00:00",
              "resource_uri": "/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/5",
            },
            {
              "status": "resolved",
              "priority": "major",
              "title": "???",
              "reported_by": {
                "username": "DrkSephy",
                "first_name": "David",
                "last_name": "Leonard",
                "display_name": "David Leonard",
                "avatar": "https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/DrkSephy"
              },
              "utc_last_updated": "2013-09-13 19:31:47+00:00",
              "metadata": {
                "kind": "bug",
              },
              "content": "???",
              "created_on": "2013-09-13T21:31:39.979",
              "local_id": 4,
              "utc_created_on": "2013-09-13 19:31:39+00:00",
              "resource_uri": "/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/4",
            },
            {
              "status": "resolved",
              "priority": "major",
              "title": "Enemy collision",
              "reported_by": {
                "username": "DrkSephy",
                "first_name": "David",
                "last_name": "Leonard",
                "display_name": "David Leonard",
                "avatar": "https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/DrkSephy"
              },
              "utc_last_updated": "2013-09-28 03:37:19+00:00",
              "responsible": {
                "username": "DrkSephy",
                "first_name": "David",
                "last_name": "Leonard",
                "display_name": "David Leonard",
                "avatar": "https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/DrkSephy"
              },
              "metadata": {
                "kind": "bug",
              },
              "content": "Jumping on enemies still does damage to player. Should be a simple fix.",
              "created_on": "2013-09-12T20:09:41.479",
              "local_id": 3,
              "utc_created_on": "2013-09-12 18:09:41+00:00",
              "resource_uri": "/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/3",
            },
            {
              "status": "resolved",
              "priority": "minor",
              "title": "jump attack shouldn't work from below",
              "reported_by": {
                "username": "ian_s_mcb",
                "first_name": "Ian",
                "last_name": "McBride",
                "display_name": "Ian McBride",
                "avatar": "https://secure.gravatar.com/avatar/32e3370bc0b40a6ff32bf62448990982?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/ian_s_mcb"
              },
              "utc_last_updated": "2013-09-28 03:30:03+00:00",
              "metadata": {
                "kind": "bug",
              },
              "content": "At the moment, the player's jump attack not only works from above, but from below too. \r\n\r\nTo see this bug: find an enemy that is on a raised platform, wait for the enemy to reach the edge of the platform, and jump up to the enemy from below.",
              "created_on": "2013-09-08T01:29:13.968",
              "local_id": 2,
              "utc_created_on": "2013-09-07 23:29:13+00:00",
              "resource_uri": "/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/2",
            },
            {
              "status": "resolved",
              "priority": "major",
              "title": "Glitch: Sloped Tiles",
              "reported_by": {
                "username": "DrkSephy",
                "first_name": "David",
                "last_name": "Leonard",
                "display_name": "David Leonard",
                "avatar": "https://secure.gravatar.com/avatar/1aee4f304d9836daa9a69b7e92cdd6ec?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F73a55a25bcb6%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&s=32",
                "resource_uri": "/1.0/users/DrkSephy"
              },
              "utc_last_updated": "2013-10-04 16:20:42+00:00",
              "metadata": {
                "kind": "bug",
              },
              "content": "After creating a new test level using placeholder graphics, it seems that sloped tiles are indeed glitchy. The player interacts with them weird, seemingly floating over them (yet still colliding with them). Will need to be figured out at some point.",
              "created_on": "2013-09-05T23:10:04.928",
              "local_id": 1,
              "utc_created_on": "2013-09-05 21:10:04+00:00",
              "resource_uri": "/1.0/repositories/DrkSephy/smw-koopa-krisis/issues/1",
            }
          ]
        }]
        self.assertEqual(bitissues.get_issue_comments_urls(self.issues, 
            self.repo_owner, self.repo_slug), [])

    ####################################
    # add_html_issue_rows(parsed_data) #
    ####################################
    @patch.object(bitissues, 'render_to_string')
    def test_add_html_issue_rows(self, mock_render_to_string):
        """
        Tests that bitissues add html returns proper html
        """
        self.html = 'includes/issues/issues-list.html'
        self.data = {}
        mock_render_to_string.return_value = {}
        self.assertEqual(bitissues.make_html_issue_rows(self.data), {})
        

    @patch.object(bitmethods, 'make_req_url')
    @patch.object(bitmethods, 'send_bitbucket_request')
    @patch.object(bitissues,  'parse_issues')
    @patch.object(bitissues,  'make_html_issue_rows')
    def test_ajax_process_issues(self, mock_send_bitbucket_request, mock_make_req_url,
        mock_parse_issues, mock_make_html_issue_rows):
        """
        Tests that ajax works on issues.
        """
        self.repo_owner = 'DrkSephy'
        self.repo_slug = 'smw-koopa-krisis'
        self.count = 1
        self.queries = {}
        self.auth_tokens = {}

        mock_make_req_url.return_value = MagicMock()
        mock_send_bitbucket_request.return_value = [{}]
        mock_parse_issues.return_value = MagicMock() 
        mock_make_html_issue_rows.return_value = ''

        self.assertEqual(bitissues.ajax_process_issues(self.auth_tokens, 
            self.repo_owner, self.repo_slug, self.count, self.queries), [{}])
