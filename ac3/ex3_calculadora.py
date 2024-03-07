"""
Exercício 3: calculadora simples
Desenvolva funções de operações aritméticas soma, subtracao, multiplicacao e divisao, 
que recebem dois números cada uma e retornam o resultado da operação indicada. 
Em seguida, crie uma função que elabora uma interface por linha de comando (CLI), 
que lê dois números e uma operação e exibe na tela o valor do resultado, ou exibe "operação inválida" 
se o usuário inserir uma mensagem diferente das quatro operações.

Exemplos
Informe um número: 5.5
Informe outro número: 10
Informe a operação: soma
Resultado: 15.5
Informe um número: 5.5
Informe outro número: 10
Informe a operação: multiplicação
Resultado: 55.0
Informe um número: 5.5
Informe outro número: 10
Informe a operação: abcd
operação inválida
"""

def calculadora(a = int(input("Informe um número: ")), b = int(input("Informe outro número: ")), operacao = input("Informe a operação: ")):
    match operacao:
        case "soma":
            return a + b
        case "subtração" | "subtracao":
            return a - b
        case "multiplicação" | "multiplicacao":
            return a * b
        case "divisão" | "divisao":
            return a / b
        case _:
            return "Operação Inválida"

def testa_calculadora():
    print(calculadora())

testa_calculadora()