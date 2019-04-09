import os
import shutil

def init_with_template(root_folder, app_name):
    shutil.copytree(os.path.join('./tests/templates', app_name), os.path.join(root_folder, app_name))
