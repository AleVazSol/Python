def run():
    my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13]

    #filter high order fuction
    odd= list(filter(lambda x: x%2 !=0, my_list))
    print(odd)

    #map high order function
    square = list(map(lambda x: x**2, my_list))
    print(square)

    #reduce high order function
    from functools import reduce
    all_multiplied = reduce(lambda a,b: a*b, my_list)
    print(all_multiplied)


if __name__ == "__main__":
    run()