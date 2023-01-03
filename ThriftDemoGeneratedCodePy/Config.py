import json
import os
from collections import namedtuple


class Config(object):
    '''
    classdocs
    '''
    instance = None

    def __init__(self):
        ''
        instance = self
        dir_path = os.path.dirname(os.path.realpath(__file__))
        config_path = os.path.join(dir_path, 'config.json')
        print("Using conf from: " + config_path)
        with open(config_path, 'r') as file:
            textData = file.read()

        jsonData = json.loads(textData, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        if hasattr(jsonData, 'createBladeFiles'):
            self.createBladeFiles = (jsonData.createBladeFiles == 'true')
        else:
            self.createBladeFiles = False

        if hasattr(jsonData, 'bladeFileLocation'):
            self.bladeFileLocation = jsonData.bladeFileLocation
        else:
            self.bladeFileLocation = 'D:\\'

        if hasattr(jsonData, 'logFileLocation'):
            self.logFileLocation = jsonData.logFileLocation
        else:
            self.logFileLocation = 'D:\\'
