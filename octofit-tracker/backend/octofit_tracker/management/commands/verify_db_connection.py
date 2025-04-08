from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = "Verify the connection to the MongoDB database."

    def handle(self, *args, **kwargs):
        db_conn = connections['default']
        try:
            db_conn.cursor()
            self.stdout.write(self.style.SUCCESS("Successfully connected to the database."))
        except OperationalError as e:
            self.stdout.write(self.style.ERROR(f"Database connection failed: {e}"))