"""
*** Task 4 ***
Write a script to concatenate N strings.
"""

N = int(input())
s = ""

for i in range(N):
	s += str(input())

print(f"Concatenated strings: {s}")
