# camelCase to snake_case

camelCase = input("camelCase: ")
for c in camelCase:
    if c.isupper():
        c = '_' + c.lower()
    print(c, end="")
    