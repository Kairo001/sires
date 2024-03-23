import csv
from apps.catalog.models import Catalog


def save_catalog():
    with open('catalog.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            id = int(row['id'])
            type = int(row['type_id'])
            code = row.get('code', None)
            value = row['value']
            parent = int(row['parent'])
            description = row.get('description', None)
            catalog = Catalog(id=id, type=type, code=code, value=value, parent_id=parent, description=description)
            catalog.save()
