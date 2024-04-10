# Docstring:
# Used to provide documentation about a module, method, function or a class.

def format_name(f_name, l_name):
    """Takes first name and last name, and format it in the title case, then returns the full name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    full_name = (f_name+" "+l_name).title()
    return full_name


print(format_name(
    f_name=input("Enter your first name : "),
    l_name=input("Enter your last name : ")
))

# ------------------------------------------------------------------------------------------------------------------------------------------
# Multiline Strings
print(
    """
This is a 
multiline
string.
"""
)

print(
    '''
This is also
a multiline
string.
'''
)
