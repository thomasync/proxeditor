import os
import importlib
from .default import Default

files = [
    file
    for file in os.listdir(__name__)
    if file.endswith(".py") and not file.startswith("_") and not file == "default.py"
]

modules = [
    importlib.import_module(f"{__name__}.{file[:-3]}") for file in files
]

hosts = [
    Default()
]
for module in modules:
    hosts.extend(
        [
            getattr(module, cls_name)
            for cls_name in dir(module)
            if isinstance(getattr(module, cls_name), type)
        ]
    )