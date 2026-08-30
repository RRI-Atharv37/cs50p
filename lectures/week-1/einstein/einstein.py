# calc energy (j) from input mass (kg)

def main():
    mass = int(input("enter mass: "))
    print(calc(mass))

def calc(mass):
    C_SQAURED = 300000000 ** 2
    return mass * C_SQAURED

main()