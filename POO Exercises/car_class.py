
class Automovil:
    
    def __init__(self, model, color, brand):
        self.model = model
        self.color = color
        self.brand = brand
        self._state = "idle"
        self._motor = Motor(cylinders=4)

    #methods
    def accelerate(self, type = "slow"):
        if type == "fast":
            self._motor.inject_fuel(5)
        else:
            self._motor.inject_fuel(2)

        self._state = "moving"


class Motor:

    def __init__(self, cylinders, type="fuel"):
        self.cylinders = cylinders
        self.type = type
        self._temperature = 0


    #methods
    def inject_fuel(self, ammount):
        """ Method to inject fuel to the motor 
        """
        pass
