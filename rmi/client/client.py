import Pyro5.api

uri = input("Insira o URI do servidor: ")
calculadora = Pyro5.api.Proxy(uri)  # Conexão com o servidor

print("Soma de 5 + 3:", calculadora.soma(5, 3))
print("Subtração de 10 - 4:", calculadora.subtracao(10, 4))
print("Multiplicação de 2 * 6:", calculadora.multiplicacao(2, 6))
print("Divisão de 8 / 2:", calculadora.divisao(8, 2))