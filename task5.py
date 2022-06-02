input_word = input('Input your word: ')
dict1 = dict()
for i in input_word:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1
print(dict1)