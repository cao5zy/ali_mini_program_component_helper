from fn import F, _

def main():
    (F(get_target_directory) >> \
     F(filter, _ is not None) >> \
     F(map, generate_template))()

    
