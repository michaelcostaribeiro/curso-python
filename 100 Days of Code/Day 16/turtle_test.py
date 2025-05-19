from turtle_test import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color('orange')
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)

jenny = Turtle()
print(jenny)
jenny.color('pink')
jenny.shape('turtle')
jenny.backward(100)
jenny.right(120)
jenny.backward(100)
jenny.right(120)
jenny.backward(100)

kevin = Turtle()
print(kevin)
kevin.color('red')
kevin.shape('turtle')
kevin.right(120)
kevin.backward(100)
kevin.left(120)
kevin.backward(100)

my_screen = Screen()
print(my_screen.canvwidth)
print(my_screen.canvheight)
my_screen.exitonclick()


