from xmlrpc.server import SimpleXMLRPCServer

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y if y != 0 else -1

server = SimpleXMLRPCServer(("localhost", 8080))

server.server_activate


# Registrando funções para acesso remoto
server.register_function(soma, "soma")
server.register_function(subtracao, "subtracao")
server.register_function(multiplicacao, "multiplicacao")
server.register_function(divisao, "divisao")

server.serve_forever()