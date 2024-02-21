class Rectangle:
    
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** (1/2)

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        
        picture = ''
        for i in range(0, self.height):
            picture += "*" * self.width
            picture += "\n"
        
        return picture

    def get_amount_inside(self, shape):
        height_times = int (self.height / shape.height)
        width_times = int(self.width / shape.width)
        return width_times * height_times

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    
    def __init__(self, lenght):
        self.width = lenght
        self. height = lenght

    def set_side(self, lenght):
        self.width = lenght
        self. height = lenght

    def __str__(self) -> str:
        return f"Square(side={self.height})"