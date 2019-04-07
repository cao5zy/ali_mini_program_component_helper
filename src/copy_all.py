import os
import shutil
from assertpy import assert_that


def copy_directory(source_path, target_path):
    return shutil.copytree(source_path, target_path)

def get_target_path(project_path, component_name):
    return os.path.join(os.path.split(project_path)[0], \
                        os.path.split(project_path)[1] + '_' + component_name)

def copy_all(project_path, component_name):
    assert_that(project_path).exists()
    assert_that(is_valid_project(project_path)).is_true()

    def copy(target_path):
        if not os.path.exists(target_path):
            copy_directory(project_path, target_path)

        return lambda init_template: init_template(target_path, component_name)
            


    return copy(get_target_path(project_path, component_name))
