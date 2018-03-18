from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/PRC_Tunnel_0',)

#绑定本地端口8888 初始化server
server = SimpleXMLRPCServer(('0.0.0.0', 8888), requestHandler=RequestHandler)


server.register_introspection_functions()
#注册一个多调用组合
server.register_multicall_functions()


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x // y

#注册调用函数,别名特别重要,这个是客户端调用时候的函数名

server.register_function(add, 'add')
server.register_function(subtract, 'subtract')
server.register_function(multiply, 'multiply')
server.register_function(divide, 'divide')

server.serve_forever()
