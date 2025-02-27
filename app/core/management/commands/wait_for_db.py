"""
Django command to wait for db connection
"""
import time

from django.db import OperationalError
from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available'))
