from flask import Flask
from random import randint

app = Flask(__name__)

# A random number for game between 0 and 9
random_number = randint(0, 9)

# Build home page in order to ask numbers
@app.route('/')
def home_page():
    return '<h1>Guess a number between 0 and 9 then type it in url...<h1/>'\
            '<img style="width: 800px;" src="https://media.wnyc.org/i/1500/1111/l/80/1/Numbers.png"/>'

@app.route('/<int:guess_num>')
def figure_guess(guess_num):
    so_high_img_link = "https://i1.sndcdn.com/artworks-000081672164-bkid9g-t500x500.jpg"
    so_low_img_link = "https://i.scdn.co/image/ab67616d00001e02ce97085f21cb7a60554b2ae3"
    done_img_link = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsd7TB_WYx0N2V6Wlu0uOUsP6chMQHOBNjyQ&s"
    idiot_img_link = "https://w0.peakpx.com/wallpaper/431/994/HD-wallpaper-dwight-schrute-quote-office-comedy-dwight-idiot-tv-show-series-schrite-quote-the.jpg"
    def to_return(pic, direction):
        return  f'<h1>its {direction} than that...<h1/>'\
                f'<img src="{pic}" />'
    
    if not 0 <= guess_num <= 9:
        return  f'<h1>must be between 0 and 9, idiot...<h1/>'\
                f'<img src="{idiot_img_link}"/>'

    elif guess_num > random_number:
        return to_return(so_high_img_link, "lower")
        
    elif guess_num < random_number:
        return to_return(so_low_img_link, "higher")
    
    elif guess_num == random_number:
        return  f'<h1>its COOORRRRREECTTTTT !!!<h1/>'\
                f'<img src="{done_img_link}" />'

    else:
        return f'something went wrong!...'
    
@app.route('/restart')
def restart_game():
    global random_number
    # A random number for game between 0 and 9
    random_number = randint(0, 9)

if __name__ == "__main__":
    app.run(debug= True)