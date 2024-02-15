# Projet 7 : Le trieur de fichiers

from pathlib import Path

# Create dictionnary to map extensions with folders
dirs = {
    'mp3': 'Musique',
    'wav': 'Musique',
    'flac': 'Musique',
    'avi': 'Videos',
    'mp4': 'Videos',
    'gif': 'Videos',
    'bmp': 'Images',
    'png': 'Images',
    'jpg': 'Images',
    'txt': 'Documents',
    'pptx': 'Documents',
    'csv': 'Documents',
    'xls': 'Documents',
    'odp': 'Documents',
    'pages': 'Documents'
}

# Create folder constants
SOURCE_FILE = Path(__file__).resolve()
SOURCE_PATH = SOURCE_FILE.parent
DATA_DIR = SOURCE_PATH / 'sources-p7/data'

# List all files in 'DATA_DIR'
files = [f for f in DATA_DIR.iterdir() if f.is_file()]

# Move all files in 'files' according to their extension
for f in files:
    output_dir = DATA_DIR / dirs.get(f.suffix[1:], 'Autres')
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / '.' / f.name)