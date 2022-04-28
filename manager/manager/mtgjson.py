from zipfile import ZipFile
from pathlib import Path
import requests
from typing import Optional

FILENAME = 'AllPrintings.sqlite'
ZIP_FILENAME = f'{FILENAME}.zip'

def download_mtgjson(root: Optional[Path] = None, force: bool = False):
    root = root or Path.cwd()
    if force or not (root / FILENAME).exists():
        url = f'https://mtgjson.com/api/v5/{ZIP_FILENAME}'
        with (root / ZIP_FILENAME).open('wb') as file:
            print(f'Downloading {root / ZIP_FILENAME}...')
            file.write(requests.get(url).content)
        if (root / FILENAME).exists():
            print(f'Deleting existing {root / FILENAME}...')
            (root / FILENAME).unlink()
        with ZipFile(root / ZIP_FILENAME, 'r') as zipfile:
            with (root / FILENAME).open('wb') as file:
                print(f'Extraxing {root / FILENAME}...')
                file.write(zipfile.open(FILENAME).read())

if __name__ == '__main__':
    download_mtgjson()