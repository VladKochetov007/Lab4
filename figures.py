from turtle import *
from random import randint
from typing import Tuple

class Figure:
    """Base class for geometric figures"""
    
    def __init__(self, x: float, y: float, color: str):
        self._x = x
        self._y = y
        self._visible = False
        self._color = color

    def _draw(self, color: str) -> None:
        """Virtual method for drawing figure with given color"""
        pass

    def show(self) -> None:
        """Show figure on screen"""
        if not self._visible:
            self._visible = True
            self._draw(self._color)

    def hide(self) -> None:
        """Hide figure from screen"""
        if self._visible:
            self._visible = False
            self._draw(bgcolor())

    def move(self, dx: float, dy: float) -> None:
        """Move figure by dx, dy pixels"""
        is_visible = self._visible
        if is_visible:
            self.hide()
        self._x += dx
        self._y += dy
        if is_visible:
            self.show()

class Circle(Figure):
    """Circle class"""
    
    def __init__(self, x: float, y: float, radius: float, color: str):
        super().__init__(x, y, color)
        self._radius = radius

    def _draw(self, color: str) -> None:
        pencolor(color)
        up()
        setpos(self._x, self._y - self._radius)
        down()
        circle(self._radius)
        up()

class Rectangle(Figure):
    """Rectangle class"""
    
    def __init__(self, x: float, y: float, width: float, height: float, color: str):
        super().__init__(x, y, color)
        self._width = width
        self._height = height

    def _draw(self, color: str) -> None:
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        for _ in range(2):
            forward(self._width)
            left(90)
            forward(self._height)
            left(90)
        up()

class Square(Rectangle):
    """Square class - inherits from Rectangle"""
    
    def __init__(self, x: float, y: float, size: float, color: str):
        super().__init__(x, y, size, size, color)

class Triangle(Figure):
    """Equilateral triangle class"""
    
    def __init__(self, x: float, y: float, side: float, color: str):
        super().__init__(x, y, color)
        self._side = side

    def _draw(self, color: str) -> None:
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        for _ in range(3):
            forward(self._side)
            left(120)
        up()

class Trapezoid(Figure):
    """Isosceles trapezoid class"""
    
    def __init__(self, x: float, y: float, base1: float, base2: float, height: float, color: str):
        super().__init__(x, y, color)
        self._base1 = base1
        self._base2 = base2
        self._height = height

    def _draw(self, color: str) -> None:
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        
        # Calculate side length using Pythagorean theorem
        side = ((self._base2 - self._base1) / 2) ** 2 + self._height ** 2
        side = side ** 0.5
        
        # Draw trapezoid
        forward(self._base1)
        left(90)
        forward(self._height)
        left(90)
        forward(self._base2)
        left(90)
        forward(self._height)
        left(90)
        up()

class Car:
    """Car class composed of figures"""
    
    def __init__(self, x: float, y: float):
        # Body (rectangle)
        self._body = Rectangle(x, y, 200, 60, "blue")
        # Wheels (circles)
        self._wheel1 = Circle(x + 40, y - 30, 20, "black")
        self._wheel2 = Circle(x + 160, y - 30, 20, "black")
        # Windows (rectangles)
        self._window1 = Rectangle(x + 120, y + 20, 40, 30, "lightblue")
        self._window2 = Rectangle(x + 40, y + 20, 40, 30, "lightblue")
        # Headlights (circles)
        self._headlight1 = Circle(x + 180, y + 30, 10, "yellow")
        self._headlight2 = Circle(x + 20, y + 30, 10, "yellow")

    def show(self) -> None:
        """Show all car parts"""
        self._body.show()
        self._wheel1.show()
        self._wheel2.show()
        self._window1.show()
        self._window2.show()
        self._headlight1.show()
        self._headlight2.show()

    def hide(self) -> None:
        """Hide all car parts"""
        self._body.hide()
        self._wheel1.hide()
        self._wheel2.hide()
        self._window1.hide()
        self._window2.hide()
        self._headlight1.hide()
        self._headlight2.hide()

    def move(self, dx: float, dy: float) -> None:
        """Move car by dx, dy pixels"""
        self._body.move(dx, dy)
        self._wheel1.move(dx, dy)
        self._wheel2.move(dx, dy)
        self._window1.move(dx, dy)
        self._window2.move(dx, dy)
        self._headlight1.move(dx, dy)
        self._headlight2.move(dx, dy)

def draw_random_figures(count: int = 100) -> None:
    """Draw random figures on screen"""
    colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "brown"]
    figures = []
    
    for _ in range(count):
        x = randint(-300, 300)
        y = randint(-300, 300)
        color = colors[randint(0, len(colors) - 1)]
        
        # Randomly choose figure type
        figure_type = randint(1, 5)
        
        if figure_type == 1:
            radius = randint(10, 50)
            figures.append(Circle(x, y, radius, color))
        elif figure_type == 2:
            side = randint(20, 100)
            figures.append(Square(x, y, side, color))
        elif figure_type == 3:
            side = randint(20, 100)
            figures.append(Triangle(x, y, side, color))
        elif figure_type == 4:
            base1 = randint(30, 100)
            base2 = randint(30, 100)
            height = randint(20, 80)
            figures.append(Trapezoid(x, y, base1, base2, height, color))
        else:
            width = randint(30, 100)
            height = randint(20, 80)
            figures.append(Rectangle(x, y, width, height, color))
    
    # Show all figures
    for figure in figures:
        figure.show()

def main() -> None:
    # Initialize turtle
    home()
    delay(30)
    
    # Test individual figures
    c = Circle(120, 120, 50, "blue")
    c.show()
    c.move(-30, -140)
    c.hide()
    
    q = Square(0, 0, 150, "red")
    q.show()
    q.move(0, 140)
    q.hide()
    
    t = Triangle(120, 120, 50, "blue")
    t.show()
    t.move(-30, -140)
    t.hide()
    
    tr = Trapezoid(120, 120, 50, 30, 40, "red")
    tr.show()
    tr.move(-30, -140)
    tr.hide()
    
    r = Rectangle(120, 120, 50, 30, "red")
    r.show()
    r.move(-30, -140)
    r.hide()
    
    # Test car
    car = Car(0, 0)
    car.show()
    car.move(100, 100)
    
    # Draw random figures
    draw_random_figures()
    
    mainloop()

if __name__ == "__main__":
    main() 