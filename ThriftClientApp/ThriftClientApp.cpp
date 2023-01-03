// ThriftClientApp.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#pragma once
#include <string>
#include <memory>
#include <thrift/protocol/TBinaryProtocol.h>
#include <thrift/transport/TSocket.h>
#include <thrift/transport/TTransport.h>
#include <thrift/transport/TTransportUtils.h>
#include <ThriftDemoGeneratedCode/CThriftDemoInterface.h>


int main()
{
	std::shared_ptr<apache::thrift::transport::TSocket> socket;
	std::shared_ptr<apache::thrift::transport::TTransport> bufferedTransport;
	std::shared_ptr<apache::thrift::protocol::TProtocol> protocol;
	std::shared_ptr<demo_thrift::CThriftDemoInterfaceClient> client;

	try {

		socket.reset(new apache::thrift::transport::TSocket("127.0.0.1", 9090));
		bufferedTransport.reset(new apache::thrift::transport::TBufferedTransport(socket, 100000));
		protocol.reset(new apache::thrift::protocol::TBinaryProtocol(bufferedTransport));
		client.reset(new demo_thrift::CThriftDemoInterfaceClient(protocol));
		bufferedTransport->open();
		client->ConfigBladesByJson("my json");
	}
	catch (apache::thrift::TApplicationException& tx) {
		if (tx.getType() == apache::thrift::TApplicationException::INTERNAL_ERROR)
		{
			std::string error = std::string(tx.what()) + ". May be server's handler is not updated";
			//::AfxMessageBox(CString(error.c_str()));
			return false;
		}
		//::AfxMessageBox(CString(tx.what()));
		return false;
	}
	catch (apache::thrift::TException& tx) {
		//::AfxMessageBox(CString(tx.what()));
		return false;
	}
	catch (const std::exception&ex)
	{
		//::AfxMessageBox(CString(ex.what()));
		return false;
	}

	//client->PreloadBlades();


    return 0;
}

