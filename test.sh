source .env/bin/activate
.env/bin/pylint src/copy_all.py \
		src/get_target_directory.py --rcfile pylint.rc
nosetests tests -s --nologcapture -w ~/projects/ali_mini_program_component_helper/src
