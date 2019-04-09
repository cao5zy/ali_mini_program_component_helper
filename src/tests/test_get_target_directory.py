import os
import shutil
from get_target_directory import get_target_directory
from assertpy import assert_that
from codegenhelper import init_test_folder, remove_test_folder, test_root, debug, put_folder, put_file
from nose import with_setup
from util import init_with_template

init_test_folder()
    
    
def init_get_target_directory():
    init_with_template(test_root(), 'template_app')

@with_setup(init_get_target_directory, remove_test_folder)
def test_get_target_directory():
    assert_that(get_target_directory('componentA', os.path.join(test_root(), 'template_app'))).contains('.test/template_app/components/componentA')
    
