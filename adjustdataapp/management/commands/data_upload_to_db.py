from django.core.management.base import BaseCommand
from adjustdataapp.models import DataSet
from decimal import Decimal
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        total_row = len(DataSet.objects.all())
        if total_row <= 0:
            with open('dataset.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                row_cnt = 0
                for row in csv_reader:
                    if row_cnt > 0:
                        DataSet(date=row[0],
                                channel=row[1],
                                country=row[2],
                                os=row[3],
                                impressions=int(row[4]),
                                clicks=int(row[5]),
                                installs=int(row[6]),
                                spend=Decimal(row[7]),
                                revenue=Decimal(row[8])).save()
                        row_cnt += 1
                    else:
                        row_cnt += 1
        else:
            print("Database has existing data, do not need initialize...")
