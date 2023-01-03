'''
Created on 5 2019

@author: LeonidP
'''
import sys


#import SonicationDataToLoad_2_FileConverter

class ThriftDemoHandler(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
        #self.logger = logging.getLogger('sonication')

    
    
    def ConfigBlades(self, MyTypeList, MyType):
        print("On ConfigBlades with {} blade confs.".format(len(MyTypeList)))
        #self.logger.info("On ConfigBlades")
        try:
            ''
        except:
            self.logger.info("Exception in ConfigBlades: %s", sys.exc_info()[0])
            return -1
        return 0
        """
        Parameters:
         - BladeConfs

        """
        pass

    def ConfigBladesByJson(self, ConfigJson):
        print(ConfigJson)
        return 0
        """
        Parameters:
         - ConfigJson

        """
        pass

