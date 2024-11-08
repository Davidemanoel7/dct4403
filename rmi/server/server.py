import Pyro5.api

@Pyro5.api.expose
class Calculadora:
    def soma(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y

    def multiplicacao(self, x, y):
        return x * y

    def divisao(self, x, y):
        if y != 0:
            return x / y
        else:
            return-1

# Inicialização do servidor
daemon = Pyro5.server.Daemon()
uri = daemon.register(Calculadora)
print(f"URI da calculadora: {uri}")
daemon.requestLoop()