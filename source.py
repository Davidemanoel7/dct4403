# Funcoes  a  disponibilizar  como  servico
def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return -1

if __name__== "__main__":
    x = float(input("Informe o primeiro numero: "))
    y = float(input("Informe o segundo numero: "))

    print("Soma: %f" % soma(x, y))
    print("Subtracao: %f" % subtracao(x, y))
    print("Multiplicacao: %f" % multiplicacao(x, y))
    print("Divisao: %f" % divisao(x, y))