#-*- coding: utf-8 -*-

num1 = raw_input("Vnesite celo število med 1 in 100: ")

def zanka():
    for x in range(1, num1 + 1):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("fizz")
        elif x % 5 == 0:
            print("buzz")
        else:
            print(x)

try:
    num1 = int(num1)
    if num1 > 100:
        print("Izbrali ste število večje od 100! Izbrano število je spremenjeno v 100.")
        num1 = 100
        zanka()
    else:
        zanka()

except ValueError:
    print("Vnesite celo število!")
