raio=float(input("Digite o raio da sua lata de óleo:"))
altura=float(input ("Digite a altura da sua lata de óleo:"))
from math import pi
area=raio**2*pi
area*=altura
print("O volume da lata de óleo é aproximadamente:",round(area,2))
