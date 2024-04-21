from random_word import Wordnik

wordnik_service = Wordnik()
doesnt_contain = []
lives = 0
currentscore = 0
highscore = 0


def new_word():
    """
    Gets a new random word.
    """
    global word, lives
    word = wordnik_service.get_random_word().lower()
    lives += len(word)
    print(word)
    return word


def validate_word():
    """
    Checks the random word only contains lowercase english alphabet letters or '-'.
    If not, runs 'run_game' function again.
    """
    for i in [*word]:
        if i not in list(map(chr, range(97, 123))) and i != '-':
            run_game()


def create_empty_list():
    """
    Creates a number of underscores equal to the random word length
    that will be updated with letters the user guesses.
    """
    global empty_list
    empty_list =[]

    for i in [*word]:
        if i == '-':
            empty_list += '-'
        else:
            empty_list += "_"

    return empty_list


def display_info():
    """
    Displays word length, letters the word doesn't contain
    and lives to help user guess
    """
    letters_string = ", ".join(doesnt_contain)
    print(f"\nlives: {lives} currentscore: {currentscore} highscore: {highscore}\n{len(word)} letters, doesn't contain: {letters_string}")
    print(*empty_list)


def get_input():
    """
    Gets user's letter or word guess.
    """
    global user_guess
    user_guess = input("Enter a letter or word: \n")
    return user_guess


def validate_input_length():
    """
    Checks the length of the user's word guess matches that of the random word.
    Prints statement and starts new guess if true.
    """
    if len(user_guess) > 1 and len(user_guess) != len(word):
        print(f"\nIncorrect word length of {len(user_guess)}")
        new_guess()


def validate_input_characters():
    """
    Checks the user's guess only contains lowercase english alphabet characters
    """
    for i in [*user_guess]:
        if i not in list(map(chr, range(97, 123))):
            print(f"\n{user_guess} contains non lowercase english alphabetic characters")
            new_guess()


def check_stats():
    """
    Check the user's stats, such as lives.
    Runs a new game or new guess based on lives value.
    """
    global doesnt_contain, currentscore
    if lives == 0:
        print(f"\nBad luck. the word was {word}")
        doesnt_contain = []
        currentscore = 0
        run_game()
    else:
        new_guess()


def check_guess():
    """
    First checks user's guess is a letter
    then updates the 'empty_list' if it is, 
    then test wether the user's guess or 'empty_string'
    matches the random word.
    """
    global doesnt_contain, lives, currentscore
    if len(user_guess) < 2:       
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
        update_highscore()
        run_game()
    else:
        lives -= 1
        check_stats()


def update_highscore():
    """
    Updates the highscore based on the currentscore.
    """
    global highscore, currentscore
    if currentscore > highscore:
        highscore = currentscore


def new_guess():
    """
    Runs through functions to get a new guess from the user.
    """
    display_info()
    get_input()
    validate_input_length()
    validate_input_characters()
    check_guess()


def run_game():
    """
    Run functions to set up game
    """
    new_word()
    validate_word()
    create_empty_list()
    new_guess()


run_game()