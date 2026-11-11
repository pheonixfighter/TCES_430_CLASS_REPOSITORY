# Robert Cromer
# test_loop.py
# This file contains the code to verify that the while loop written in the code is correct
# This was written as a script since it was just meant to test if the assembly loop was coded \
# correctly

# constants in the ASM code
A = 0
B = 1

i = 1
j = 0
k = -1

while i > j:
    i = i + A - 2 * j
    if j >= k:
        i = i + 2
        k = k - B + 2 * j
    j += 1
    print(i, " ", j, " ", k)
#end of loop

print(i, " ", j, " ", k)


