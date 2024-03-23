import csv

# Django
from django.core.management.base import BaseCommand, CommandError

# Models
from apps.catalog.models import CatalogType


class Command(BaseCommand):
    help = "Save catalog types from csv file."

    def handle(self, *args, **options):
        try:
            with open('catalog_type.csv', 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    id = int(row['id'])
                    value = row['value']
                    description = row.get('description', None)
                    catalog_type = CatalogType(id=id, value=value, description=description)
                    catalog_type.save()
        except Exception as e:
            raise CommandError(f"An error occurred while saving catalog types: {e}")
        self.stdout.write(self.style.SUCCESS("Catalog types saved successfully."))
