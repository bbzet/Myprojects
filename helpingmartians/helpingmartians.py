import random
#The first data where cargo were hidden
distance = [200, 0, 200, 1, 4, 313, 9]

#The first locations by index
first_data1 = distance[0]
first_data2 = distance[2]
first_data3 = distance[5]
weight = 0

#Function that checked the weight
def checking_mark(weight):
    if weight == 713:
        return "YES"
    else:
        return "NO"

#Inputed data and checked operations
r = True
while r:
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
#The final result
    if checking_mark(weight) == "YES":
        print(f"Congratulations! The weight is {weight} kilograms. You have marked the right locations of cargo.")
        r = False
    elif checking_mark(weight) == "NO":
        print(f'{weight} kilograms are not the right weight. You marked wrong locations, and the boxes changed their locations. Try it again.')
        random.shuffle(distance)

        weight = 0