from PIL import Image 
img = Image.open("blank_states_img.gif")
img = img.resize((1000,800))
img.save("bg_resized.gif")
