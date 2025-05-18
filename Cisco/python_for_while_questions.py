#Question 1: Create a for loop that counts from 0 to 10, and prints odd numbers to the screen.
print("0 to 10 in a for structure")

for i in range(1, 11):
    print(i, end=" ")
    if i % 2 == 1:
        print("\nodd number:", i)

#Question 2: Create a while loop that counts from 0 to 10, and prints odd numbers to the screen.
print("\n\n0 to 10 in a while structure")

x = 1
while x < 11:
    if x % 2 ==1:
        print("\nodd number:", x)
    else:
        print(x)
    x+= 1

#Question 3: Create a program with a for loop and a break statement. The program should iterate
#over characters in an email address, exit the loop when it reaches the @ symbol, and print the
#part before @ on one line.
print("\n\nemail without @.com")

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    else:
        print(ch, end ="")

#Question 4: Create a program with a for loop and a continue statement. The program should iterate over
#a string of digits, replace each 0 with x, and print the modified string to the screen.
print("\n\nreplace 0 for x")

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        # Line of code.
    else:
        print(digit, end="")

print()
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
    
