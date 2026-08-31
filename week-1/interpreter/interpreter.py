# x y z
# y -> +, -, *, /
# x,z are int

x,y,z = input("expression: ").split(" ")
# int(x),y,int(z) = input("expression: ").split(" ")
x = int(x)
z = int(z)

match y:
    case "+":
        print(float(x + z))
    case "-":
        print(float(x - z))
    case "*":
        print(float(x * z))
    case "/":
        print(float(x / z))