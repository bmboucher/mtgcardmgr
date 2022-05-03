from optparse import Option
from zipfile import ZipFile
from pathlib import Path
import requests
from typing import Optional

import sqlite3

FILENAME = 'AllPrintings.sqlite'
ZIP_FILENAME = f'{FILENAME}.zip'

def download_mtgjson(root: Optional[Path] = None):
    root = root or Path.cwd()
    if (root / ZIP_FILENAME).exists():
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

_db: Optional[sqlite3.Connection] = None
def get_mtgjson_db(root: Optional[Path] = None):
    global _db
    if not _db:
        root = root or Path.cwd()
        if not (root / FILENAME).exists():
            download_mtgjson(root)
        _db = sqlite3.Connection(root / FILENAME)
        _db.row_factory = sqlite3.Row
    return _db

def get_cards(root: Optional[Path] = None):
    cursor = get_mtgjson_db(root).cursor().execute('SELECT name, setCode, number, uuid FROM Cards')
    return [{
        'name': row['name'],
        'code': f"{row['setCode']}/{row['number']}",
        'uuid': row['uuid']
    } for row in cursor]

if __name__ == '__main__':
    download_mtgjson()