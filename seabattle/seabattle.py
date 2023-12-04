import random

ar = []
for i in range(7):
    arr = ['•'] * 7
    ar.append(arr)

flag = True
while True:
    i = random.randint(0, 6)
    j = random.randint(0, 6)
    dirr = random.randint(1, 2)
    if dirr == 1:
        if i > 0 and i < 6:
            ar[i][j] = '*'
            ar[i - 1][j] = '*'
            ar[i + 1][j] = '*'
            flag = False
    else:
        if j > 0 and j < 6:
            ar[i][j] = '*'
            ar[i][j - 1] = '*'
            ar[i][j + 1] = '*'
            flag = False
    if not flag:
        break

for i in range(2):
    flag = True
    while True:
        i = random.randint(0, 6)
        j = random.randint(0, 6)
        dirr = random.randint(1, 2)
        if dirr == 1:
            if ar[i][j] == '•' and i > 0 and ar[i - 1][j] == '•':
                if j > 0 and ar[i][j - 1] == '*':
                    flag = False
                if j < 6 and ar[i][j + 1] == '*':
                    flag = False
                if j > 0 and i > 0 and ar[i - 1][j - 1] == '*':
                    flag = False
                if j < 6 and i > 0 and ar[i - 1][j + 1] == '*':
                    flag = False
                if j > 0 and i > 1 and ar[i - 2][j - 1] == '*':
                    flag = False
                if j < 6 and i > 1 and ar[i - 2][j + 1] == '*':
                    flag = False
                if i > 1 and ar[i - 2][j] == '*':
                    flag = False
                if i < 6 and ar[i + 1][j] == '*':
                    flag = False
                if j > 0 and i < 6 and ar[i + 1][j - 1] == "*":
                    flag = False
                if j < 6 and i < 6 and ar[i + 1][j + 1] == "*":
                    flag = False

                if flag:
                    ar[i][j] = '*'
                    ar[i - 1][j] = '*'
        if not flag:
            break
for i in ar:
    for j in i:
        print(j, end=' ')
    print()