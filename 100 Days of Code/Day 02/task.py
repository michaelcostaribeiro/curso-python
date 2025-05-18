print("Bem vindo à calculadora de gorjetas!")
bill = float(input('Quanto foi o total gasto? '))
tip = int(input('Quanto de gorjeta vocês desejam dar? 10, 12 ou 15? '))
peopleCount = int(input('Quantas pessoas vão dividir a conta? '))

finalValue = round(((bill/100*tip)+bill)/peopleCount,2)
print(f'Cada pessoa pagará: ${finalValue}.')