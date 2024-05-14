# Data Frames and Series
import pandas

# NOTE: A whole table is a 'dataframe' and each column is a 'series'.

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# print(data["temp"])

# converting data to a dictionary
""" 
data_dict = data.to_dict()
print(data_dict)
"""

# converting data to a list
"""  
temp_list = data["temp"].to_list()
print(len(temp_list))
"""

# average temperature
"""  average_temp = round(data["temp"].mean())
print(average_temp)
"""

# highest temperature
""" 
max_temp = data["temp"].max()
print(max_temp)
"""

# get data in columns
"""
print(data["condition"])
print(data.condition)
"""

# checking data in row
""" print(data.day == "Monday") """

# checking day with max temp
""" print(data[data.temp == data.temp.max()]) """

monday = data[data.day == "Monday"]
""" print(monday.condition) """

# monday temp into fahrenheit
"""
monday_temp = monday.temp[0]
monday_temp = monday_temp * 9/5+32
print(monday_temp)
"""

# creating dataframe from a dictionary
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
new_df = pandas.DataFrame(data_dict)
print(new_df)

# creating csv file from the csv data
new_df.to_csv("new_df.csv")
