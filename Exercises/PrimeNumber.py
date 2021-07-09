def isPrime(number):
    prime= True
    for j in range(2,number):
        if number%j ==0:
            prime=False
            break
    return prime

def run():
    PRESENTATION="""
    This program displays the prime numbers
    from 0 to n
    please enter the n number:
    """
    lastNumber=int(input(PRESENTATION))
    for i in range(lastNumber+1):
        if isPrime(i)==False:
            continue
        print(str(i)+ " is prime")


if __name__ == '__main__':
    run()