def format_phone_number(number, area_code="+48", delimiter=" "):
    amount_to_take = 3
    divided_number = [number[x*amount_to_take:amount_to_take*x+amount_to_take] for x in range(amount_to_take)]

    return f"{area_code} (0) {divided_number[0]}{delimiter}{divided_number[1]}{delimiter}{divided_number[2]}"


print( format_phone_number('579995799') )
print( format_phone_number('766081621', '+41') )
print( format_phone_number('766081621', '+41', '-') )
print( format_phone_number('766081621', '+41', '+') )
