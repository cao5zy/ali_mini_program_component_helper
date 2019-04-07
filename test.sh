source .env/bin/activate
.env/bin/pylint src/copy_all.py --rcfile pylint.rc
nosetests tests -s --nologcapture -w /Users/tracy/Documents/ali_mini_program_component_helper/src
