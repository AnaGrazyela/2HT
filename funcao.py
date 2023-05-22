def verificar_par():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        return "O número é par"
    else:
        return "O número é Ímpar"
    
resultado = verificar_par()
print(resultado)
