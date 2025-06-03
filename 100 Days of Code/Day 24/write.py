f = open('demofile.txt')
print(f.read(5))
f.close()
with open('demofile.txt') as t:
    test = t.read(-1)
print(test+test+test)

with open('../../../../../../OneDrive/Área de Trabalho/writing_text.txt', 'w') as file:
    file.write('writing test')