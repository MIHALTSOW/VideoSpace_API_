#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys
import subprocess


def refresh_requirements():
    """Install requirements from requirements.txt."""
    if os.path.exists('requirements.txt'):
        subprocess.run("pip freeze > requirements.txt", shell=True, check=True)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VideoSpace_API.settings')

    try:
        from django.core.management import execute_from_command_line

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)




if __name__ == '__main__':
    main()
    refresh_requirements()


