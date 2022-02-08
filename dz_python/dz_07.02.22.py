import json
from random import choice


def gen_persom():
    name = ''
    tel = ''
    letters = ['a', "b", 'b', 'd', 'e', 'f', 'e', 'g']
    num = [str(j) for j in range(10)]

    while len(name) != 7:
        name += choice(letters)
    while len(tel) != 11:
        tel += choice(num)
    person = {'name': name, "tel": tel}
    return person


def write_json(person_dict):
    try:
        data = json.load(open('person.json'))
    except FileNotFoundError:
        data = {}
    data.update(person_dict)
    with open('person.json', 'w') as f:
        json.dump(data, f, indent=5)


person2 = {}
for i in range(5):
    gen_persom()
    person2[i] = (gen_persom())

print(person2)

write_json(person2)
