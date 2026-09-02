# prompt user to place an order one item per line until control-d
# after each display the total cost of all items inputted so far
# prefix with $ and format to two decimal places
# input case insenitively, ignore any input that isnt an item
# assume every item on menu will be titlecased

TAQUERIA = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_cost = 0

while True:
    try:
        item = input("Item: ").title()
        total_cost+=TAQUERIA[item]
        print(f"${total_cost:.2f}")
    except EOFError:
        print(f"\n${total_cost:.2f}")
        break
    except KeyError:
        pass
