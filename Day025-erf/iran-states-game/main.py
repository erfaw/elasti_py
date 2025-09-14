import turtle, os, time; os.system('cls');
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
start_time = time.time()

def update_timer():
    elapsed = int(time.time() - start_time)
    formated = time.strftime("%H:%M:%S", time.gmtime(elapsed))
    sc.title(f"Iran States Game | Time elapsed: {formated}")
    sc.ontimer(
        update_timer,
        1000
    )
    
def process_user_guess():
    # global tries_num, wrong_guess
    for sn in states_data["state"]:
        if answer_state == sn and answer_state not in correct_list: 
            print(f"GZ✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔")
            turtle_write.on_map(answer_state)
            correct_list.add(answer_state)
            break  
        elif answer_state == sn and answer_state in correct_list:
            print(f"you correctly guessed {answer_state} already")
        else:
            pass
    # tries_num += 1

def normalize_fa_ar(text):
    return (
        text.replace("ي", "ی")  # عربی -> فارسی
            .replace("ك", "ک")
    )

def calculate_stars(tries_num, wrong_guess, whole_time):
    """
    MADE BY GPT
    محاسبه تعداد ستاره‌ها بر اساس:
    - tries_num: تعداد تلاش‌های کاربر
    - wrong_guess: تعداد جواب‌های غلط
    - whole_time: زمان کل بازی بر حسب ثانیه
    """
    # --- نرمال‌سازی فاکتورها ---
    efficiency_score = 31 / tries_num
    accuracy_score = max(0, (31 - wrong_guess) / 31)
    # فرض: بهترین زمان 10 دقیقه، بدترین 30 دقیقه
    time_score = max(0, min(1, (1800 - whole_time) / 1200))

    # --- ترکیب وزن‌دار ---
    final_score = (0.5 * efficiency_score) + (0.3 * accuracy_score) + (0.2 * time_score)

    # --- تبدیل به ستاره ---
    stars = round(final_score * 5)

    # اطمینان از بازه 0 تا 5
    stars = max(0, min(5, stars))

    return stars


answer_state = normalize_fa_ar(
    sc.textinput("حدس بزنید...",prompt="Enter Persian name of the IRAN states | نام فارسی استان های ایران را وارد کنید")
    )
while True:
    #get guess from user
    update_timer()
    process_user_guess()
    tries_num += 1
    wrong_guess = int(tries_num - len(correct_list))
    if len(correct_list) == len(states_data['state']):
        break
    answer_state = normalize_fa_ar(
        sc.textinput(
            f"corrects {len(correct_list)}/{len(states_data['state'])} | wrongs: {wrong_guess} | tries: {tries_num}",
            prompt="Enter Persian name of the IRAN states | نام فارسی استان های ایران را وارد کنید")
    )
whole_time = time.time()-start_time
star_score = calculate_stars(tries_num, wrong_guess, whole_time)
print(star_score)

sc.exitonclick()