from django.core.management.base import BaseCommand
from repertoire.models import Work, File
import csv
import os

class Command(BaseCommand):

    help = 'Digest CSV File'

    def add_arguments(self, parser):

        parser.add_argument('filepath', type=str, help='Indicate the file name')

    def handle(self, *args, **kwargs):

        filepath = kwargs['filepath']
        file_name = os.path.split(filepath)[1]
            
        with open(filepath) as file:

            """
            Read the number of works in document
            """
            File.objects.create(
                filename = file_name,
                work_count = len(file.readlines()) - 1
                )

        with open(filepath) as file:

            """
            Populate database with information extracted from CSV file using the CSV Module
            """
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                Work.objects.create(
                    proprietary_id = row[4],
                    iswc = row[2],
                    source = row[3],
                    title = row[0],
                    contributors = f"[{row[1]}]",
                    file = File.objects.get(filename=file_name)
                    )