def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)


def run():
    n=int(input("Pick a number: "))
    print(factorial(n))


if __name__ == "__main__":
    run()
