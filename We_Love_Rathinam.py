import turtle
turtle.setup(1366,768)
board = turtle.Turtle()
turtle.bgcolor("black")
 
 
circle_positions = [(0,0,"orange"),(-70,-110,"skyblue"), (70,-110,"lightgreen")]
circle_positions1 = [(0,50,"orange"),(-70,-60,"skyblue"), (70,-60,"lightgreen")]

for pos in circle_positions:
  board.penup()
  board.setpos(pos[0],pos[1])
  board.pencolor(pos[2])
  board.pensize(20)
  board.pendown()
  board.circle(60)

for pos in circle_positions1:
  board.penup()
  board.setpos(pos[0],pos[1])
  board.pencolor(pos[2])
  board.pensize(20)
  board.pendown()
  board.circle(10)
  board.ht()
  board.pu()
  board.goto(1,-250)
  board.write("WE ❤ RATHINAM!",align="center",font=("Arial",60,("bold")))

 
turtle.done()
