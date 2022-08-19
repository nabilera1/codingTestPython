integers = [1, 2, 3]

strings = [str(integer) for integer in integers]
a_string = "".join(strings)
an_integer = int(a_string)

print(an_integer)