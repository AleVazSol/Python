def run():
    dictionary={}
    for i in range(1,101):
        dictionary[i]=i**3
    print(dictionary)

    dictionary2={key:value for (key,value) in dictionary.items() if key % 3 != 0}
    print(dictionary2)

    my_dict = {i : round(i**0.5,2) for i in  range(1,1001)}
    print(my_dict)


if __name__=="__main__":
    run()
