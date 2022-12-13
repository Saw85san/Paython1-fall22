dishes = {
    "dish1": {
        "Name": "Salmon Sushi", "price": 30, "Origin": "Japan", "exist": False},
    "dish2": {
        "Name": "Pork Dumplings", "price": 25, "Origin": "China", "exist": False},
    "dish3": {
        "Name": "Choziro Tacos", "price": 20, "Origin": "Mexico", "exist": False},
    "dish4": {
        "Name": "Chickpea Curry", "price": 36, "Origin": "India", "exist": True},
    "dish5": {
        "Name": "Apple Pie", "price": 16, "Origin": "USA", "exist": True},
    "dish6": {
        "Name": "Jollof Rice", "price": 18, "Origin": "Nigeria", "exist": False},
    "dish7": {
        "Name": "Dolma", "price": 45, "Origin": "Azerbaijan", "exist": False},
    "dish8": {
        "Name": "Vegetable Pho", "price": 25, "Origin": "Vietnam", "exist": True},
    "dish9": {
        "Name": "Kvass", "price": 12, "Origin": "Russia", "exist": True},
    "dish10": {
        "Name": "Luau", "price": 30, "Origin": "Samoa", "exist": True}

}

for key in dishes.values():
    print(f"{key['Name']}" ,':' , end=" ")
    for value in dishes.values():
        print(f" {value['price']}","$")
        break


######################

dishes = {
    "dish1": {
        "Name": "Salmon Sushi", "price": 30, "Origin": "Japan", "exist": False},
    "dish2": {
        "Name": "Pork Dumplings", "price": 25, "Origin": "China", "exist": False},
    "dish3": {
        "Name": "Choziro Tacos", "price": 20, "Origin": "Mexico", "exist": False},
    "dish4": {
        "Name": "Chickpea Curry", "price": 36, "Origin": "India", "exist": True},
    "dish5": {
        "Name": "Apple Pie", "price": 16, "Origin": "USA", "exist": True},
    "dish6": {
        "Name": "Jollof Rice", "price": 18, "Origin": "Nigeria", "exist": False},
    "dish7": {
        "Name": "Dolma", "price": 45, "Origin": "Azerbaijan", "exist": False},
    "dish8": {
        "Name": "Vegetable Pho", "price": 25, "Origin": "Vietnam", "exist": True},
    "dish9": {
        "Name": "Kvass", "price": 12, "Origin": "Russia", "exist": True},
    "dish10": {
        "Name": "Luau", "price": 30, "Origin": "Samoa", "exist": True}

}

for i in dishes :
  print(dishes[i]['Name'] , " = " , dishes[i]['Origin'] ," = " , dishes[i]['price'])
  
############################

dishes = {
    "dish1": {
        "Name": "Salmon Sushi", "price": 30, "Origin": "Japan", "exist": False},
    "dish2": {
        "Name": "Pork Dumplings", "price": 25, "Origin": "China", "exist": False},
    "dish3": {
        "Name": "Choziro Tacos", "price": 20, "Origin": "Mexico", "exist": False},
    "dish4": {
        "Name": "Chickpea Curry", "price": 36, "Origin": "India", "exist": True},
    "dish5": {
        "Name": "Apple Pie", "price": 16, "Origin": "USA", "exist": True},
    "dish6": {
        "Name": "Jollof Rice", "price": 18, "Origin": "Nigeria", "exist": False},
    "dish7": {
        "Name": "Dolma", "price": 45, "Origin": "Azerbaijan", "exist": False},
    "dish8": {
        "Name": "Vegetable Pho", "price": 25, "Origin": "Vietnam", "exist": True},
    "dish9": {
        "Name": "Kvass", "price": 12, "Origin": "Russia", "exist": True},
    "dish10": {
        "Name": "Luau", "price": 30, "Origin": "Samoa", "exist": True}

}
for i in dishes :
  if dishes[i]['exist']:
    print(dishes[i]['Name'] , " = " , dishes[i]['price'])


#################################
dishes=[
        [1,'Salmon Sushi', 30, 'Japan', False],
        [2,'Pork Dumplings', 25, 'China', False],
        [3,'Choziro Tacos', 20, 'Mexico', False],
        [4, 'Chickpea Curry', 36, 'India', True],
        [5, 'Apple Pie', 16, 'USA', True],
        [6, 'Jollof Rice', 18, 'Nigeria', False],
        [7, 'Dolma', 45, 'Azerbaijan', False],
        [8, 'Vegetable Pho', 25, 'Vietnam', True],
        [9, 'Kvass', 12, 'Russia',  True],
        [10, 'Luau', 30, 'Samoa', True]
        ]


x=input("Enter the name of dish")
y=int(input("Enter the price of dish"))
z=input("Enter the origin of dish")
f=input("Enter the kind of dish")
num=len(dishes[0])
new=(num,x,y,z,f)
dishes.append(new)

print(dishes)
###############################3
dishes=[(1,'Salmon Sushi', 30, 'Japan', False),
        (2,'Pork Dumplings', 25, 'China', False),
        (3,'Choziro Tacos', 20, 'Mexico', False),
        (4, 'Chickpea Curry', 36, 'India', True),
        (5, 'Apple Pie', 16, 'USA', True),
        (6, 'Jollof Rice', 18, 'Nigeria', False),
        (7, 'Dolma', 45, 'Azerbaijan', False),
        (8, 'Vegetable Pho', 25, 'Vietnam', True),
        (9, 'Kvass', 12, 'Russia',  True),
        (10, 'Luau', 30, 'Samoa', True)]

discount = lambda a, b: a*(1-0.2)

def apply_discount(b):
        return 100*(1-0.2)

print("The Price After Discount:", 100*(1-0.2))

############################################


dishes = [(1, 'Salmon Sushi', 30, 'Japan', False),
          (2, 'Pork Dumplings', 25, 'China', False),
          (3, 'Choziro Tacos', 20, 'Mexico', False),
          (4, 'Chickpea Curry', 36, 'India', True),
          (5, 'Apple Pie', 16, 'USA', True),
          (6, 'Jollof Rice', 18, 'Nigeria', False),
          (7, 'Dolma', 45, 'Azerbaijan', False),
          (8, 'Vegetable Pho', 25, 'Vietnam', True),
          (9, 'Kvass', 12, 'Russia', True),
          (10, 'Luau', 30, 'Samoa', True)]


# The menu and main function have been written for you this time. Look over the code and try to understand it.
# You will be writing your own menu and main function soon.

# Main Function: This function calls the functions above. The main function is like the manager of the train station.
# It determines which functions are called, in what order, how many times. It often has additional code as well.
# You may change this code as you please to test your code but the current code will be used to grade your code.

def menu():
    print('Welcome to Python Kitchen. How may I help you? Enter the number of the option you want to do.')
    print('1.See menu')
    print('2.Order')
    print('3.See dishes in order of price')
    print('4.I am the chef, I want to add a dish to the menu.')
    print('5.Exit')
    pass


def main():
    x = 0

    x = int(input("to see the menu click 0: "))
    if x == 0:
        menu()
    while (x != 5):

        x = int(input())

        if x == 1:
            a = input('Are you vegatarian? Enter Y or N.')
            if (a == 'y' or a == 'Y'):
                print(dishes)
            else:
                print_menu()

        if x == 2:
            print('The Orde for dishes')
            print_menu()

        if x == 3:
            print(dishes)
        if x == 4:
            add_dish()
            print('Your new menu is: ')
            print_menu()

    print('Have a good day!')
    pass


main()





