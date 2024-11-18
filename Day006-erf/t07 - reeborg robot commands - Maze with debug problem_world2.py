# solve "problem_world2"
def turn_right():
    turn_left()
    turn_left()
    turn_left()
  

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

n_t_r = 0
while not at_goal() :
    if right_is_clear():
        turn_right()
        move()
        n_t_r += 1
        if n_t_r >= 5 and front_is_clear():
            move()
    elif front_is_clear():
        move()
        n_t_r = 0
    else:
        turn_left()
    
