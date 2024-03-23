import csv

# Django
from django.core.management.base import BaseCommand, CommandError

# Models
from apps.catalog.models import Catalog


class Command(BaseCommand):
    help = "Save catalogs from csv file."

    def handle(self, *args, **options):
        try:
            with open('catalog.csv', 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    id = int(row['id'])
                    type_id = int(row['type'])
                    code = row.get('code', None)
                    value = row['value']
                    parent_id = row.get('parent', None)
                    description = row.get('description', None)
                    catalog = Catalog(id=id, type_id=type_id, code=code, value=value,
                                      parent_id=parent_id, description=description)
                    catalog.save()
        except Exception as e:
            raise CommandError(f"An error occurred while saving catalogs: {e}")
        self.stdout.write(self.style.SUCCESS("Catalogs saved successfully."))