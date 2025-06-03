import pandas

table = pandas.read_csv('./weather_data.csv')

# print(table)
# print(table.max())

# table_list = table['temp'].to_list()
# print(table_list)
# print(table['temp'].mean())


# print(table[table.temp == table.temp.max()])

monday = table[table.day == 'Monday']
print((monday.temp*9/5)+32)