import os
from pathlib import Path
import shutil


project_path = Path().resolve().joinpath('my_project')

for root, dirs, files in os.walk(project_path):
    if root.endswith('templates'):
        shutil.copytree(root, project_path.joinpath('templates'), dirs_exist_ok=True)        

