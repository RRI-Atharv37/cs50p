# input as X/Y
# <= 1% = E
# >= 99% = F
# X -> non negative integer
# Y -> positive integer
# ValueError, ZeroDivisionError
while True:
    try:
        x,y = input("Fraction: ").split('/')
        x = int(x)
        y = int(y)
        if x <= 0 or y <= 0:
            raise ValueError
        percentage = round(x/y*100)
        if percentage <= 1: print('E')
        elif percentage >= 99: print('F')
        else: print(f"{percentage}%")
        break
    except ValueError:
        print("cannot divide non negative integers")
    except ZeroDivisionError:
        print("cannot divide by zero")
    # else:
    #     if percentage <= 1: print('E')
    #     elif percentage >= 99: print('F')
    #     else: print(f"{percentage}%")
