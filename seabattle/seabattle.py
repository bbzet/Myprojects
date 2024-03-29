import random
import os

letters = "  1 2 3 4 5 6 7   "

name = input("Enter your name: ")
def Search(ar):
    for i in range(len(ar)):
        for j in range(len(ar[i])):
            if ar[i][j] == '1' or ar[i][j] == '2' or ar[i][j] == '3':
                return False
    return True

def out_table(ar):
    counter = 1
    print(letters)
    for i in ar:
        print(chr(counter + 64), end=" ")
        counter += 1
        for j in i:
            print(j, end=' ')
        print()

def place_ships():
    ar = []
    for i in range(7):
        arr = ['•'] * 7
        ar.append(arr)

    flag = True
    while flag is True:
        i = random.randint(0, 6)
        j = random.randint(0, 6)
        dirr = random.randint(1, 2)
        if dirr == 1:
            if 0 < i < 6:
                ar[i][j] = '3'
                ar[i - 1][j] = '3'
                ar[i + 1][j] = '3'
                flag = False
        else:
            if 0 < j < 6:
                ar[i][j] = '3'
                ar[i][j - 1] = '3'
                ar[i][j + 1] = '3'
                flag = False
        if not flag:
            break

    c_ships = 0

    while c_ships != 2:
        flag = True
        while flag is True:
            i = random.randint(0, 6)
            j = random.randint(0, 6)
            dirr = random.randint(1, 2)
            if dirr == 1:
                if ar[i][j] == '•' and i > 0 and ar[i - 1][j] == '•':
                    if j > 0 and ar[i][j - 1] != '•':
                        flag = False
                    if j < 6 and ar[i][j + 1] != '•':
                        flag = False
                    if j > 0 and i > 0 and ar[i - 1][j - 1] != '•':
                        flag = False
                    if j < 6 and i > 0 and ar[i - 1][j + 1] != '•':
                        flag = False
                    if j > 0 and i > 1 and ar[i - 2][j - 1] != '•':
                        flag = False
                    if j < 6 and i > 1 and ar[i - 2][j + 1] != '•':
                        flag = False
                    if i > 1 and ar[i - 2][j] != '•':
                        flag = False
                    if i < 6 and ar[i + 1][j] != '•':
                        flag = False
                    if j > 0 and i < 6 and ar[i + 1][j - 1] != '•':
                        flag = False
                    if j < 6 and i < 6 and ar[i + 1][j + 1] != '•':
                        flag = False

                    if flag:
                        ar[i][j] = '2'
                        ar[i - 1][j] = '2'
                        c_ships += 1

            if dirr == 2:
                if ar[i][j] == '•' and j < 6 and ar[i][j + 1] == '•':
                    if j < 5 and ar[i][j + 2] != '•':
                        flag = False
                    if i < 6 and j < 5 and ar[i + 1][j + 2] != '•':
                        flag = False
                    if j < 5 and i > 0 and ar[i - 1][j + 2] != '•':
                        flag = False
                    if i < 6 and j < 6 and ar[i + 1][j + 1] != '•':
                        flag = False
                    if i < 6 and ar[i + 1][j] != '•':
                        flag = False
                    if i < 6 and j > 0 and ar[i + 1][j - 1] != '•':
                        flag = False
                    if j > 0 and ar[i][j - 1] != '•':
                        flag = False
                    if i > 0 and j > 0 and ar[i - 1][j - 1] != '•':
                        flag = False
                    if i > 0 and ar[i - 1][j] != '•':
                        flag = False
                    if j < 6 and i > 0 and ar[i - 1][j + 1] != '•':
                        flag = False
                    if flag:
                        ar[i][j] = '2'
                        ar[i][j + 1] = '2'

                        c_ships += 1

                if c_ships == 2:
                    break
    c1_ships = 0
    while c1_ships != 4:
        i = random.randint(0, 6)
        j = random.randint(0, 6)
        if ar[i][j] == '•':

            flag = True
            if i > 0 and j > 0 and ar[i - 1][j - 1] != '•':
                flag = False
            if i > 0 and ar[i - 1][j] != '•':
                flag = False
            if i > 0 and j < 6 and ar[i - 1][j + 1] != '•':
                flag = False
            if j < 6 and ar[i][j + 1] != '•':
                flag = False
            if i < 6 and j < 6 and ar[i + 1][j + 1] != '•':
                flag = False
            if i < 6 and ar[i + 1][j] != '•':
                flag = False
            if i < 6 and j > 0 and ar[i + 1][j - 1] != '•':
                flag = False
            if j > 0 and ar[i][j - 1] != '•':
                flag = False

            if flag:
                ar[i][j] = "1"
                c1_ships += 1
        if c1_ships == 4:
            break


    return ar
def inp(ar):
    while True:
        n = input("\nEnter the coordinates, for example: a 1: ")
        n = n.split()
        if len(n) != 2:
            print("Enter only one letter and one digit!")
        else:
            a = n[0].lower()
            b = n[1].lower()
            flag = True
            if not b.isdigit():
                print("Second coordinates must be a digit!")
                flag = False
            elif 1 > int(b) or int(b) > 7:
                print("Second coordinates must be in range 1-7")
                flag = False
            elif not a.isalpha() or ord(a) >= 104 or ord(a) < 97:
                print("First coordinates must be a letter in range a-g")
                flag  = False
            else:

                s1 = ord(a) - 97
                s2 = int(b) - 1
                if ar[s1][s2] == '+' or ar[s1][s2] == '*':
                    print("These coordinates already atacked!")
                else:
                    if flag:
                        break

    return [ord(a) - 97, int(b) - 1]


def isSunk2(ar, i, j):
    if i > 0 and ar[i - 1][j] == '2':
        return False
    if i < 6 and ar[i + 1][j] == '2':
        return False
    if j > 0 and ar[i][j - 1] == '2':
        return False
    if j < 6 and ar[i][j + 1] == '2':
        return False
    return True

def isSunk3(ar, i, j):
    if i > 0 and i < 6 and (ar[i - 1][j] == '3' or ar[i + 1][j] == '3'):
        return False
    if j > 0 and j < 6 and (ar[i][j - 1] == '3' or ar[i][j + 1] == '3'):
        return False
    if i > 1 and (ar[i - 1][j] == '3' or ar[i - 2][j] == '3'):
        return False
    if i < 5 and (ar[i + 1][j] == '3' or ar[i + 2][j] == '3'):
        return False
    if j > 1 and (ar[i][j - 1] == '3' or ar[i][j - 2] == '3'):
        return False
    if j < 5 and (ar[i][j + 1] == '3' or ar[i][j + 2] == '3'):
        return False

    return True


ar = place_ships()
table = []
for i in range(7):
    k = []
    for j in range(7):
        k.append('•')
    table.append(k)

out_table(table)

while True:
    flag = Search(ar)
    if flag:
        break

    lst = inp(ar)
    i = lst[0]
    j = lst[1]

    if ar[i][j] == '2':
        ar[i][j] = '*'
        table[i][j] = '*'
        flag = isSunk2(ar, i, j)
        if flag == False:
            print("HIT")
        else:
            print("SUNK")
    elif ar[i][j] == '3':
        ar[i][j] = '*'
        table[i][j] = '*'
        flag = isSunk3(ar, i, j)
        if flag == False:
            print("HIT")
        else:
            print("SUNK")
    elif ar[i][j] == '1':
        ar[i][j] = '*'
        table[i][j] = '*'
        print("SUNK")
    else:
        table[i][j] = "+"
        print("MISS")
    out_table(table)
    os.system('cls')