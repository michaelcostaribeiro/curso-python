import pandas

squirrel_table = pandas.read_csv('squirrel\Squirrel_Data.csv')

# print(squirrel_table.columns)
#  Gonna need 'Primary Fur Color' and 'Count'

counted_values = squirrel_table['Primary Fur Color'].value_counts()
print(counted_values['Gray'])

squirrel_count = {
    'Fur color' :['Gray','Cinnamon','Black'],
    'Count' : [counted_values['Gray'],counted_values['Cinnamon'],counted_values['Black']]
}

count_data = pandas.DataFrame(squirrel_count)
print(count_data)
count_data.to_csv('./squirrel/squirrel_count.csv')