from xmlrpc.client import ServerProxy, Error
import xmlrpc.client

#连接远程的rpc服务器
with ServerProxy("http://127.0.0.1:8888/PRC_Tunnel_0") as proxy:
    print(proxy)
    #
    multicall = xmlrpc.client.MultiCall(proxy)

    try:
        #
        print(proxy.subtract(1024, 2048))
        #
        multicall.add(23, 28)
        multicall.subtract(23, 28)
        result = multicall()
        print("23+28=%d, 23-28=%d" % tuple(result))

    except Error as v:
        print("Error", v)
