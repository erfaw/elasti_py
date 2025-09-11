import turtle, os; os.system('cls');

import pandas as pd
image = "./Day025-erf/iran-states-game/bg_resized.gif"
sc = turtle.Screen()
sc.title("Iran States Game")
sc.addshape(image)
turtle.shape(image)

data_dict = {
    "state":[],
    "xcor" : [],
    "ycor" : []
}

def update_csv():
    states_data = pd.DataFrame(data_dict)
    states_data.to_csv("./Day025-erf/iran-states-game/31_states.csv")

def get_mouse_click_coor(x, y):
    print(x, y)
    state_name = input('state_name ? =')
    if state_name == 'done()':
        update_csv()
    else:
        data_dict["state"].append(state_name)
        data_dict["xcor"].append(x)
        data_dict["ycor"].append(y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
