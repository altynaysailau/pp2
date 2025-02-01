class shape:
    def area(self):
        return 0

class square(shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


shape = shape()
square = square(5)

print(f"Shape area: {shape.area()}") 
print(f"Square area: {square.area()}")  