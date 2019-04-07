import os
from assertpy import assert_that
from codegenhelper import init_test_folder, remove_test_folder, test_root, debug, put_folder, put_file
from nose import with_setup
from copy_all import copy_directory

init_test_folder()

def setup_copy_directory():
    put_file('test1.txt', put_folder('folder1', test_root()), '')
    put_file('test2.txt', put_folder('folder1', test_root()), '')
    put_file('test3.txt', put_folder('folder2', os.path.join(test_root(), 'folder1')), '')
    
@with_setup(setup_copy_directory)
def test_copy_directory():
    copy_directory(os.path.join(test_root(), 'folder1'), os.path.join(test_root(), 'folder1-x'))

    assert_that(os.path.join(test_root(), 'folder1-x', 'test1.txt')).exists()
    assert_that(os.path.join(test_root(), 'folder1-x',  'test2.txt')).exists()
    assert_that(os.path.join(test_root(), 'folder1-x', 'folder2', 'test3.txt')).exists()
    
