#Написати функцію date, яка приймає 3 аргументи - день, місяць і рік. Повернути True, якщо така дата є в нашому календарі, і False - в іншому
#випадку.
def date(day,month,year):
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year % 4 == 0:
        days_in_month[1]+=1
    if month < 1 or month > 12:
        result = False
    else:
        if day <= days_in_month[month-1]:
            result =  True
        else:
            result = False
    return result
def main():
    day = int(input("Введіть день: "))
    month = int(input("Введіть місяць: " ))
    year= int(input("Введіть рік: " ))
    print(date(day,month,year))

if __name__ == "__main__":
    main()




