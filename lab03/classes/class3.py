class shape:
    def area(self):
        pass
    def __init__(self):
        pass
class rectangle(shape):
    def __init__(self, length, width):
        super().__init__()
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
a = rectangle(20,40)
print("Area is ", a.area())

