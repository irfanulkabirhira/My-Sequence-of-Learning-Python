import random

stages = ['''
 +----+
 |    |
 0    |
/|\   |
/ \   |
      |
==========
''', '''
 +----+
 |    |
 0    |
/|\   |
/     |
      |
==========

''', '''
 +----+
 |    |
 0    |
/|\   |
      |   
==========
''', '''

 +----+
 |    |
 0    |
/|    |     
      |
      |
==========

''', '''
 +----+
 |    |
 0    |
 |    |
      |
      |     
==========

''', '''
 +----+
 |    |
 0    |
      |
      |
==========
''', '''
 +----+
 |    |
      |
      |
      |
==========

''']

# Step 1:
word_list = ["hira", "muktha", "manik"]

# Create a variable names "Lives" to keep tracking of Lives lieft
# set 'Lives' to equal = 0 initially
lives = 6


# The 'choice' method from the 'random' module is used to select a random element from a non-empty sequence
chosen_word = random.choice(word_list)
print(chosen_word)

# Step 2:
""" To Create a Placeholder """
placeholder = ""
word_lentgh = len(chosen_word)
for position in range(word_lentgh):
    placeholder += "_"
print(placeholder)

# Step 3:
""" Use a while loop to let user guess again """

# let initially game is not over
game_over = False
# Initially Correct letter = 0
correct_letters = []

while not game_over:
    # Update the code below to tell the user how many lives they have left
        print(f"*********<???> {lives}/6 lives left *******")
    # The .lower() method is applied to ensure that the user's input is converted to lowercase,
    # regardless of whether they type uppercase or lowercase letters.
        guess = input("Guess a lower letter: ").lower()
    # The Word that user already guessed , Print the letter
        display = ""
        for letter in chosen_word:
            if letter == guess:
                display += letter
                # The append method is used to add an element to the end of a
                # list that's why the previous chosen word would be there too
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
        print(display)

        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                game_over = True
                print(f"******** Is was {chosen_word}! You loss the game !!")
        if "_" not in display:
            game_over = True
            print("********You win !!!**********")
        print(stages[lives])




