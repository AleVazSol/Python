def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Alejandra", "lastname": "Garcia"}
    

    super_list = [
        {"firstname": "Facundo", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "Rodriguez"},
        {"firstname": "Pablo", "lastname": "Trinidad"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "Fernandez"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 3, 0, 1],
        "floating_nums": [1.1, 4.55, 6.43],
    }

    
    for key,values in super_dict.items():
        print(key," : ", values)
    

    for dict in super_list:
        for key,value in dict.items():
            print(key," : ", value)
        

if __name__ == '__main__':
    run()