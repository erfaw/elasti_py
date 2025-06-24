import os; os.system('cls')
import csv
import pandas;
# with open("./weather_data.csv") as f:
#     data = csv.reader(f)
#     tempratures = []
#     for row in data:
#         print(row)
#         if row[1] == 'temp':
#             continue
#         tempratures.append(
#             int(row[1])
#         )
#     print(tempratures)

data = pandas.read_csv("./weather_data.csv")
# data_dict = data.to_dict()

# temp_list = data['temp']
# print(temp_list) 
# average = data['temp'].mean()
# # average = sum(temp_list) / len(temp_list)
# print(f"average is {average:.2f} C")

print(f"\n\n\nthe maximum temprature is {data['temp'].max()}\n\n")

# my_row = data[data.temp.max()]
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp_F = monday.temp * (9/5) + 32
print(f"monday temp in C is {monday.temp}\nmonday temp in F is {monday_temp_F}")
    

