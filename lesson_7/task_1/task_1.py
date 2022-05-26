import os
from pathlib import Path


starter = {
    'my_project': [
        'settings',
        'mainapp',
        'adminapp',
        'authapp'
    ]
}

for root_folder, sub_folders in starter.items():
    base_path = Path('.', root_folder).resolve()
    for sub_folder in sub_folders:
        full_path = base_path.joinpath(sub_folder)
        os.makedirs(full_path, exist_ok=True)        


