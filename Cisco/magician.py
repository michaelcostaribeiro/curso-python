secret_number = 777

number = int(input(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
"""))

while number!= secret_number:
    print("""+===============================+
|Ha ha! You're stuck in my loop!|
+===============================+""")
    number = int(input("""+========================+
|What is your next guess?|
+========================+"""))



print("+===+\n"+"|",number,"|\n"+"+===+", sep ="")

print("""+====================================+
|Well done, muggle! You are free now.|
+====================================+""")
