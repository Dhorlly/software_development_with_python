##
# You are stucked in an infinite loop. Enter the keyword to escape
##

print("""
        *********************************
        *    WELCOME TO THE LOOP GAME.  *
        *                               *
        *      YOU ARE STUCK IN AN      *
        *         INFINITE LOOP!        *
        *       TO ESCAPE SAY THE       *
        *            MAGIC WORD         *
        *********************************
        """)
magic_word = "chupacabra"

while True:
    your_input = input("Enter the magic word: ")
    if your_input == magic_word:
        break

print("You've successfully left the loop!")
