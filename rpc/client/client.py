import xmlrpc.client

# Conectando ao servidor
proxy = xmlrpc.client.ServerProxy("http://localhost:8080/")

# Chamando funções remotas
print("Soma de 5 + 3:", proxy.soma(5, 3))
print("Subtração de 10 - 4:", proxy.subtracao(10, 4))
print("Multiplicação de 2 * 6:", proxy.multiplicacao(2, 6))
print("Divisão de 8 / 2:", proxy.divisao(8, 2))