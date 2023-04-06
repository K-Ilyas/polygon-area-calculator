class Rectangle:
    def __init__(self,width=0,height=0) :
        self.width = width
        self.height = height
    def set_width(self,width) :
        self.width =width
    def set_height(self,height):
        self.height = height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self) :
        return (self.width*2) + (self.height*2)
    def get_diagonal(self):
        return  ((self.width ** 2 + self.height ** 2) ** .5)    
    def get_picture(self) :
        if self.width > 50 or self.height > 50 :
          return "Too big for picture."
        
        picture = ''

        for i in range(self.height) :
            for j in range(self.width) :
                picture = picture +"*"
            picture = picture + "\n"

        return picture
              
    def get_amount_inside(slef,shape):
        return int(slef.get_area() / shape.get_area())
    
    def __str__(self) :
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"


class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
        self.side = side
    def set_side(self,side):
        self.side = side
        self.set_width(side)
        self.set_height(side)

    def __str__(self):
        return "Square(side="+str(self.width)+")"




