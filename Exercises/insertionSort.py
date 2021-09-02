import random

def insertion_sort(list):
    for index in range(1,len(list)):
        current_position=index
        number=list[index]
        while(current_position>0 and list[current_position-1]>number):
            list[current_position]=list[current_position-1]
            current_position=current_position-1
        list[current_position]=number




    return list



if __name__ == '__main__':
    list_size = int(input('how big is the list '))
    list = [random.randint(0, 100) for i in range(list_size)]
    print(list)
    result = insertion_sort(list)
    print(list)
    