#!/usr/bin/env python
import os
import sys
<<<<<<< HEAD

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projectUtfpr.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
=======
import shutil
import Levenshtein
import errno
sys.path.append('scriptLattes')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "utfpr.settings")


    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
>>>>>>> e75cb122e700f2a2f1b538f220809e0b1802c041
