def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    Doneflag = False
    while Doneflag == False :
        try:
            num = int(input('Enter Number: '))
            if num<0:
                raise ValueError ("the number is negative")
            Doneflag = True
        except ValueError as ve:
            print(ve, "---> Try again with a POSITIVE NUMBER")   
    print(divisors(num))
    print("End of the program")


if __name__ == '__main__':
    run()