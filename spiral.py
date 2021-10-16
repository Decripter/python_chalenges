import turtle

turtle.title("confession artifact")
turtle.bgcolor('black')
colors=['red','orange','yellow','green']
turtle.hideturtle()


text=['Te','Amo','Minha','Bufinha']

turtle.speed(0)

for i in range(70):

    turtle.pencolor(colors[i%4])


    turtle.penup() 

    turtle.forward(i*6)

    turtle.pendown()

    turtle.write(text[i%4],font=("Microsoft Yahei",int(i/4+4)))

    turtle.left(92)

    

input()