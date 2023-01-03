@echo  ""
@echo  ""
@echo Generating SonicationHalServer c++ thrift client-server...
%THRIFT_COMPILER_HOME%\thrift-0.12.0.exe -r -o ..\ThriftDemoGeneratedCode --gen cpp ThriftDemoInterface.thrift

@echo Generating SonicationHalServer py thrift client-server...
%THRIFT_COMPILER_HOME%\thrift-0.12.0.exe -r -out ..\ThriftDemoGeneratedCodePy --gen py ThriftDemoInterface.thrift
@echo  ""
@echo Done.