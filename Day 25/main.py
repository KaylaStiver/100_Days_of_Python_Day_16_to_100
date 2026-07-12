# with open("./weather_data.csv", mode="r") as file:
#     weather_data = file.read().splitlines()

# import csv
# with open("./weather_data.csv", mode="r") as file:
#     weather_data = csv.reader(file, delimiter=",")
#     temperatures = []
#     weather_data.__next__()
#     for row in weather_data:
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("./weather_data.csv")

# data_dict = data.to_dict()
# print(data.temp.max())

monday = data[data.day == "Monday"]
monday_temp = (monday.temp[0] * 9 / 5) + 32
print(monday_temp)