# multiple return values
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    full_name = (f_name+" "+l_name).title()
    return full_name


print(format_name(
    f_name=input("Enter your first name : "),
    l_name=input("Enter your last name : ")
))
