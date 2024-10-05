from django.core.management.base import BaseCommand, CommandParser
from django.core.management import call_command
import os
from django.conf import settings
import json
from User.models import User
from cats.models import Cat
from cats_type.models import CatsType
from django.db import IntegrityError
import random
from django.db import transaction


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('-fn', '--filename', type=str, required=True,
                            help='Name of JSON file with test data')
    
    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, options.get('filename'))
        if not os.path.isfile(path):
            self.stderr.write(self.style.ERROR(f'File not found: {path}'))
            return
        
        try:
            with transaction.atomic():
                self.stderr.write(self.style.SUCCESS(
                    'Loading cat types from JSON...'))
                status_cat_types: str | None = call_command(
                    'LoadCatTypes', filename='cat_types.json')
                if status_cat_types is None:
                    raise RuntimeError

                with open(path, 'r') as file:
                    data: dict[str, list] = json.load(file)
                    if not isinstance(data, dict):
                        raise ValueError(
                            'Invalid data format, expected a dict.')
                    users: list[User] = [
                        User.objects.create_user(
                            username=user[0], password=user[1])
                        for user in data.get('users')]
                    all_types = CatsType.objects.all()
                    Cat.objects.bulk_create(
                        [Cat(**cat,
                            owner=random.choice(users),
                            type=random.choice(all_types))
                        for cat in data.get('cats')]
                    )
                    self.stderr.write(self.style.SUCCESS(
                        'Users and cats loaded successfully.'))
        except RuntimeError as err:
            pass
        except (json.JSONDecodeError, ValueError) as err:
            self.stderr.write(self.style.ERROR(
                f'Invalid JSON or data error: {str(err)}'))
        except IndexError as err:
            self.stderr.write(self.style.ERROR(
                f'Error when loading users or cats types: ' + str(err)))
        except IntegrityError as err:
            self.stderr.write(self.style.ERROR(f'Database error: {str(err)}'))
