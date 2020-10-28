
dct = (1, 'A, E, I, L, N, O, R, S, T, U',
       2, 'D, G',
       3, 'B, C, M, P',
       4, 'F, H, V, W, Y',
       5, 'K',
       8, 'J, X',
       10, 'Q, Z')

dict1 = {}
for i in range(0, len(dct), 2):
    for el in dct[i + 1].split(', '):
        dict1[el] = dct[i]

chars1 = list(dict1.keys())
chars1.append(' ')
str1 = input('Enter : ')

str1 = str1.upper()
prepared_string = ''.join([c for c in str1 if c in chars1]).split()

for word in prepared_string:
    points = 0
    list_points = []
    for c in word:
        points += dict1[c]
        list_points.append(dict1[c])
    list_points = '+'.join([str(i)for i in list_points])
    print(f'{word} {list_points} = {points}')


