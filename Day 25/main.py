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
#
# data = pandas.read_csv("./weather_data.csv")
#
# data_dict = data.to_dict()
# print(data.temp.max())
#
# monday = data[data.day == "Monday"]
# monday_temp = (monday.temp[0] * 9 / 5) + 32
# print(monday_temp)

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur = data["Primary Fur Color"]


gray = 0
cinnamon = 0
black = 0

for i in fur:
    if i == "Gray":
        gray = gray + 1
    if i == "Cinnamon":
        cinnamon = cinnamon + 1
    if i == "Black":
        black = black + 1


fur_dict = {"Fur Color": ["gray", "cinnamon", "black"], "Count": [gray, cinnamon, black]}
fur_df = pandas.DataFrame(data=fur_dict)

fur_df.to_csv("./squrriel_count.csv")
