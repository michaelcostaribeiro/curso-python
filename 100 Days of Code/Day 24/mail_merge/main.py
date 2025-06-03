def send_email(name):
    with open(f'./mails/{name.lower()}_mail.txt', 'w') as sending_file:
        with open('./mail_example.txt', 'r') as example_file:
            example = example_file.readlines()
        for i in range(0,len(example)):
            if i == 0:
                sending_file.write(example[i].replace('[name]', name))
            else:
                sending_file.write(example[i])

def get_names():
    with open('./names/invited_names.txt', 'r') as name_file:
        names = name_file.readlines()
        name_records = []
        for i in range(0,len(names)):
            name_records.append(names[i].replace('\n', ''))
        return name_records

name_list = get_names()

print(name_list)

for name in name_list:
    send_email(name)
