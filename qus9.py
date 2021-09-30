import math



def findRoots(a, b, c):
    disc = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(disc))

    if disc > 0:
        print(" real and different roots ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif disc == 0:
        print(" real and same roots")
        print(-b / (2 * a))


    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)


a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))


if a == 0:
    print("invalid")

else:
    findRoots(a, b, c)