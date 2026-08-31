# coke for 50
# accepted: 25, 10, 5
# prompt the user to insert a coin one at a time
# ignore any integer that isnt accepted denomination
# each time inform the amount due
# once the user has inputted atleast 50, inform how much change the user is owed

def main():
    amount_due = 50
    while amount_due > 0:
        print('amount due: ', amount_due)

        coin = int(input("insert coin: "))
        if coin in [5,10,25]:
            amount_due -= coin

    print('change owed: ', abs(amount_due))

main()