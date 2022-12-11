# Média Aritmética:

valor1 = float(input("Digite um valor:"))
valor2 = float(input("Digite um valor:"))
valor3 = float(input("Digite um valor:"))
valor4 = float(input("Digite um valor:"))
media = (valor1 + valor2 + valor3 + valor4)/ 4
print(" A média arimética dos valores é", media)
media = 0

# Média ponderada:

valor1 = float(input("Digite um valor:"))
valor2 = float(input("Digite um valor:"))
valor3 = float(input("Digite um valor:"))
valor4 = float(input("Digite um valor:"))
peso = float(input("Digite um peso:"))
media = ((valor1 * peso) + (valor2 * peso) + (valor3 * peso) + (valor4 * peso)/(peso * 4))
print("A média ponderada é:", media)
