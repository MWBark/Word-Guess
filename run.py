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
    else:
        return True


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
                break

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
        user_guess = input("Enter a word or letter:\n").lower()

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
                print("Please use english alphabet characters\n")
                break

    return user_guess


def run_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore, guessed_words):
    """
    Runs a guessing loop while 'new_guess' = True.
    If the user gets the word, 'new_guess' = False and 'got_word = True' is returned.
    If lives = 0, 'new_guess' = False and 'got_word = False' is returned.
    """
    new_guess = True

    while new_guess is True:
        display_info(lives, word, empty_list, doesnt_contain, currentscore, highscore)
        user_guess = get_input(word, empty_list, doesnt_contain, guessed_words)

        # Letter guess
        if len(user_guess) < 2:
            # Correct letter guess
            if user_guess in [*word]:
                for i in range(len([*word])):
                    if [*word][i] == user_guess:
                        empty_list[i] = user_guess

                if empty_list == [*word]:
                    got_word = True
                    new_guess = False
                else:
                    print(f"\n'{user_guess}' is in word\n")
            # Incorrect letter guess
            else:
                doesnt_contain += user_guess
                print(f"\nword doesn't contain '{user_guess}'\n")
                lives -= 1
                if lives == 0:
                    got_word = False
                    new_guess = False
        # Word guess
        else:
            # Correct word guess
            if user_guess == word:
                got_word = True
                new_guess = False
            # Incorrect word guess
            else:
                print(f"\nThe word isn't '{user_guess}'")
                guessed_words.append(user_guess)
                lives -= 1
                if lives == 0:
                    got_word = False
                    new_guess = False

    return got_word


def update_highscore(currentscore, highscore):
    """
    Makes highscore = currentscore if the currentscore is
    greater than the highscore.
    """
    if currentscore > highscore:
        highscore = currentscore

    return highscore


def run_game(currentscore, highscore):
    """
    Run functions to set up game
    """
    api_up = check_api()
    if api_up is True:
        # Reset Game
        word = new_word()
        empty_list = create_empty_list(word)
        doesnt_contain = []
        guessed_words = []
        lives = 0
        lives = len(word)
        # Get user input
        got_word = run_guess(lives, word, empty_list, doesnt_contain, currentscore, highscore, guessed_words)
        if got_word is True:
            print(f"\nWell done. The word was '{word}'\n")
            currentscore += 1
            highscore = update_highscore(currentscore, highscore)
        else:
            print(f"\nBad luck. The word was '{word}'\n")
            currentscore = 0

        while True:
            answer = input("Continue playing? Enter 'yes' or 'no'.\n").lower()
            if answer == 'yes':
                run_game(currentscore, highscore)
            elif answer == 'no':
                print("\nThanks for playing Word Guess!\n")
                break
            else:
                print(f"\nYou entered '{answer}'. Please only enter 'yes' or 'no'.\n")


print("""
WELCOME TO WORD GUESS!

Guess the random words generated from Wordnik. Enter letters to fill in the
blank letter spaces or guess the whole word. Incorrect letter guesses and word
guesses cost life points. Life points equal to the length of the random word
are added for each new word. Guess the word before your life points reach 0.
Successful guesses score a point.

Please visit Wordnik.com and enter any words that come up to find out more
about them.

Let's Play!
""")

run_game(currentscore, highscore)
