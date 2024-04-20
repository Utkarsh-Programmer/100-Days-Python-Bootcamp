# Using prettytable package.

from prettytable import PrettyTable

# Define the table with column names
table = PrettyTable(["Name", "Age", "City"])

# Add rows of data (can include different data types)
table.add_row(["Alice", 30, "New York"])
table.add_row(["Bob", 25, "London"])
table.add_row(["Charlie", 42, "Paris"])

# Print the table in a user-friendly format
print(table)
