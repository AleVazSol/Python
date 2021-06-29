selection = input("pesos to dollar = D, dollar to peso = P ")
if selection=="D":
    pesos=input("Enter how many pesos you have: ")
    pesos=float(pesos)
    dollar=round(pesos/20.1,2)
    print("you have "+str(dollar)+" dollars")
    print("Conversion finished")
elif selection== "P":
    pesos=input("Enter how many Dollars you have: ")
    dollar=float(pesos)
    pesos=round(dollar*20.1,2)
    print("you have "+str(pesos)+" pesos")
    print("Conversion finished")
else:
    print("Option no valid")
    
