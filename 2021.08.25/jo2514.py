word = input()
KOI = 0
IOI = 0

for i in range(len(word) - 2):
    if word[i:i+3] == 'KOI':
        KOI += 1
    elif word[i:i+3] == 'IOI':
        IOI += 1

print(KOI)
print(IOI)