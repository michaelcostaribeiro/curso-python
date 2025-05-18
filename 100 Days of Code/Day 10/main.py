from art import logo

def add(firstNumber, secondNumber):
    return firstNumber + secondNumber

def subtract(firstNumber, secondNumber):
    return firstNumber - secondNumber

def multiply(firstNumber, secondNumber):
    return firstNumber * secondNumber

def divide(firstNumber, secondNumber):
    return firstNumber / secondNumber


def calc(firstNumber):
    operator = input('+\n-\n*\n/\nEscolha um operador: ')
    secondNumber = float(input('Qual é o segundo número?: '))
    match operator:
        case '+':
            result = add(firstNumber, secondNumber)
            calcRender(firstNumber,secondNumber, result)
            return result
        case '-':
            result = subtract(firstNumber, secondNumber)
            calcRender(firstNumber, secondNumber, result)
            return result
        case '*':
            result = multiply(firstNumber, secondNumber)
            calcRender(firstNumber, secondNumber, result)
            return result
        case '/':
            result = divide(firstNumber, secondNumber)
            calcRender(firstNumber, secondNumber, result)
            return result

def calcRender(firstNumber,secondNumber, resultNumber):
    print(f'{firstNumber} + {secondNumber} = {resultNumber}')

print(logo)
wannaContinue = True
clearNumber = ''
primaryNumber = float(input('Qual é o primeiro número?'))
while wannaContinue:
    if clearNumber == 'n':
        print('\n'*100 + logo)
        primaryNumber = float(input('Qual é o primeiro número?'))
    currentNumber = calc(primaryNumber)
    clearNumber = input(f'Digite "s" para continuar calculando com o número {currentNumber}, ou digite "n" para começar um novo cálculo:')
    if clearNumber != 's':
        primaryNumber = 0
    else:
        primaryNumber = currentNumber
