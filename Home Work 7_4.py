#Написати функцію season, яка приймає 1 аргумент - номер місяця (від 1 до 12), і повертає пору року, якій цей місяць належить (зима, весна, літо або
#осінь).
def season(month_number):
    if month_number == 12 or (month_number>=1 and month_number<=2) : print("Зима")
    elif month_number >=3 and month_number <=5 : print("Весна")
    elif month_number >=6 and month_number <=8 : print("Літо")
    else:
        print("Осінь")

def main():
    month_number = int(input("Введіть номер місяця : "))
    while month_number < 1 or month_number > 12:
        print("Ви ввели неправильний номер місяця, введіть ще раз: ")
        month_number = int(input())
    season(month_number)

if __name__ == "__main__":
    main()