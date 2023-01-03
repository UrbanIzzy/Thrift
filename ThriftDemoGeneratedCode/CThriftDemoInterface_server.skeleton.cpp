// This autogenerated skeleton file illustrates how to build a server.
// You should copy it to another filename to avoid overwriting it.

#include "CThriftDemoInterface.h"
#include <thrift/protocol/TBinaryProtocol.h>
#include <thrift/server/TSimpleServer.h>
#include <thrift/transport/TServerSocket.h>
#include <thrift/transport/TBufferTransports.h>

using namespace ::apache::thrift;
using namespace ::apache::thrift::protocol;
using namespace ::apache::thrift::transport;
using namespace ::apache::thrift::server;

class CThriftDemoInterfaceHandler : virtual public CThriftDemoInterfaceIf {
 public:
  CThriftDemoInterfaceHandler() {
    // Your initialization goes here
  }

  int32_t ConfigBlades(const std::vector< ::sonicationhal_thrift::CMyType> & TypeList, const  ::sonicationhal_thrift::CMyType& OneType) {
    // Your implementation goes here
    printf("ConfigBlades\n");
  }

  int32_t ConfigBladesByJson(const std::string& ConfigJson) {
    // Your implementation goes here
    printf("ConfigBladesByJson\n");
  }

};

int main(int argc, char **argv) {
  int port = 9090;
  ::apache::thrift::stdcxx::shared_ptr<CThriftDemoInterfaceHandler> handler(new CThriftDemoInterfaceHandler());
  ::apache::thrift::stdcxx::shared_ptr<TProcessor> processor(new CThriftDemoInterfaceProcessor(handler));
  ::apache::thrift::stdcxx::shared_ptr<TServerTransport> serverTransport(new TServerSocket(port));
  ::apache::thrift::stdcxx::shared_ptr<TTransportFactory> transportFactory(new TBufferedTransportFactory());
  ::apache::thrift::stdcxx::shared_ptr<TProtocolFactory> protocolFactory(new TBinaryProtocolFactory());

  TSimpleServer server(processor, serverTransport, transportFactory, protocolFactory);
  server.serve();
  return 0;
}

