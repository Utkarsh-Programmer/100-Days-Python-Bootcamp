import pandas
import csv

# NOTE: csv method allows the functionality to read and write the CSV(comma separated values) files.


# Reading CSV file using 'csv' built-in module
"""
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)  # read csv file row by row
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(row[1])
    print(temperature)
"""

# Reading CSV file using 'pandas' module
data = pandas.read_csv("weather_data.csv")
# print(data)
print(data["temp"])
