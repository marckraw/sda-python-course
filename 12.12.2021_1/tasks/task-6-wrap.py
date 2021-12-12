from textwrap import wrap

def format_phone_number(number, area_code="+48", delimiter=" "):
    divided_number = wrap(number, 3)
    return f"{area_code} (0) {divided_number[0]}{delimiter}{divided_number[1]}{delimiter}{divided_number[2]}"


print( format_phone_number('579995799') )
print( format_phone_number('766081621', '+41') )
print( format_phone_number('766081621', '+41', '-') )
print( format_phone_number('766081621', '+41', '+') )


##################################################################################################
from textwrap import wrap

def format_phone_number_new(number, area_code="+48", delimiter=" "):
    divided_number = wrap(number, 3)
    return f"{area_code} (0) {delimiter.join(divided_number)}"


print( format_phone_number('579995799') )
print( format_phone_number('766081621', '+41') )
print( format_phone_number('766081621', '+41', '-') )
print( format_phone_number('766081621', '+41', '+') )
