import colorgram

colors_of_pic = colorgram.extract(r"C:\Users\ErF\Desktop\python\elasti_py\Day018-erf\image.jpg", 10)

colors = []

for each in colors_of_pic:
    colors_list = []
    colors_list.append(each.rgb.r)
    colors_list.append(each.rgb.g)
    colors_list.append(each.rgb.b)
    colors.append(tuple(colors_list))

print(colors)

