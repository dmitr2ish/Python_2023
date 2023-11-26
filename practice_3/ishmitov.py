from figures import Shape, Rectangle, Square, Triangle

shape1 = Shape([1,2,3,4])
shape2 = Rectangle([3,4])
shape3 = Square(5)
shape4 = Triangle([3,4,5])

print(shape1, shape1.area())
print(shape2, shape2.area())
print(shape3, shape3.area())
print(shape4, shape4.area())