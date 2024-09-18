# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.

def calcular_fatorial(numero):
    if numero < 0:
        return "Fatorial não está definido para números negativos."
    elif numero == 0:
        return 1  # O fatorial de 0 é 1.
    
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i  # Multiplica fatorial pelo próximo número.

    return fatorial

# Recebendo o número do usuário
try:
    numero = int(input("Digite um número inteiro: "))
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é: {resultado}")
except ValueError:
    print("Por favor, digite um número inteiro válido.")