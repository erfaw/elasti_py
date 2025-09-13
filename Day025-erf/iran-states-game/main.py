import turtle, os; os.system('cls');
import pandas as pd
image = "./Day025-erf/iran-states-game/bg_resized.gif"

#prepare screen and background image
sc = turtle.Screen()
sc.title("Iran States Game")
sc.addshape(image)
turtle.shape(image)
states_data = pd.read_csv("./Day025-erf/iran-states-game/31_states.csv").loc[:, ["state", "xcor", "ycor"]]

class CorrectNameWriter(turtle.Turtle):
    def __init__(self,):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("red")
    def on_map(self, state_name):
        self.goto(
            int(states_data[states_data["state"] == state_name]["xcor"]),
            int(states_data[states_data["state"] == state_name]["ycor"]),
        )
        self.write(f"{state_name}", False, "center", ("Arial", 12, "bold"))

turtle_write = CorrectNameWriter()


correct_list = set()
wrong_guess = 0
tries_num = 0
def process_user_guess():
    for sn in states_data["state"]:
        if answer_state == sn and answer_state not in correct_list:
            tries_num += 1
            print(f"GZ✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔")
            turtle_write.on_map(answer_state)
            correct_list.add(answer_state)
            break  
        elif answer_state == sn and answer_state in correct_list:
            print(f"you correctly guessed {answer_state} already")
        else:
            wrong_guess += 1

def normalize_fa_ar(text):
    return (
        text.replace("ي", "ی")  # عربی -> فارسی
            .replace("ك", "ک")
    )

while True:
    #get guess from user
    answer_state = normalize_fa_ar(
        sc.textinput("حدس بزنید...",prompt="Enter Persian name of the IRAN states | نام فارسی استان های ایران را وارد کنید")
        )
    os.system('cls')
    process_user_guess()

sc.exitonclick()