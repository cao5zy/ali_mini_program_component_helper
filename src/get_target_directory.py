import os

def get_target_components_path(root):
    return os.path.join(root, 'components')

def get_target_directory_with_components(root, template_name):
    return os.path.join(get_target_components_path(root), template_name)

def get_target_directory_directly(root, template_name):
    return os.path.join(root, template_name)
    
def get_target_directory(template_name, root=os.getcwd()):
    return (lambda path: [None] if os.path.exists(path) else [path]) \
        (get_target_directory_with_components(root, template_name) \
         if os.path.exists(get_target_components_path(root)) \
         else get_target_directory_directly(root, template_name))
