namespace cpp demo_thrift
namespace csharp demo_thrift
//namespace py demo_thrift

include "MyType.thrift"

service CThriftDemoInterface {
i32 ConfigBlades(1:list<MyType.CMyType> TypeList, 2:MyType.CMyType OneType),
	i32 ConfigBladesByJson(1:string ConfigJson),
}