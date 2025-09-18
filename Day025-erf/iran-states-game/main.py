import turtle, subprocess, time; subprocess.call("cls", shell=True);
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
    def all_miss(self, misses):
        #print all miss with another color
        self.color("green")
        for sn in misses:
            self.on_map(sn)
        self.color("red")


turtle_write = CorrectNameWriter()

def update_timer():
    """Calculate elapsed time and update it in screen.title()"""
    elapsed = int(time.time() - start_time)
    formated = time.strftime("%H:%M:%S", time.gmtime(elapsed))
    sc.title(f"Iran States Game | Time elapsed: {formated}")
    sc.ontimer(
        update_timer,
        1000
    )
    
def process_user_guess(answer, correct_list):
    for sn in states_data["state"]:
        if answer == sn and answer not in correct_list: 
            turtle_write.on_map(answer)
            correct_list.add(answer)
            break  
        elif answer == sn and answer in correct_list:
            print(f"you correctly guessed {answer} already")
            sc.textinput("Warning", f"you correctly guessed {answer} already, try another one")
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
    # فرض: بهترین زمان 5 دقیقه، بدترین 20 دقیقه
    time_score = max(0, min(1, (900 - whole_time) / 300))

    # --- ترکیب وزن‌دار ---
    final_score = (0.5 * efficiency_score) + (0.3 * accuracy_score) + (0.2 * time_score)

    # --- تبدیل به ستاره ---
    stars = round(final_score * 5)

    # اطمینان از بازه 0 تا 5
    stars = max(0, min(5, stars))

    return stars

end_game_message = ""
def main():
    global start_time, end_game_message
    correct_list = set()
    tries_num = 0
    wrong_guess = 0
    start_time = time.time()

    answer_state = normalize_fa_ar(
        sc.textinput("حدس بزنید...",prompt="Enter Persian name of the IRAN states | نام فارسی استان های ایران را وارد کنید")
        )
    while True:
        #get guess from user
        update_timer()
        process_user_guess(answer_state, correct_list)
        tries_num += 1
        wrong_guess = int(tries_num - len(correct_list))
        if len(correct_list) == len(states_data['state']):
            break
        answer_state = normalize_fa_ar(
            sc.textinput(
                f"corrects {len(correct_list)}/{len(states_data['state'])} | wrongs: {wrong_guess} | tries: {tries_num}",
                prompt="Enter Persian name of the IRAN states | نام فارسی استان های ایران را وارد کنید\ntype 'exit' to refuse continue | را وارد کنید 'exit' برای انصراف و دیدن نمره و جواب نهایی ")
        )
        if answer_state.lower() == 'exit':
            all_states_name = states_data["state"]
            misses = set()
            misses = [state_name for state_name in all_states_name if state_name not in correct_list] # using List Comprehension topic to return 'misses' (from next day lesson) instead of below comments but same functionality :
            # for sn in all_states_name:
            #     if sn not in correct_list:
            #         misses.add(sn)
            turtle_write.all_miss(misses)
            break

    whole_time = time.time()-start_time
    whole_time_formated = time.strftime("%H:%M:%S", time.gmtime(whole_time))
    star_score = calculate_stars(tries_num, wrong_guess, whole_time)
    star_char = '★'
    if len(correct_list) == len(states_data["state"]):
        end_game_message = f"Score:\t{star_score*star_char}\t\t\t\n\nElapsed time: {whole_time_formated}\nAll tries: {tries_num}\nWrong guesses: {wrong_guess}\n\n:برای شروع مجدد 1 را وارد کنید"
    else: 
        end_game_message = f"Score: Failed! \t\t\t\n\nElapsed time: {whole_time_formated}\nAll tries: {tries_num}\nWrong guesses: {wrong_guess}\nMissed: {len(misses)}\n\n:برای شروع مجدد 1 را وارد کنید"


play_again = 1
while play_again == 1:
    turtle_write.clear()
    main()
    #textinput baryae neshon dadane etelaat score o zaman va porsidane inke aya mikhay mojadad bazi kni?
    play_again = sc.numinput(
        "Try Again? | شروع مجدد؟",
        end_game_message,
        1,
        0,
        1
    ) # ==> int num 1 or 0

# prepare closing message
turtle_write.clear()
sc.clear()
sc.bgcolor("black")
turtle_write.goto(0,0)
turtle_write.color("white")
turtle_write.write(arg="Have a Nice Day! | !روز خوبی داشته باشید", 
                   move=False,
                   align = "center",
                   font=("Arial",22,"normal")
                   )

sc.exitonclick()