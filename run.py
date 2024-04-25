from random_word import Wordnik

wordnik_service = Wordnik()
currentscore = 0
highscore = 0


def new_word():
    """
    Gets a new random word.
    """
    word = wordnik_service.get_random_word().lower()
    return word


def validate_word(word):
    """
    Checks the random word only contains lowercase english alphabet letters
    or '-'. If not, runs 'run_game' function again.
    """
    for i in [*word]:
        if i not in list(map(chr, range(97, 123))) and i != '-':
            run_game(currentscore, highscore)


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
    print(f"{len(word)} letters, doesn't contain: {letters_string}")
    print(*empty_list)


def get_input():
    """
    Gets user's letter or word guess.
    """
    user_guess = input("Enter a letter or word: \n")
    return user_guess


def validate_input(user_guess, lives, word, empty_list, doesnt_contain, currentscore, highscore):
    """
    Checks the length of the user's word guess matches that of the random word.
    Prints statement and starts new guess if true.
    """
    if len(user_guess) > 1 and len(user_guess) != len(word):
        print(f"\nIncorrect word length of {len(user_guess)} letters entered\n")
        new_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore)
    elif len(user_guess) < 1:
        print("\nNo input was entered\n")
        new_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore)
    elif user_guess in empty_list or user_guess in doesnt_contain:
        print(f"\n'{user_guess}' has already been guessed\n")
        new_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore)
    else:
        for i in [*user_guess]:
            if i not in list(map(chr, range(97, 123))):
                print(f"\n'{user_guess}' contains invalid characters")
                print("Please use lowercase english alphabet characters\n")
                new_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore)


def check_stats(lives, word, empty_list, doesnt_contain, currentscore, highscore):
    """
    Check the user's stats, such as lives.
    Runs a new game or new guess based on lives value.
    """
    if lives == 0:
        print(f"\nBad luck. the word was {word}")
        currentscore = 0
        run_game(currentscore, highscore)
    else:
        new_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore)


def check_guess(user_guess, lives, word, empty_list, doesnt_contain, currentscore, highscore):
    """
    If guess is a letter, checks whether it's in the random word or not.
    If it is, updates empty_guess and checks if it matches the word.
    If it does, run got_word, else run new_guess.
    If the letter guess isn't in the random word, add it to doesnt_contain,
    minus 1 life, and run check_stats.
    If guess is a word, run got-word if correct, else minus 1 life and check_stats
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
                new_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore)
        else:
            doesnt_contain += user_guess
            print(f"\nword doesn't contain '{user_guess}'\n")
            lives -= 1
            check_stats(lives, word, empty_list, doesnt_contain, currentscore, highscore)
    else:
        if user_guess == word:
                got_word(word, currentscore, highscore)
        else:
            print(f"\nThe word isn't '{user_guess}'")
            lives -= 1
            check_stats(lives, word, empty_list, doesnt_contain, currentscore, highscore)


def got_word(word, currentscore, highscore):
    print(f"\nCongrats! The word was '{word}\n'")
    currentscore += 1

    if currentscore > highscore:
        highscore = currentscore

    run_game(currentscore, highscore)


def new_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore):
    """
    Runs through functions to get a new guess from the user.
    """
    display_info(lives, word, empty_list, doesnt_contain, currentscore, highscore)
    user_guess = get_input()
    validate_input(user_guess, lives, word, empty_list, doesnt_contain, currentscore, highscore)
    check_guess(user_guess, lives, word, empty_list, doesnt_contain, currentscore, highscore)


def run_game(currentscore, highscore):
    """
    Run functions to set up game
    """
    word = new_word()
    validate_word(word)
    empty_list = create_empty_list(word)
    doesnt_contain = []
    lives = 0
    lives = len(word)
    new_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore)


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
