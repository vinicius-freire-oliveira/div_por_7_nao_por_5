# Itera sobre todos os números de 5 a 99
for num in range(5, 100):
    # Verifica se o número é divisível por 7 e não é divisível por 5
    if (num % 7 == 0 and num % 5 != 0):
        # Se atender às condições, imprime o número
        print(num)
