# Squirrel Census Data Analysis
import pandas as pd

# reading csv
data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# gray squirrels
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])

# red squirrels
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

# black squirrels
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# making data frame
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")
