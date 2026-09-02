GROCERY = {}

while True:
    try:
        item = input("Item: ").lower()
        if item in GROCERY:
            GROCERY[item] += 1
        else:
            GROCERY[item] = 1
    except EOFError:
        for sort in sorted(GROCERY):
            print(GROCERY[sort], sort.upper())
        break
    except KeyError:
        pass
