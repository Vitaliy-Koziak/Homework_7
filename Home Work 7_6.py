#Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000, і повертає True, якщо воно просте, і False - в іншому випадку.

def is_prime(number):
        temp_number = 2
        while number % temp_number != 0 :
            temp_number += 1
        if temp_number == number : return  True
        else:
            return False

def main():
    number = int(input("Введіть число від 0 до 1000: "))
    while number < 0 or number > 1000:
        print("Ваше число не задовільняє межі, введіть інше: ")
        number = int(input())
    print(is_prime(number))

if __name__ == "__main__":
    main()