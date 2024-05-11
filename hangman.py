import random
def choose_word():
    words=["apple","orange","blueberry","mango","peach","jellyfruit"]
    return random.choice(words)
def display_word(word,guessed_letters):
    display=""
    for letter in word:
        if letter in guessed_letters:
            display+=letter
        else:
            display+="_"
    return display

def hangman():
    word=choose_word()
    guessed_letters=[]
    attempts=6
    print("Welcome to hangman")
    print("Guess the word")
    while attempts > 0:
        print("\n" + display_word(word,guessed_letters))
        guess=input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You have already guessed the word")
            continue
        if guess in word:
            print("Good Guess")
            guessed_letters.append(guess)
        if guess not in word:
            attempts-=1
            print(f'wrong Guess. Atempts remaining: {attempts}')
            if attempts==0:
                print("Sorry,You are out of attempts: The word was",word)
        else:
            if "_" not in display_word(word,guessed_letters):
                print(f"congratulations, you have guessed the word,{word}")
                break
hangman()
