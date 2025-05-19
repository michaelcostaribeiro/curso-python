from prettytable import PrettyTable

tabela = PrettyTable()

tabela.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
tabela.add_column('Type', ['Electric', 'Water', 'Fire'])
tabela.align = 'l'
print(tabela)
print(tabela.get_string(fields=['Type']))