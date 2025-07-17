from pathlib import Path
import logging
import os

files = [
    "src/__init.py__",
    "src/helper.py",
    "templates/chat.html",
    "static/style.css",
    "src/prompt.py",
    "research/snippets.ipynb",
    "setup.py",
    ".env",
    "requirements.txt",
    "app.py",
    "store_index.py"
]

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

for filepath in files:
    filepath = Path(filepath)
    dir, file = os.path.split(filepath)

    if dir != "":
        os.makedirs(dir, exist_ok=True)
        logging.info(f"Creating directory: {dir} for the file: {file}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"File already exist: {file}")