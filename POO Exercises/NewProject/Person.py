class Person:

    quantity=0
    
    @classmethod
    def addPerson(cls):
        cls.quantity +=1
        

    def __init__(self,name,lastName,age):
        self._name = name
        self._lastName = lastName
        self._age = age
        Person.addPerson()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age




