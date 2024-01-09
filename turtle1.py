import turtle

turtle.speed(20)
for i in range(10):
    if i%5==0:
        turtle.color("yellow")
    else:
        turtle.color("black")
    for x in range(6):
        turtle.forward(40)
        turtle.right(60)
    turtle.right(80)    
