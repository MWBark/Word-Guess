from random_word import Wordnik
import requests

wordnik_service = Wordnik()
currentscore = 0
highscore = 0


def check_api():
    """
    Checks whether the API is running.
    If not, prints message.
    """
    req = requests.get("https://status.wordnik.com/").status_code

    if req != 200:
        print("The Wordnik API used to generate the random words appears to be down. Check status at https://status.wordnik.com/.")
        exit()


def new_word():
    """
    Gets a new random word.
    """
    valid = False
    word = ""

    while not valid:
        valid = True
        word = wordnik_service.get_random_word()

        for i in [*word]:
            if i not in list(map(chr, range(97, 123))) and i != '-':
                valid = False

    return word


def create_empty_list(word):
    """
    Creates a number of underscores equal to the random word length
    that will be updated with letters the user guesses.
    """
    empty_list = []

    for i in [*word]:
        if i == '-':
            empty_list += '-'
        else:
            empty_list += "_"

    return empty_list


def display_info(lives, word, empty_list, doesnt_contain, currentscore, highscore):
    """
    Displays word length, letters the word doesn't contain
    and lives to help user guess
    """
    letters_string = ", ".join(doesnt_contain)
    print(f"\nlives:{lives} currentscore:{currentscore} highscore:{highscore}")
    print("." * 38)
    print(f"{len(word)} letters, doesn't contain: {letters_string}\n")
    print(*empty_list)


def get_input(word, empty_list, doesnt_contain, guessed_words):
    """
    Gets user's letter or word guess.
    """
    valid = False
    user_guess = ""

    while not valid:
        valid = True
        user_guess = input("Enter a word or letter:\n")

        if len(user_guess) > 1 and len(user_guess) != len(word):
            valid = False
            print(f"\nIncorrect word length of {len(user_guess)} letters entered\n")   
        if len(user_guess) < 1:
            valid = False
            print("No input was entered\n")
        if user_guess in empty_list or user_guess in doesnt_contain or user_guess in guessed_words:
            valid = False
            print(f"\n'{user_guess}' has already been guessed\n")
        for i in [*user_guess]:
            if i not in list(map(chr, range(97, 123))):
                valid = False
                print(f"\n'{user_guess}' contains invalid characters")
                print("Please use lowercase english alphabet characters\n")
                break

    return user_guess


def check_lives(lives, word, empty_list, doesnt_contain, currentscore, highscore, guessed_words):
    """
    Check the lives. If lives = 0, reset currentscore and run_game,
    else start a new guess.
    """
    if lives == 0:
        print(f"\nBad luck. the word was '{word}'\n")
        currentscore = 0
        run_game(currentscore, highscore)
    else:
        new_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore, guessed_words)


def check_guess(user_guess, lives, word, empty_list, doesnt_contain, currentscore, highscore, guessed_words):
    """
    If guess is a letter, checks whether it's in the random word or not.
    If it is, updates empty_guess and checks if it matches the word.
    If it does, run got_word, else run new_guess.
    If the letter guess isn't in the random word, add it to doesnt_contain,
    minus 1 life, and run check_stats.
    If guess is a word, run got-word if correct, else minus 1 life, add to guessed_words and check_stats
    """
    if len(user_guess) < 2:
        if user_guess in [*word]:
            for i in range(len([*word])):
                if [*word][i] == user_guess:
                    empty_list[i] = user_guess

            if empty_list == [*word]:
                got_word(word, currentscore, highscore)
            else:
                print(f"\n'{user_guess}' is in word\n")
                new_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore, guessed_words)
        else:
            doesnt_contain += user_guess
            print(f"\nword doesn't contain '{user_guess}'\n")
            lives -= 1
            check_lives(lives, word, empty_list, doesnt_contain, currentscore, highscore, guessed_words)
    else:
        if user_guess == word:
                got_word(word, currentscore, highscore)
        else:
            print(f"\nThe word isn't '{user_guess}'")
            guessed_words.append(user_guess)
            lives -= 1
            check_lives(lives, word, empty_list, doesnt_contain, currentscore, highscore, guessed_words)


def got_word(word, currentscore, highscore):
    """
    Run winning end game. Ad 1 to currentscore, update the highscore, then run_game.
    """
    print(f"\nCongrats! The word was '{word}'\n")
    currentscore += 1

    if currentscore > highscore:
        highscore = currentscore

    run_game(currentscore, highscore)


def new_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore, guessed_words):
    """
    Runs through functions to get a new guess from the user.
    """
    display_info(lives, word, empty_list, doesnt_contain, currentscore, highscore)
    user_guess = get_input(word, empty_list, doesnt_contain, guessed_words)
    check_guess(user_guess, lives, word, empty_list, doesnt_contain, currentscore, highscore, guessed_words)


def run_game(currentscore, highscore):
    """
    Run functions to set up game
    """
    check_api()
    word = new_word()
    empty_list = create_empty_list(word)
    doesnt_contain = []
    guessed_words = []
    lives = 0
    lives = len(word)
    new_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore, guessed_words)


print("""
WELCOME TO WORD GUESS!

Guess the random words generated from Wordnik. Enter letters to fill in the
blank letter spaces or guess the whole word. Letter guesses and incorrect word
guesses cost life points. Life points equal to the length of the random word
are added for each new word. Guess the word before your life points reach 0.
Successful guesses score a point.

Please visit Wordnik.com and enter any words that come up to find out more
about them.

Let's Play!
""")


run_game(currentscore, highscore)
