import turtle, os; os.system('cls');
import pandas as pd
image = "./Day025-erf/iran-states-game/bg_resized.gif"

#prepare screen and background image
sc = turtle.Screen()
sc.title("Iran States Game")
sc.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("./Day025-erf/iran-states-game/31_states.csv").loc[:, ["state", "xcor", "ycor"]]

corrects = 0
def process_user_guess():
    for sn in states_data["state"]:
        if answer_state == sn:
            print(f"GZ✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔")
            # 1. show name state on map
            # 2. append to a list named {right list}
            # 3. increase number of correct states
        else:
            pass

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