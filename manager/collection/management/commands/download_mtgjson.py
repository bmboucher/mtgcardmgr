from django.core.management.base import BaseCommand
from typing import Any
from zipfile import ZipFile
from pathlib import Path
import requests

FILENAME = 'AllPrintings.sqlite'
ZIP_FILENAME = f'{FILENAME}.zip'

class Command(BaseCommand):
    help = 'Downloads MTG JSON SQLite database'

    def handle(self, *args: Any, **kwargs: Any):
        root = Path.cwd()
        if (root / ZIP_FILENAME).exists():
            print(f'Deleting existing {root / ZIP_FILENAME}...')
            (root / ZIP_FILENAME).unlink()
        url = f'https://mtgjson.com/api/v5/{ZIP_FILENAME}'
        with (root / ZIP_FILENAME).open('wb') as file:
            print(f'Downloading {root / ZIP_FILENAME}...')
            file.write(requests.get(url).content)
        if (root / FILENAME).exists():
            print(f'Deleting existing {root / FILENAME}...')
            (root / FILENAME).unlink()
        with ZipFile(root / ZIP_FILENAME, 'r') as zipfile:
            with (root / FILENAME).open('wb') as file:
                print(f'Extracting {root / FILENAME}...')
                file.write(zipfile.open(FILENAME).read())
        (root / ZIP_FILENAME).unlink()