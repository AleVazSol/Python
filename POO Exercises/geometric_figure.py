from abc import *

class Geometricfigure:
    def __init__(self,height,width):
        self._height=height
        self._width=width
    def __str__(self):
        return f"Geometric figure height:{self._height} width: {self._width}"
    
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value
    
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value

    @abstractclassmethod
    def area(self):
        pass

class color:
    def __init__(self,color):
        self._color:color

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,value):
        self._color=value
    

#subclases
class square(Geometricfigure,color):
    def __init__(self, side, color):
        Geometricfigure.__init__(self,side,side)
        color.__init__(self,color)
    def __str__(self):
        return super().__str__()+"  SQUARE"
    def area(self):
        return self._height*self._width
    

class rectangle(Geometricfigure,color):
    def __init__(self, height, width, color):
        Geometricfigure.__init__(self,height,width)
        color.__init__(self,color)
    def __str__(self):
        return super().__str__()+"  RECTANGLE"
    def area(self):
        return self._height*self._width
    



if __name__=="__main__":

    square=square(5,"Green")
    print(square)
    print(square.area())
    rectangle=rectangle(5,8,"Red")
    print(rectangle)
    print(rectangle.area())


    

    
