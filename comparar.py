#Exercício Python 09: faça um software que verifique entre 2 numeros qual o maior

print("Comparador de números")
numero = float(input("Digite o 1° número: "))
numero2 = float(input("Digite o 2° número: "))
if numero > numero2:
    print(f"O número {numero} é o maior.")
else:
    print(f"O número {numero2} é o maior.")