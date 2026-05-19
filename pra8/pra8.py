class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Area:", 3.14 * self.r * self.r)

    def circum(self):
        print("Circumference:", 2 * 3.14 * self.r)

c1 = Circle(2)
c1.area()
c1.circum()