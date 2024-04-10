# function with output
def format_name(f_name, l_name):
    # .title() methods converts string into the title case.
    full_name = (f_name+" "+l_name).title()
    # return statement is used inside a function to exit the function and optionally return a value back to the caller.
    return full_name


print(format_name("angElA", "yU"))
