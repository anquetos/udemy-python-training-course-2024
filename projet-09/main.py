# Projet 9 : organiser des données

from pathlib import Path

CURRENT_DIR = Path(__file__).parent.absolute()
SOURCE_FILE = CURRENT_DIR / 'prenoms-a-nettoyer.txt'
DEST_FILE = CURRENT_DIR / 'prenoms-final.txt'

with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
    read_data = f.read()

first_names_raw_list = read_data.split()

cleaned_first_names = [first_name.strip('., ') for first_name in first_names_raw_list]

with open(DEST_FILE, 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(cleaned_first_names)))