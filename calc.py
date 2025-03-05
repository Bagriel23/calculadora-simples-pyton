def calculator():
    while True:
        print("Calculadora simples")
        print()
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("s - Sair.")
        operation = input("Selecione uma opção ou 's' para sair: ")

        if operation == 's' or operation == 'S':
            print("Obrigado por usar a calculadora simples!")
            break

        if operation not in ['1', '2', '3', '4']:
            print("Opção inválida! Tente novamente.")
            continue

        n1 = float(input("Primeiro valor: "))
        n2 = float(input("Segundo valor: "))

        if operation == '1':
            result = n1 + n2
            print("O resultado da soma é: ", result)

        elif operation == '2':
            result = n1 - n2
            print("O resultado da subtração é: ", result)

        elif operation == '3':
            result = n1 * n2
            print("O resultado da multiplicação é: ", result)

        else:
            if n2 == 0:
                print("Divisões por 0 não são possíveis. Tente novamente.")
                continue
            else:
                result = n1 / n2
                print("O resultado da divisão é: ", result)

calculator()