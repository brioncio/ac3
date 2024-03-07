"""
Exercício 1: triângulos
Desenvolva uma função determina_tipo_triangulo que recebe três lados de um triângulo 
e retorna uma string, "Escaleno", "Isósceles" ou "Equilátero", conforme o tipo do triângulo. 
A função deve retornar "Não é um triângulo" se os três lados não formarem um triângulo. 
Use a função abaixo como teste:

def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo
"""

def testa_triangulo(l1, l2, l3):

    if l1 - l2 > l3 or l1 + l2 < l3:
        return "Não é um triângulo"
    if l1 == l2 != l3 or l1 != l2 == l3 or l1 == l3 != l2:
        return "Isósceles"
    if l1 == l2 == l3:
        return "Equilátero"
    if l1 != l2 != l3:
        return "Escaleno"
    
def main():
    print(testa_triangulo(4,4,4))
    print(testa_triangulo(2,4,4))
    print(testa_triangulo(3,4,5))
    print(testa_triangulo(1,1,4))

main()