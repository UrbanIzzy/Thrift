'''
Created on 12  2019

@author: LeonidP
'''
import getopt
import logging
import logging.config
import sys

from thrift import transport, protocol
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import Config
import ThriftDemoInterface
from ThriftDemoInterface import CThriftDemoInterface
import ThriftDemoHandler


class ServerEnvelop(object):
    '''
    classdocs
    '''
    def __init__(self, ip, port):
        '''
        Constructor
        '''
        print('Init server')
        self.handler = ThriftDemoHandler.ThriftDemoHandler(None)
        self.processor = ThriftDemoInterface.CThriftDemoInterface.Processor(self.handler)
        self.transport = transport.TSocket.TServerSocket(ip, port)
        self.tfactory = transport.TTransport.TBufferedTransportFactory()
        self.pfactory = protocol.TBinaryProtocol.TBinaryProtocolFactory()

        self.server = TServer.TThreadedServer(self.processor, self.transport, self.tfactory, self.pfactory)
        #self.server = TServer.TSimpleServer(self.processor, self.transport, self.tfactory, self.pfactory)

    def serve(self):
        self.server.serve()

def main():
    print("Welcome to Python Thrift SonicationHal server")
    print('example use: ip=127.0.0.1  port=9091 threads=1 verbose loop=10 array=1000')

    #Config.instance = Config.Config()
    #logFilePath = Config.instance.logFileLocation + "\\SonicationHal-thrift-python.txt"

    #logger = logging.getLogger('sonication')
    #logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    #fh = logging.FileHandler(logFilePath)
    #fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    #ch = logging.StreamHandler()
    #ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #fh.setFormatter(formatter)
    #ch.setFormatter(formatter)
    # add the handlers to the logger
    #logger.addHandler(fh)
    #logger.addHandler(ch)

    #logger.info("Thrift SonicationHalPy server started with arguments: {}".format(sys.argv[1:]))
    #logger.info('default: ip=127.0.0.1  port=9091 threads=1 verbose loop=10 array=1000')

    ip = '127.0.0.1'
    port = 9090
    threads = 1
    verbose = False
    loop = 10
    arraySize = 1000
    try:
        opts, _ = getopt.getopt(sys.argv[1:], 'i:p:t:l:a:v', ['ip=', 'port=', 'threads=', 'loop=', 'array=', 'verbose'])
    except getopt.GetoptError:
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-i', '--ip'):
            ip = arg
        if opt in ('-p', '--port'):
            port = int(arg)
        if opt in ('-t', '--threads'):
            threads = int(arg)
        if opt in ('-l', '--loop'):
            loop = int(arg)
        if opt in ('-a', '--array'):
            arraySize = int(arg)

    print("Start server with ip:{} port:{}".format(ip, port))
    serverInstance  = ServerEnvelop(ip, port)
    serverInstance.serve()

if __name__ == "__main__":
    main()