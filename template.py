import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    f"personas/engineer.py",
    f"personas/pm.py",
    f"personas/designer.py",
    f"moderator/moderator.py",
    f"utils/prompts.py",
    f"utils/ConversationContext.py",
    f"utils/moderator_utils.py",
    f"utils/summarizer.py",
    "main.py",
    ".env",
    "test.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")