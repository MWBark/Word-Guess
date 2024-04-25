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
            run_game()


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


def display_info(doesnt_contain, lives, currentscore, highscore, word, empty_list):
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


def validate_input_length(user_guess, lives, word, empty_list, doesnt_contain, currentscore, highscore):
    """
    Checks the length of the user's word guess matches that of the random word.
    Prints statement and starts new guess if true.
    """
    if len(user_guess) > 1 and len(user_guess) != len(word):
        print(f"\nIncorrect word length of {len(user_guess)}")
        new_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore)


def validate_input_characters(user_guess, lives, word, empty_list, doesnt_contain, currentscore, highscore):
    """
    Checks the user's guess only contains lowercase english alphabet characters
    """
    for i in [*user_guess]:
        if i not in list(map(chr, range(97, 123))):
            print(f"\n{user_guess} contains invalid characters")
            print("Please use lowercase english alphabet characters")
            new_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore)


def check_stats(lives, word, empty_list, doesnt_contain, currentscore, highscore):
    """
    Check the user's stats, such as lives.
    Runs a new game or new guess based on lives value.
    """
    if lives == 0:
        print(f"\nBad luck. the word was {word}")
        doesnt_contain = []
        currentscore = 0
        run_game()
    else:
        new_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore)


def check_guess(user_guess, lives, word, empty_list, doesnt_contain, currentscore, highscore):
    """
    First checks user's guess is a letter
    then updates the 'empty_list' if it is,
    then test wether the user's guess or 'empty_string'
    matches the random word.
    """
    if len(user_guess) < 2:
        if user_guess not in [*word]:
            doesnt_contain += user_guess
        else:
            for i in range(len([*word])):
                if [*word][i] == user_guess:
                    empty_list[i] = user_guess

    if empty_list == [*word] or user_guess == word:
        print(f"\nCongrats! The word was {word}")
        doesnt_contain = []
        currentscore += 1
        highscore = update_highscore(currentscore, highscore)
        run_game(currentscore, highscore)
    else:
        lives -= 1
        check_stats(lives, word, empty_list, doesnt_contain, currentscore, highscore)


def update_highscore(currentscore, highscore):
    """
    Updates the highscore based on the currentscore.
    """
    if currentscore > highscore:
        highscore = currentscore
    return highscore


def new_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore):
    """
    Runs through functions to get a new guess from the user.
    """
    display_info(lives, word, empty_list, doesnt_contain, currentscore, highscore)
    get_input()
    user_guess = get_input()
    validate_input_length(user_guess, lives, word, empty_list, doesnt_contain, currentscore, highscore)
    validate_input_characters(user_guess, lives, word, empty_list, doesnt_contain, currentscore, highscore)
    check_guess(user_guess, lives, word, empty_list, doesnt_contain, currentscore, highscore)


def run_game(currentscore, highscore):
    """
    Run functions to set up game
    """
    word = new_word()
    validate_word(word)
    doesnt_contain = []
    lives = 0
    lives = len(word)
    empty_list = create_empty_list(word)
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
