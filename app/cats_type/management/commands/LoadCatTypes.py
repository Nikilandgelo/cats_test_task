from django.core.management.base import BaseCommand, CommandParser
import os
import json
from cats_type.models import CatsType
from django.db import IntegrityError
from django.conf import settings


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('-fn', '--filename', type=str, required=True,
                            help='Name of JSON file with cat types')
    
    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, options.get('filename'))
        if not os.path.isfile(path):
            self.stderr.write(self.style.ERROR(f'File not found: {path}'))
            return

        try:
            with open(path, 'r') as file:
                data: list[dict] = json.load(file)
                if not isinstance(data, list):
                    raise ValueError('Invalid data format, expected a list.')

                CatsType.objects.bulk_create(
                    [CatsType(name=cat_type.get('name')) for cat_type in data]
                )
                return 'Cat types loaded successfully.'
        except (json.JSONDecodeError, ValueError, AttributeError) as err:
            self.stderr.write(self.style.ERROR(
                f'Invalid JSON or data error: {str(err)}'))
        except IntegrityError as err:
            self.stderr.write(self.style.ERROR(f'Database error: {str(err)}'))
