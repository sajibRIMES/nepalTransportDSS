from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
TEMLATE_DIR = Path(__file__).resolve().parent

print(BASE_DIR)
# os.path.join(TEMLATE_DIR, 'templates/rest_framework')
print(TEMLATE_DIR)