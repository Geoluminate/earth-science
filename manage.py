#!/usr/bin/env python

import os
import sys

if __name__ == "__main__":
    sys.path.append("tests")
    os.environ.setdefault("DJANGO_ENV", "development")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")

    from django.core.management import execute_from_command_line

    # This allows easy placement of apps within the interior
    # project directory.
    # current_path = Path(__file__).parent.resolve()
    # sys.path.append(str(current_path / "tests"))

    execute_from_command_line(sys.argv)
