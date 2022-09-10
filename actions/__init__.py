import importlib
import os

ignore_filenames = ["__init__.py", "__pycache__", "base.py"]

module_names = [
    filename.replace(".py", "")
    for filename in os.listdir("./actions")
    if (filename not in ignore_filenames and filename.endswith(".py"))
]

for module_name in module_names:
    ip = f"actions.{module_name}"
    importlib.import_module(ip)
