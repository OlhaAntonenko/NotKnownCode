"""
*** Task 5 ***
Write a script to convert decimal to hexadecimal
		Sample decimal number: 30, 4
		Expected output: 1e, 04
"""

numbers = str(input()).split(",")
hex_numbers = [format(int(i), "02x") for i in numbers]
print(*hex_numbers, sep=", ")
