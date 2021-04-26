# To convert an IP address to a defanged IP address, we need to replace “.” with “[.]”. During coding interviews, a standard problem for changing an IP address is that you receive a valid IP address, you must return a defanged version of that IP address.
def ip_address_func(ip_address):
    new_address = " "
    split_address = ip_address.split(".")
    seperator = "[.]"
    new_address = seperator.join(split_address)
    return new_address


ip_address = ip_address_func('1.1.2.3')
print(ip_address)
