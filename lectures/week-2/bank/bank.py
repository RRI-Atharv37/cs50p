# hello = 0
# hxxxxx = 20
# anything else = 100
# ignore leading whitespaces, case insensitive
# cases like hello xxxxx or hxxxx yyyyy also follow the above

greeting = input("greeting: ").lstrip().lower()

if(greeting.startswith('hello')):
    print("$0")
elif(greeting.startswith('h')):
    print("$20")
else:
    print("$100")
    