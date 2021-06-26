sentence = input()
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croa:
    sentence = sentence.replace(i, '*')
print(len(sentence))