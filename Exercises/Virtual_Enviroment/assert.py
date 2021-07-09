def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input('enter number: ')
    assert num.isnumeric(), "You Should enter a NUMBER"
    assert int(num)>=0, "You Should enter a Positive Number"
    print(divisors(int(num)))
    print("End of the program")
    


if __name__ == '__main__':
    run()