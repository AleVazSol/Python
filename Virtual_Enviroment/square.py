def create_numbers_list(lastNumber):
    numbersList=[]
    for i in range(1,int(lastNumber)+1):
        if i % 3 != 0 :
            numbersList.append(str(i))
    return numbersList



def run():
    naturalNumbers=create_numbers_list(100)
    for item in naturalNumbers:
        squareItem=int(item)**2
        print(item," multiplied by itself is : ",str(squareItem))

    #with list comprehension method    
    listComprehension=[i for i in range(1,10001) if i % 36 ==0]
    print(listComprehension)

if __name__=='__main__':
    run()