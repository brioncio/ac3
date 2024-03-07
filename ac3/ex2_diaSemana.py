"""
Exercício 2: dia da semana
Desenvolva uma função dia_semana que recebe um número inteiro e 
retorna uma string indicando o dia da semana equivalente, 
considerando que o dia da semana igual a 1 é o domingo, 2 é segunda-feira, etc. 
A função deve retornar uma string vazia caso o número seja inválido. 
Use a função abaixo como teste:

def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia
"""

def dia_semana(num):
    match num:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda-Feira"
        case 3:
            return "Terça-Feira"
        case 4:
            return "Quarta-Feira"
        case 5:
            return "Quinta-Feira"
        case 6:
            return "Sexta-Feira"
        case 7:
            return "Sábado"
        case _:
            return " "
        
def testa_dia_semana():
    print(dia_semana(2))
    print(dia_semana(4))
    print(dia_semana(1))
    print(dia_semana(7))
    print(dia_semana(9))

testa_dia_semana()