name = input("Enter your name: ")
board = []
counter = 1

print("      BATTLEBOARD      ")
print()

for i in range(1, 8):
    row = ["# "]*7
    board.append(row)

for i in range(1, 8):
    print(" ", i, end='')
    if i == 7:
        print('')
for row in board:
    print(counter, end=" ")
    counter += 1
    for point in row:
        print(point, end=" ")

    print()
