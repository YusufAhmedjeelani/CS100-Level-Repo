# Yusuf Ahmedjeelani
# Final Project
# CS 111, Reckinger
# Draws a turtle animation slideshow of NBA teams with team logos and city skylines with matching team colors
#Re Add Images back into program filetree
import turtle
import random
import image
import math
import time
 
## Write your code here.  
s = turtle.getscreen()
t = turtle.Turtle()
s.colormode(255) #Changes color select options
def main_menu(): #Creates the main menu animation
  t.hideturtle()
  s.bgcolor("cyan")
  t.penup()
  t.goto(-200,600)
  t.write("Welcome to the NBA experience!",False, align = "center", font=("Arial", 50, "normal"))
  t.penup()
  t.goto(0,-300)
  t.fillcolor("darkorange")
  t.pencolor("black")
  t.begin_fill()
  t.circle(400)
  t.end_fill()
  t.goto(-275,-180) 
  t.pendown()
  t.width(4)
  t.circle(380, 140) #Creates circle for the basketball
  t.penup()
  t.goto(-360, -50)
  t.pendown()
  t.circle(-460,-110) #Creates semi-circle arcs for the lines on the ball
  t.penup()
  t.goto(-370, 20)
  t.pendown()
  t.circle(500, -100) #Creates semi-circle arcs for the lines on the ball
  t.penup()
  t.goto(-680,50)
  t.write("Western Conference",False, align = "left", font=("Arial", 20, "bold"))
  t.penup()
  t.goto(480,50)
  t.write("Eastern Conference",False, align = "left", font=("Arial", 20, "bold"))
  t.penup()
  t.goto(-100, -400)
  t.write("Created by Yusuf Ahmedjeelani and Safwan Asghar",False, align = "center", font=("Arial", 18, "italic"))
  time.sleep(1) #Stops code for a second so viewer can see image
 
 
def western(): #Creates western conference menu
  s.colormode(255)
  t.hideturtle()
  s.bgcolor("goldenrod")
  t.penup()
  t.goto(0,600)
  t.write("Welcome to the Western Conference",False, align = "center", font=("Arial", 25, "normal"))
  img = image.FileImage("wcon.gif") #Captures picture from file tree
  width = img.get_width() #Captures image width
  height = img.get_height() #Captures image height
  for row in range(0, height, 8): #Loops through pixels in picture by using a nested loop
    for col in range(0, width, 5):
      p = img.get_pixel(col, row) #Grabs pixel color information
      r = p.red
      g = p.green
      b = p.blue
      t.pencolor(r, g, b) 
      t.fillcolor(r, g, b)
      x = col + 30 #Adjusts X value
      y = (row * -1) + (height/2) #Flips and adjusts Y value to be recognizable 
      t.goto(x,y) 
      t.stamp()
  t.penup()
  t.goto(-700, 500)
  t.write("Los Angeles Lakers",False, align = "left", font=("Arial", 18, "bold"))
  t.penup()
  t.goto(-700, 100)
  t.write("San Antonio Spurs",False, align = "left", font=("Arial", 18, "bold"))
  t.penup()
  t.goto(-700, -300)
  t.write("Golden State Warriors",False, align = "left", font=("Arial", 18, "bold"))
  t.penup()

def eastern():#Creates eastern conference menu
  s.colormode(255)
  t.hideturtle()
  s.bgcolor("darkgreen")
  t.penup()
  t.goto(0,600)
  t.write("Welcome to the Eastern Conference",False, align = "center", font=("Arial", 25, "normal"))
  img = image.FileImage("econ.gif") #Captures picture from file tree
  width = img.get_width()#Captures image width
  height = img.get_height() #Captures image height
  for row in range(0, height, 8): #Loops through pixels in picture by using a nested loop
    for col in range(0, width, 5):
      p = img.get_pixel(col, row)  #Grabs pixel color information
      r = p.red
      g = p.green
      b = p.blue
      t.pencolor(r, g, b)
      t.fillcolor(r, g, b)
      x = col + (width/2) #Adjusts X value
      y = (row * -1) + (height/2) #Flips and adjusts Y value to be recognizable 
      t.goto(x,y)
      t.stamp()
  t.penup()
  t.goto(-700, 500)
  t.write("Philadelphia 76ers",False, align = "left", font=("Arial", 18, "bold"))
  t.penup()
  t.goto(-700, 100)
  t.write("Chicago Bulls",False, align = "left", font=("Arial", 18, "bold"))
  t.penup()
  t.goto(-700, -300)
  t.write("Boston Celtics",False, align = "left", font=("Arial", 18, "bold"))
  t.penup()
  time.sleep(5)
 
