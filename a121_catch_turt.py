
# a121_catch_a_turtle.pnew_ypos
#-----import statements-----
import turtle as trtl
import random
from time import sleep
import leaderboard as lb

#-----wait for start-----
sleep(0)

#-----game configuration----
spot_color = "blue"
spot_size = 10
spot_shape = "classic"
score = 0
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# countdown variables
timer = 60
counter_interval = 1000   #1000 represents 1 second
timer_up = False

# setup font
font_setup = ("Arial", 50, "normal")

# leaderboard
leaderboard_file = "a122_leaderboard.txt"
player_name = input("what is your name?")


#-----initialize turtled-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.color(spot_color)
spot.penup()
spot.speed(0)

# init score_writer
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.speed(0)
score_writer.goto(420,320)
score_writer.color("white")
score_writer.pencolor("white")

# countdown
counter =  trtl.Turtle()
counter.speed(0)
counter.penup()
counter.goto(-460,320)
counter.color("white")
counter.pencolor("white")

#-----game functions--------
def spot_clicked(x, y):
    global timer_up
    global wn
    print("checking...")
    if timer_up == False:
        update_score()
        change_position()
    else:
        print("bye!")
        spot.hideturtle()
        sleep(1)
        wn.bye()

def change_position():
    global colors
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-300,300)
    spot.goto(new_xpos,new_ypos)
    spot.color = random.choice(colors)
    spot.stamp()
    spot.fd(1000)
    spot.fd(-1000)


def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.pencolor("white")
    score_writer.write(score, font=font_setup)
    score_writer.pencolor("black")

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.pencolor("white")
    counter.write("Time's Up", font=font_setup)
    counter.pencolor("black")
    timer_up = True
  else:
    counter.pencolor("white")
    counter.write("Timer: " + str(timer), font=font_setup)
    counter.pencolor("black")
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file)
  leader_scores_list = lb.get_scores(leaderboard_file)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)
        
#-----events----------------
spot.onclick(spot_clicked)

wn = trtl.Screen()
wn.bgcolor("black")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()