import json
import pandas as pd
from django.db import transaction
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.apps import apps

from backend_core.models import Student

class Command(BaseCommand):
    help = 'Import Students from sheet'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str,  nargs='+', help='Name of the app')
    def get_records(self, filename):
        base_dir = settings.BASE_DIR.parent
        file_path = f"{base_dir}/{filename}"
        df = pd.read_excel(file_path, index_col=0)
        df.fillna('None', inplace=True)
        records=df.to_dict('records')
        return records
    def populate_db(self, data):
        bulk_list = list()
        for d in data:
            student = Student(**d)
            bulk_list.append(student)
        Student.objects.bulk_create(bulk_list)

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        print(filename)
        for file in filename:
            records = self.get_records(file)
            self.populate_db(records)

        try:
            print("jbkjdfk")
        except Exception as e:
            print(e)