def build1(team): #Creates buildings for skyline passes team name for parameter
  if team == "Philadelphia": #Branch for city specific colors
    t.fillcolor("red")
    t.pencolor("white")
  if team == "Chicago": #Changes colors for different cities
    t.fillcolor("grey")
    t.pencolor("black")
  if team == "Boston":
    t.fillcolor("saddle brown")
    t.pencolor("white")
  if team == "Los_Angeles":
    t.fillcolor("black")
    t.pencolor("purple")
  if team == "San_Antonio":
    t.fillcolor("snow3")
    t.pencolor("powder blue")
  if team == "San_Francisco":
    t.fillcolor("gold")
    t.pencolor("white")
  height = 500
  width = 300
  t.setheading(90) #Positions turtle to face North
  t.width(2)
  t.pendown()
  t.begin_fill()
  t.forward(height)
  t.setheading(45) #Positions turtle to face Northeast
  t.forward(width/2)
  t.setheading(315) #Positions turtle to face Southeast
  t.forward(width/2)
  t.setheading(270) #Positions turtle to face South
  t.forward(height)
  t.setheading(180) #Positions turtle to face West
  t.forward(width)
  t.end_fill()
  t.setheading(0) #Positions turtle to face East
  t.forward(width) #Returns back to position to draw new building

def build2(team):#Creates buildings for skyline passes team name for parameter
  if team == "Philadelphia":
    t.fillcolor("black")
    t.pencolor("red")
  if team == "Chicago":#Changes colors for different cities
    t.fillcolor("black")
    t.pencolor("white")
  if team == "Boston":
    height = 250
    t.fillcolor("black")
    t.pencolor("white")
  if team == "Los_Angeles":
    t.fillcolor("purple3")
    t.pencolor("white")
  if team == "San_Antonio":
    t.fillcolor("azure4")
    t.pencolor("white")
  if team == "San_Francisco":
    t.fillcolor("deep sky blue")
    t.pencolor("yellow")
  height = 250
  t.setheading(90) #Positions turtle to face North
  t.width(2)
  t.pendown()
  t.begin_fill()
  t.forward(height)
  t.setheading(0) #Positions turtle to face East
  t.forward(height)
  t.setheading(270) #Positions turtle to face South
  t.forward(height)
  t.setheading(180) #Positions turtle to face West
  t.forward(height)
  t.end_fill()
  t.setheading(0) #Positions turtle to face East
  t.forward(height) #Returns back to position to draw new building

def build3(team):#Creates buildings for skyline passes team name for parameter
  if team == "Philadelphia":
    t.fillcolor("red")
    t.pencolor("white")
  if team == "Chicago":
    t.fillcolor("red")
    t.pencolor("white")
  if team == "Boston":
    height = 250
    t.fillcolor("lime")
    t.pencolor("black")
  if team == "Los_Angeles": #Changes colors for different cities
    t.fillcolor("yellow")
    t.pencolor("indigo")
  if team == "San_Antonio":
    t.fillcolor("black")
    t.pencolor("white")
  if team == "San_Francisco":
    t.fillcolor("white")
    t.pencolor("aqua")
  height = 450
  width = 200
  t.setheading(90) #Positions turtle to face North
  t.width(2)
  t.pendown()
  t.begin_fill()
  t.forward(height)
  t.setheading(0) #Positions turtle to face East
  t.forward(width)
  t.setheading(270)  #Positions turtle to face South
  t.forward(height)
  t.setheading(180) #Positions turtle to face West
  t.forward(width)
  t.end_fill()
  t.setheading(0) #Positions turtle to face East
  t.forward(width) #Returns back to position to draw new building

