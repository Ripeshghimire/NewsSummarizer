import yaml
from pathlib import Path
from NewsSummarizer.logger import logging
def read_yaml(yaml_file):
    '''Reads yaml file'''
    with open (yaml_file,'r'):
        yaml_data =  yaml.safe_load(yaml_file)
        logging.info(f"yaml file: {path_to_yaml} loaded successfully")
    return yaml_data