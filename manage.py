#!/usr/bin/env python
import os
import sys
import shutil
import Levenshtein
import errno
sys.path.append('scriptLattes')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "utfpr.settings")


    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)