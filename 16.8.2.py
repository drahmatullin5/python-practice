class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2


class Circle:
    def __init__(self, r):
        self.r = r

    def get_circle_area(self):
        return self.r ** 2 * 3.14
      
      #Далее импорт
      
      from rectangle import Rectangle, Square, Circle

if __name__ == '__main__':

    rect_1 = Rectangle(3, 4)
    rect_2 = Rectangle(12, 5)

    print(rect_1.get_area())
    print(rect_2.get_area())

    square_1 = Square(5)
    square_2 = Square(10)
    
    print(square_1.get_area_square(), 
          square_2.get_area_square())

    circle_1 = Circle(20)
    circle_2 = Circle(4)
    
    print(circle_1.get_circle_area(),
          circle_2.get_circle_area())

 
    figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

    for figure in figures:
        if isinstance(figure, Square):
            print(figure.get_area_square())

        elif isinstance(figure, Circle):
            print(figure.get_circle_area())

        else:
            print(figure.get_area())
       
