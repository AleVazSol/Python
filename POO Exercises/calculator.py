
#high class
class Calculator:


    def __init__(self,numA,numB):
        self._numa=int(numA)
        self._numb=int(numB)

    #This define the property Num A for the getter and setter
    @property
    def numa(self):
        return self._numa
         
    @numa.setter
    def setNumA(self,value):
        if (int(value)>=0):
            self._numa=value
            print(f"NumA value was setted to: {value}")
        else:
            print("use only positive numbers")
    
    #This define the property Num B for the getter and setter
    @property
    def numb(self):
        return self._numb
         
    @numb.setter
    def setNumB(self,value):
        if (int(value)>=0):
            self._numb=value
            print(f"NumB value was setted to: {value}")
        else:
            print("use only positive numbers")

    #generic methods
    def sum(self):
        return self._numa + self._numb

    def sub(self):
        return self._numa - self._numb

    def mult(self):
        return self._numa * self._numb

    def div(self):
        return self._numa / self._numb


#subclass

class Cientific_calculator(Calculator):
    def __init__(self, numA, numB):
        super().__init__(numA, numB)

    #adding method pow
    def pow(self):
        result=super().numa
        for i in range (super().numb-1):
            result= result*super().numa
        return result



if __name__=="__main__":

    Calculator2=Cientific_calculator(numA=0,numB=0)
    number1=input("Enter number A ")
    Calculator2.setNumA=int(number1)
    number2=input("Enter number B ")
    Calculator2.setNumB=int(number2)
    print(f"the multiplication of both numbers have the following result:  {Calculator2.mult()}")

    #using the subclass method
    print(f"{number1} raised to {number2} have the following result:  {Calculator2.pow()}")

    
