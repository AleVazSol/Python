import random

def buble_sort(list):
    lenght=len(list)
    
    for n in range(lenght):
        for i in range (0,lenght-1-n):
            if list[i]>list[i+1]:

                list[i],list[i+1]=list[i+1],list[i]
    
    return list



if __name__ == '__main__':
    list_size = int(input('how big is the list '))
    list = [random.randint(0, 100) for i in range(list_size)]
    print(list)
    result = buble_sort(list)
    print(list)
    