from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class HelloWorldService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def say_hello(ctx, name):
        return f"Hello, {name}!"

app = Application([HelloWorldService],
                  tns='spyne.examples.hello',
                  in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8000, WsgiApplication(app))
    print("SOAP server listening on http://localhost:8000")
    server.serve_forever()
