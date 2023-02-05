import spisok as sp
from random import randint, choice

def Generate():
    name = choice(sp.name_people)
    lastname = choice(sp.lastname_people)
    if name in sp.female_name:
        lastname += 'a'
    age = randint(20, 60)
    address = f'{choice(sp.name_sity)}, {choice(sp.name_street)}, д.{randint(1, 200)}, кв.{randint(1, 200)}'

    return f"'{name}', '{lastname}', '{age}', '{address}'"

table = []
size = 1000

for i in range(size):
    temp = f"INSERT INTO STUDENTS VALUES (NULL, {Generate()});"
    table.append(temp)

for i in table:
    print(i)