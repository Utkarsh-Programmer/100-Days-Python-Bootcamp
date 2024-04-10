# Exercise 2
# Travel Log.

# DON'T CHANGE THE CODE BELOW
country = input("Enter the country name you visited : ")
visits = input("How many times you visited : ")
# eval() function is used
list_of_cities = eval(
    input("Enter the cities you've traveled, inside 'quotes': "))
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },

    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

# WRITE YOUR CODE HERE
# ------------------------------------------------------------------------------------------------------------------------------------------


def add_new_country(name, time_visited, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = time_visited
    new_country["cities"] = cities_visited
    # .append() method adds item to the end of the dictionary
    travel_log.append(new_country)

# ------------------------------------------------------------------------------------------------------------------------------------------


# DON'T CHANGE THE CODE BELOW
add_new_country(country, visits, list_of_cities)
print(
    f"I've been travel to {travel_log[2]["country"]}  {
        travel_log[2]["visits"]} times."
)
print(f"My favorite city was {travel_log[2]["cities"][0]}.")
