#Написати функцію square, яка приймає 1 аргумент - сторону квадрата, і повертає 3 значення (за допомогою кортежу): периметр квадрата, площу
#квадрата і діагональ квадрата.
from math import sqrt
def square(side):
    perim = side * 4
    square = side ** 2
    diagonal = side * sqrt(2)
    a = (perim,square,diagonal)
    return (a)
def main():
    side = float(input("Enter side of square: "))
    print(square(side))

if __name__ == "__main__":
    main()
