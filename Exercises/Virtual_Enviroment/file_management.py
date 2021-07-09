from os import read


def Read():
    numbers = []
    with open("./file.txt","r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def Write():
    names=["Ale","Ivan","Clau"]
    with open("./file.txt","a", encoding="utf-8") as f :
        for name in names:
            f.write(name+"\n")


def run():
    Write()


if __name__ == "__main__":
    run()