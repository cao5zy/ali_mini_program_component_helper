from copy_all import copy_all
from init_template import init_template
from get_option import get_option

def main():
    get_option()({
        'template': lambda config: copy_all(config.project_path, config.template_name)(init_template)
    })()


if __name__ == '__main__':
    main()