def build4(team):#Creates buildings for skyline passes team name for parameter
  if team == "Philadelphia": #Changes colors for different cities
    t.fillcolor("white")
    t.pencolor("white")
  if team == "Chicago":
    t.fillcolor("white")
    t.pencolor("black")
  if team == "Boston":
    height = 250
    t.fillcolor("white")
    t.pencolor("gold")
  if team == "Los_Angeles":
    t.fillcolor("white")
    t.pencolor("black")
  if team == "San_Antonio":
    t.fillcolor("white")
    t.pencolor("cyan")
  if team == "San_Francisco":
    t.fillcolor("blue")
    t.pencolor("white")
  height = 580
  angle = 315
  t.setheading(90) #Positions turtle to face North
  t.width(2)
  t.width(2)
  t.pendown()
  t.begin_fill()
  t.forward(height)
  t.setheading(315) #Positions turtle to face Southeast
  t.forward(262.488) #Moves forward to make a slant shaped roof
  t.setheading(270) #Positions turtle to face South
  t.forward(400) 
  t.setheading(180)  #Positions turtle to face West
  t.forward(height/2)
  t.end_fill()
  t.setheading(0) #Positions turtle to face East
  t.forward(height/2)


def Philadelphia(): #Creates screen for team
  s.colormode(255)
  t.hideturtle()
  s.bgcolor("darkblue")
  t.penup()
  t.goto(0,600)
  t.pencolor("white")
  t.write("The Philadelphia 76ers",False, align = "center", font=("Arial", 25, "normal"))
  t.penup()
  t.goto(-880,500)
  t.write("Championship years:",False, align = "left", font=("Arial", 25, "bold"))
  t.penup()
  t.goto(-300,500)
  rings = load_rings() #Calls function to get data and stores dictionary in varaible "rings"
  t.write(rings['76ers'],False, align = "left", font=("Arial", 16, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(-880, 300)
  t.write("Conference title years:",False, align = "left", font=("Arial", 25, "bold"))
  t.penup()
  t.goto(-300,300)
  conference = load_conference() #Calls function to get data and stores dictionary in varaible "conference"
  t.write(conference['76ers'],False, align = "left", font=("Arial", 16, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(-880, 100)
  t.write("Most popular player:",False, align = "left", font=("Arial", 25, "bold"))
  t.penup()
  t.goto(-300,100)
  pop_player = load_player() #Calls function to get data and stores dictionary in varaible "pop_player"
  t.write(pop_player['76ers'],False, align = "left", font=("Arial", 20, "bold"))#Calls dictionary to find key
  t.penup
  t.goto(-880, -100)
  t.write("Year founded:",False, align = "left", font=("Arial", 25, "bold"))
  t.goto(-300,-100)
  founded = load_year_founded()  #Calls function to get data and stores dictionary in varaible "pop_player"
  t.write(founded['76ers'],False, align = "left", font=("Arial", 20, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(0,600)
  img = image.FileImage("76ers_logo.gif") #Opens team logo picture
  width = img.get_width() #Grabs picture width
  height = img.get_height() #Grabs picture height
  for row in range(0, height, 10): #Uses nested loop to iterate through each pixel
    for col in range(0, width, 10):
      p = img.get_pixel(col, row) #Gets pixel information
      r = p.red
      g = p.green
      b = p.blue
      t.pencolor(r, g, b)
      t.fillcolor(r, g, b)
      x = col + (width/4) #Adjusts X values
      y = (row * -1) + (height/1.5) #Flips and adjusts Y values
      t.goto(x,y)
      t.stamp()
  t.penup()
  t.goto(-1600,-800)
  for i in range(8): #Loop is used to build repeating skyline
    build1('Philadelphia')#Call various buildings using team arguement
    build4('Philadelphia')
    build3('Philadelphia')
    build2('Philadelphia')
  

  
 
def Chicago(): #Creates screen for team
  s.colormode(255)
  t.hideturtle()
  s.bgcolor("darkred")
  t.penup()
  t.goto(0,600)
  t.pencolor("white")
  t.write("The Chicago Bulls",False, align = "center", font=("Arial", 25, "normal"))
  t.penup()
  t.goto(-880,500)
  t.write("Championship years:",False, align = "left", font=("Arial", 25, "bold"))
  t.penup()
  t.goto(-300,500)
  rings = load_rings() #Calls function to get data and stores dictionary in varaible "rings"
  t.write(rings['Bulls'],False, align = "left", font=("Arial", 16, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(-880, 300)
  t.write("Conference title years:",False, align = "left", font=("Arial", 25, "bold"))
  t.penup()
  t.goto(-300,300)
  conference = load_conference() #Calls function to get data and stores dictionary in varaible "conference"
  t.write(conference['Bulls'],False, align = "left", font=("Arial", 16, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(-880, 100)
  t.write("Most popular player:",False, align = "left", font=("Arial", 25, "bold"))
  t.penup()
  t.goto(-300,100)
  pop_player = load_player() #Calls function to get data and stores dictionary in varaible "pop_player"
  t.write(pop_player['Bulls'],False, align = "left", font=("Arial", 20, "bold")) #Calls dictionary to find key
  t.penup
  t.goto(-880, -100)
  t.write("Year founded:",False, align = "left", font=("Arial", 25, "bold"))
  t.goto(-300,-100)
  founded = load_year_founded() #Calls function to get data and stores dictionary in varaible "pop_player"
  t.write(founded['Bulls'],False, align = "left", font=("Arial", 20, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(0,600)
  img = image.FileImage("bulls_logo.gif") #Opens team logo picture
  width = img.get_width() #Grabs picture width
  height = img.get_height() #Grabs picture height
  for row in range(0, height, 10): #Uses nested loop to iterate through each pixel
    for col in range(0, width, 10):
      p = img.get_pixel(col, row) #Gets pixel information
      r = p.red
      g = p.green
      b = p.blue
      t.pencolor(r, g, b)
      t.fillcolor(r, g, b)
      x = col + (width/4) #Adjusts X values
      y = (row * -1) + (height/1.5) #Flips and adjusts Y values
      t.goto(x,y)
      t.stamp()
  t.penup()
  t.goto(-1600,-800)
  for i in range(8): #Loop is used to build repeating skyline
    build1('Chicago') #Call various buildings using team arguement
    build4('Chicago')
    build3('Chicago')
    build2('Chicago')

 
def Boston(): #Creates screen for team
  s.colormode(255)
  t.hideturtle()
  s.bgcolor("forestgreen")
  t.penup()
  t.goto(0,600)
  t.pencolor("white")
  t.write("The Boston Celtics",False, align = "center", font=("Arial", 25, "normal"))
  t.penup()
  t.goto(-880,500)
  t.write("Championship years:",False, align = "left", font=("Arial", 25, "bold"))
  t.penup()
  t.goto(-450,500)
  rings = load_rings() #Calls function to get data and stores dictionary in varaible "rings"
  t.write(rings['Celtics'],False, align = "left", font=("Arial", 16, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(-880, 300)
  t.write("Conference title years:",False, align = "left", font=("Arial", 25, "bold"))
  t.penup()
  t.goto(-420,300)
  conference = load_conference() #Calls function to get data and stores dictionary in varaible "conference"
  t.write(conference['Celtics'],False, align = "left", font=("Arial", 16, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(-880, 100)
  t.write("Most popular player:",False, align = "left", font=("Arial", 25, "bold"))
  t.penup()
  t.goto(-450,100)
  pop_player = load_player() #Calls function to get data and stores dictionary in varaible "pop_player"
  t.write(pop_player['Celtics'],False, align = "left", font=("Arial", 20, "bold")) #Calls dictionary to find key
  t.penup
  t.goto(-880, -100)
  t.write("Year founded:",False, align = "left", font=("Arial", 25, "bold"))
  t.goto(-450,-100)
  founded = load_year_founded() #Calls function to get data and stores dictionary in varaible "pop_player"
  t.write(founded['Celtics'],False, align = "left", font=("Arial", 20, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(0,800)
  img = image.FileImage("celtics_logo.gif") #Opens team logo picture
  width = img.get_width() #Grabs picture width
  height = img.get_height() #Grabs picture height
  for row in range(0, height, 5): #Uses nested loop to iterate through each pixel
    for col in range(0, width, 5):
      p = img.get_pixel(col, row) #Gets pixel information
      r = p.red
      g = p.green
      b = p.blue
      t.pencolor(r, g, b)
      t.fillcolor(r, g, b)
      x = col + (width/2) #Adjusts X values
      y = (row * -1) + (width/2) #Flips and adjusts Y values
      t.goto(x,y)
      t.stamp()
  t.penup()
  t.goto(-1600,-800)
  for i in range(8): #Loop is used to build repeating skyline
    build1('Boston') #Call various buildings using team arguement
    build4('Boston')
    build3('Boston')
    build2('Boston')

 
def Los_Angeles(): #Creates screen for team
  s.colormode(255)
  t.hideturtle()
  s.bgcolor("darkgoldenrod")
  t.penup()
  t.goto(0,600)
  t.pencolor("white")
  t.write("The Los Angeles Lakers",False, align = "center", font=("Arial", 25, "normal"))
  t.penup()
  t.goto(-880,500)
  t.write("Championship years:",False, align = "left", font=("Arial", 25, "bold"))
  t.penup()
  t.goto(-350,500)
  rings = load_rings() #Calls function to get data and stores dictionary in varaible "rings"
  t.write(rings['Lakers'],False, align = "left", font=("Arial", 16, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(-880, 300)
  t.write("Conference title years:",False, align = "left", font=("Arial", 25, "bold"))
  t.penup()
  t.goto(-350,300)
  conference = load_conference() #Calls function to get data and stores dictionary in varaible "conference"
  t.write(conference['Lakers'],False, align = "left", font=("Arial", 16, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(-880, 100)
  t.write("Most popular player:",False, align = "left", font=("Arial", 25, "bold"))
  t.penup()
  t.goto(-350,100)
  pop_player = load_player() #Calls function to get data and stores dictionary in varaible "pop_player"
  t.write(pop_player['Lakers'],False, align = "left", font=("Arial", 20, "bold")) #Calls dictionary to find key
  t.penup
  t.goto(-880, -100)
  t.write("Year founded:",False, align = "left", font=("Arial", 25, "bold"))
  t.goto(-350,-100)
  founded = load_year_founded() #Calls function to get data and stores dictionary in varaible "pop_player"
  t.write(founded['Lakers'],False, align = "left", font=("Arial", 20, "bold")) #Calls dictionary to find key
  t.penup() 
  t.goto(0,600)
  img = image.FileImage("lakers_logo.gif") #Opens team logo picture
  width = img.get_width() #Grabs picture width
  height = img.get_height() #Grabs picture height
  for row in range(0, height, 8): #Uses nested loop to iterate through each pixel
    for col in range(0, width, 5):
      p = img.get_pixel(col, row) #Gets pixel information
      r = p.red
      g = p.green
      b = p.blue
      t.pencolor(r, g, b)
      t.fillcolor(r, g, b)
      x = col + (width/3.5) #Adjusts X values
      y = (row * -1) + (height/2) #Flips and adjusts Y values
      t.goto(x,y)
      t.stamp()
  t.penup()
  t.goto(-1600,-800)
  for i in range(8): #Loop is used to build repeating skyline
    build1('Los_Angeles') #Call various buildings using team arguement
    build4('Los_Angeles')
    build3('Los_Angeles')
    build2('Los_Angeles')

def San_Antonio(): #Creates screen for team
  s.colormode(255)
  t.hideturtle()
  s.bgcolor("grey13")
  t.penup()
  t.goto(0,600)
  t.pencolor("white")
  t.write("The San Antonio Spurs",False, align = "center", font=("Arial", 25, "normal"))
  t.penup()
  t.goto(-880,500)
  t.write("Championship years:",False, align = "left", font=("Arial", 25, "bold"))
  t.penup()
  t.goto(-300,500)
  rings = load_rings() #Calls function to get data and stores dictionary in varaible "rings"
  t.write(rings['Spurs'],False, align = "left", font=("Arial", 16, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(-880, 300)
  t.write("Conference title years:",False, align = "left", font=("Arial", 25, "bold"))
  t.penup()
  t.goto(-300,300)
  conference = load_conference() #Calls function to get data and stores dictionary in varaible "conference"
  t.write(conference['Spurs'],False, align = "left", font=("Arial", 16, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(-880, 100)
  t.write("Most popular player:",False, align = "left", font=("Arial", 25, "bold"))
  t.penup()
  t.goto(-300,100)
  pop_player = load_player() #Calls function to get data and stores dictionary in varaible "pop_player"
  t.write(pop_player['Spurs'],False, align = "left", font=("Arial", 20, "bold")) #Calls dictionary to find key
  t.penup
  t.goto(-880, -100)
  t.write("Year founded:",False, align = "left", font=("Arial", 25, "bold"))
  t.goto(-300,-100)
  founded = load_year_founded() #Calls function to get data and stores dictionary in varaible "pop_player"
  t.write(founded['Spurs'],False, align = "left", font=("Arial", 20, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(0,600)
  img = image.FileImage("spurs_logo.gif") #Opens team logo picture
  width = img.get_width() #Grabs picture width
  height = img.get_height() #Grabs picture height
  for row in range(0, height, 10): #Uses nested loop to iterate through each pixel
    for col in range(0, width, 10):
      p = img.get_pixel(col, row) #Gets pixel information
      r = p.red
      g = p.green
      b = p.blue
      t.pencolor(r, g, b)
      t.fillcolor(r, g, b) 
      x = col + (width/4) #Adjusts X values
      y = (row * -1) + (height/1.5) #Flips and adjusts Y values
      t.goto(x,y)
      t.stamp()
  t.penup()
  t.goto(-1600,-800)
  for i in range(8): #Loop is used to build repeating skyline
    build1('San_Antonio') #Call various buildings using team arguement
    build4('San_Antonio')
    build3('San_Antonio')
    build2('San_Antonio')


 
def load_rings(): #Function that loads championships years through a txt file
  file = open('championships.txt')
  contents = file.readlines()
  rings = {} #Creates dictionary
  years = ""
  for i in range(len(contents)): #Loops through unfiltered contents
    list = contents[i] #Makes each line of file a list
    list = list.split() #Splits string
    team_name = list[0] #Uses index for team name
    for i in range(1,len(list)): #Loops through values without teamname
      temp = list[1:] #Adds sliced values
      years = ' '.join(temp) #Joins values in temp as a string
      rings[team_name] = years #Adds years to dictionary
  return rings
def San_Francisco(): #Creates screen for team
  s.colormode(255)
  t.hideturtle()
  s.bgcolor("blue2")
  t.penup()
  t.goto(0,600)
  t.pencolor("white")
  t.write("The Golden State Warriors",False, align = "center", font=("Arial", 25, "normal"))
  t.penup()
  t.goto(-880,500)
  t.write("Championship years:",False, align = "left", font=("Arial", 25, "bold"))
  t.penup()
  t.goto(-300,500)
  rings = load_rings() #Calls function to get data and stores dictionary in varaible "rings"
  t.write(rings['Warriors'],False, align = "left", font=("Arial", 16, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(-880, 300)
  t.write("Conference title years:",False, align = "left", font=("Arial", 25, "bold")) 
  t.penup()
  t.goto(-300,300)
  conference = load_conference() #Calls function to get data and stores dictionary in varaible "conference"
  t.write(conference['Warriors'],False, align = "left", font=("Arial", 16, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(-880, 100)
  t.write("Most popular player:",False, align = "left", font=("Arial", 25, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(-300,100)
  pop_player = load_player() #Calls function to get data and stores dictionary in varaible "pop_player"
  t.write(pop_player['Warriors'],False, align = "left", font=("Arial", 20, "bold")) #Calls dictionary to find key
  t.penup
  t.goto(-880, -100)
  t.write("Year founded:",False, align = "left", font=("Arial", 25, "bold"))
  t.goto(-300,-100)
  founded = load_year_founded() #Calls function to get data and stores dictionary in varaible "pop_player"
  t.write(founded['Warriors'],False, align = "left", font=("Arial", 20, "bold")) #Calls dictionary to find key
  t.penup()
  t.goto(0,600)
  img = image.FileImage("warriors_logo.gif") #Opens team logo picture
  width = img.get_width() #Grabs picture width
  height = img.get_height() #Grabs picture height
  for row in range(0, height, 8): #Uses nested loop to iterate through each pixel
    for col in range(0, width, 8):
      p = img.get_pixel(col, row) #Gets pixel information
      r = p.red
      g = p.green
      b = p.blue
      t.pencolor(r, g, b)
      t.fillcolor(r, g, b)
      x = col + (width/1.5) #Adjusts X values
      y = (row * -1) + (height/1.5) #Flips and adjusts Y values
      t.goto(x,y)
      t.stamp()
  t.penup()
  t.goto(-1600,-800)
  for i in range(8): #Loop is used to build repeating skyline
    build1('San_Francisco') #Call various buildings using team arguement
    build4('San_Francisco')
    build3('San_Francisco')
    build2('San_Francisco')

 
def load_conference(): #Function that loads championships years through a txt file
  file = open('conference_titles.txt')
  contents = file.readlines()
  conference = {} #Creates dictionary
  years = ""
  for i in range(len(contents)): #Loops through unfiltered contents
    list = contents[i] #Makes each line of file a list
    list = list.split() #Splits string
    team_name = list[0] #Uses index for team name
    for i in range(1,len(list)): #Loops through values without teamname
      temp = list[1:] #Adds sliced values
      years = ' '.join(temp) 
      conference[team_name] = years #Adds years to dictionary
  return conference
 
def load_player(): #Function that loads most well known player through a txt file
  file = open('most_well_known_player.txt')
  contents = file.readlines()
  pop_player = {} #Creates dictionary
  for i in range(len(contents)): #Loops through unfiltered contents
    list = contents[i] #Makes each line of file a list
    list = list.split() #Splits string
    team_name = list[0] #Uses index for team name
    for i in range(1,len(list)): #Loops through values without teamname
      player_name = list[1:] #Adds players name to list
      temp = player_name[0] + " " + player_name[1] #String concatenates two values in list
      player_name = temp
      pop_player[team_name] = player_name #Adds playername to dictionary
  return pop_player
 
def load_year_founded(): #Function that loads year founded through a txt file
  file = open('years_founded.txt')
  contents = file.readlines()
  founded = {} #Creates dictionary
  year = ""
  for i in range(len(contents)): #Loops through unfiltered contents
    list = contents[i] #Makes each line of file a list
    list = list.split() #Splits string
    team_name = list[0] #Uses index for team name
    for i in range(1,len(list)): #Loops through values without teamname
      year_founded = list[1] #Uses index get year
      founded[team_name] = year_founded #Adds year to dictionary
  return founded

main_menu() #Makes menu
s.clearscreen() #Clears screen for next display
eastern() #Makes eastern conference menu
s.clearscreen()
Philadelphia() #Makes Philadelphia menu
s.clearscreen()
Chicago() #Makes Chicago menu
s.clearscreen()
Boston() #Makes Boston menu
s.clearscreen()
western()
s.clearscreen()
Los_Angeles() #Makes Los_Angeles menu
s.clearscreen()
San_Antonio() #Makes San_Antonio menu
s.clearscreen()
San_Francisco() #Makes San_Francisco menu
s.clearscreen()

turtle.mainloop() 

 
 

