#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()

drawer = trtl.Turtle()


#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def drop_apple():
  apple.hideturtle()
  a_fall = apple.clone()
  a_fall.showturtle()
  a_fall.penup()
  a_fall.setposition(a_fall.xcor(), (a_fall.ycor()-200))
  wn.update()
  a_fall.hideturtle()
  apple.showturtle()


  



#-----function calls-----
draw_apple(apple)

drawer.hideturtle()
drawer.color("white")
drawer.write("A", font=("Arial", 74, "bold")) 

wn.onkeypress(drop_apple, "a")
wn.listen()


wn.mainloop()