#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    # Asynchornous requests
    from gevent import monkey
    monkey.patch_all()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technetium.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
