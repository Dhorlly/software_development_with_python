##
#Simple game that allows users to guess a number
##

print(
        """
        +===============================+
        | Welcome to my game, muggle    |
        | Enter an integer number       |
        | and guess what number         |
        | I've picked for you.          |
        | So, what's the                |
        | secret                        |
        | number?                       |
        +===============================+
        """)

secret_number = 101
number = int(input("Enter the number: "))

while number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Enter the number: "))
print("Well done, muggle! You are free now")
