import random

distance = [200, 0, 200, 1, 4, 313, 9]


first_data1 = distance[0]
first_data2 = distance[2]
first_data3 = distance[5]
weight = 0

for _ in range(3):
    valid_input = False
    while not valid_input:
        try:
            kilometers1 = int(input("Enter the kilometer mark where the box can be buried: "))
            if 1 <= kilometers1 <= 7:
                valid_input = True
            else:
                print("Enter numbers between 1 to 7.")
        except ValueError:
            print("Please enter a valid number.")

    kilometers = kilometers1 - 1
    weight += distance[kilometers]

if weight == 713:
    print(f"Congratulations! The weight is {weight} kilograms. You have marked the right locations of cargo.")
else:
    print(f'{weight} kilograms are not the right weight. You marked wrong locations, and the boxes changed their locations. Try it again.')
    random.shuffle(distance)

    weight = 0
