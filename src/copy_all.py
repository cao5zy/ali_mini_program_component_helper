import os
import shutil
from assertpy import assert_that


def copy_directory(source_path, target_path):
    return shutil.copytree(source_path, target_path)


def copy_all(project_path, component_name):
    assert_that(project_path).exists()
    assert_that(is_valid_project(project_path)).is_true()

    def copy(target_path):
        if not os.path.exists(target_path):
            copy_directory(project_path, target_path)
            
        def cb_init_template(init_template):
            init_template(target_path)

        return cb_init_template

    return copy(get_project_path(project_path, component_name))
