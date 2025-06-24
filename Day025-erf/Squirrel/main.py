import pandas
import os; os.system('cls')

file_path = "./Day025-erf/Squirrel/004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv"
target_column = "Primary Fur Color"
data = pandas.read_csv(file_path)

data_g = data.groupby(target_column)[target_column].size()

data_dict = {
    target_column: data_g.index,
    "count": data_g.values
}
print(data.groupby(target_column).size())
my_data_frame = pandas.DataFrame(data_dict)
my_data_frame.to_csv("./Day025-erf/Squirrel/Squirrel-count.csv")
