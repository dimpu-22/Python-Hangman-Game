import random

# -----------------------------
# HANGMAN STAGES
# -----------------------------
hangman_stages = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]

# -----------------------------
# WORD CATEGORIES
# -----------------------------
categories = {
    "Programming": [
        "python",
        "computer",
        "variable",
        "function",
        "compiler"
    ],

    "Fruits": [
        "apple",
        "banana",
        "orange",
        "mango",
        "grapes"
    ],

    "Animals": [
        "tiger",
        "elephant",
        "giraffe",
        "rabbit",
        "monkey"
    ]
}

wins = 0
losses = 0

print("=======================================")
print("      WELCOME TO HANGMAN GAME")
print("=======================================")

while True:

    print("\nChoose a Category:")
    print("1. Programming")
    print("2. Fruits")
    print("3. Animals")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        category = "Programming"
    elif choice == "2":
        category = "Fruits"
    elif choice == "3":
        category = "Animals"
    else:
        print("Invalid Choice!")
        continue

    secret_word = random.choice(categories[category])

    hidden_word = []

    for letter in secret_word:
        hidden_word.append("_")

    guessed_letters = []

    attempts = 6

    print("\nCategory:", category)

    while attempts > 0:

        print(hangman_stages[6 - attempts])

        print("\nWord:")
        print(" ".join(hidden_word))

        print("\nGuessed Letters:", " ".join(guessed_letters))

        print("Remaining Attempts:", attempts)

        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:

            print("Correct Guess!")

            for i in range(len(secret_word)):

                if secret_word[i] == guess:
                    hidden_word[i] = guess

        else:

            print("Wrong Guess!")

            attempts -= 1

        if "_" not in hidden_word:

            print("\n=======================================")
            print("🎉 CONGRATULATIONS!")
            print("You guessed the word:", secret_word)
            print("=======================================")

            wins += 1
            break

    if attempts == 0:

        print(hangman_stages[6])

        print("\n=======================================")
        print("💀 GAME OVER!")
        print("The word was:", secret_word)
        print("=======================================")

        losses += 1

    print("\n========== SCORE ==========")
    print("Wins   :", wins)
    print("Losses :", losses)
    print("===========================")

    again = input("\nDo you want to play again? (y/n): ").lower()

    if again != "y":
        print("\nThank you for playing Hangman!")
        print("Final Score")
        print("Wins   :", wins)
        print("Losses :", losses)
        print("Goodbye!")
        break