import string
from Python.ClassExamples import Letters

print(dir(list))
letter_list = []
letter_list2 = [string.ascii_uppercase]
tup_1 = tuple(string.ascii_uppercase)

for s in string.ascii_lowercase:
    letter_list.append(s)

print(letter_list)
print(letter_list2)
print(tup_1)

letter = Letters.Letters
letter.a = letter_list[0]

print(type(letter))
