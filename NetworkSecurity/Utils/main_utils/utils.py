import yaml
from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.Logger.logger import logging
import numpy as np
import os,sys
import dill
import pickle

def read_yaml_file(file_path:str) -> dict:

    with open(file_path, 'rb') as yaml_file:
        return yaml.safe_load(yaml_file)
    
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
            
    except Exception as e:
        raise NetworkSecurityException(e, sys)