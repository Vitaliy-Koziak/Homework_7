#Написати функцію arithmetic, яка приймає 3 аргументи: перші 2 - числа, третій - операцію, яка повинна бути здійснена над ними. Якщо третій
#аргумент +, додати їх; якщо -, то відняти; * - помножити; / - розділити (перше на друге). В інших випадках повернути рядок "Невідома операція".
def arithmetic(first_number,second_number,sign):
    if sign == "+" : return first_number + second_number
    elif sign == "-" : return first_number - second_number
    elif sign == "*" : return first_number * second_number
    elif sign == "/" :
            while second_number == 0:
                print("На нуль ділити не можна! ")
                second_number = float(input("Введіть друге число: "))
            return first_number / second_number
    else:
        print("Невідома операція! ")
def main():
    first_number = float(input("Введіть перше число: "))
    second_number = float(input("Введіть друге число: "))
    sign = input("Введіть знак: ")

    print("Результат: ", arithmetic(first_number,second_number,sign) )
if __name__ == "__main__":
    main()