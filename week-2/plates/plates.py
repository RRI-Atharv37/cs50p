# CONDITIONS TO BE VALID
# first 2 must be letters
# 2 <= size <= 6
# numbers must be at last place in a row
# 0 cannot be the first number
# no periods, space, punctuation

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if not (2 <= len(plate) <= 6):
        return False
    if not plate[0:2].isalpha():
        return False
    if not plate.isalnum():
        return False
    if not check_num(plate):
        return False

    return True

def check_num(plate):
    num = False
    for number in plate:
        if number.isdigit() and num == False:
            if number == '0':
                return False
            num = True
        if number.isalpha() and num == True:
            num = False
            return False
    return True

main()
