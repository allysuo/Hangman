import random

#Base:
word_bank = ["chiken", "dog", "horse", "cat", "mango", "banana", "sick", "house"]
word = random.choice(word_bank) #It's going to choose a random word from the bank we created
guessWord = ['_'] * len(word)
attempts = 10

#Saying if it's right or not:
while attempts > 0:
    print("\nCurrent word " + " ".join(guessWord))
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessWord[i] = guess
        print("Great guess!")
    else:
        attempts -= 1
        print(f"Eh... it wasn't that one. You have {attempts} attempts left.")
    

    if "_" not in guessWord:
        print(f"Congratulations! You've guessed the word: {word}")
        break

    if attempts == 0 and "_" in guessWord:
        print(f"Game over. The word was: {word}")