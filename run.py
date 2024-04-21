from random_word import Wordnik

wordnik_service = Wordnik()
doesnt_contain = []
lives = 0


def new_word():
    """
    Gets a new random word.
    """
    global word, lives
    word = wordnik_service.get_random_word().lower()
    lives += len(word)
    print(word)
    return word

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
    print(f"\nlives: {lives}\n{len(word)} letters, doesn't contain: {letters_string}")
    print(*empty_list)


def get_input():
    """
    Gets user's letter or word guess.
    """
    global user_guess
    user_guess = input("Enter a letter or word: \n")
    return user_guess


def check_stats():
    """
    Check the user's stats, such as lives.
    Runs a new game or new guess based on lives value.
    """
    global doesnt_contain
    if lives == 0:
        print(f"\nBad luck. the word was {word}")
        doesnt_contain = []
        run_game()
    else:
        display_info()
        get_input()
        check_guess()


def check_guess():
    """
    First checks user's guess is a letter
    then updates the 'empty_list' if it is, 
    then test wether the user's guess or 'empty_string'
    matches the random word.
    """
    global doesnt_contain, lives
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
        run_game()
    else:
        lives -= 1
        check_stats()


def run_game():
    """
    Run functions to set up game
    """
    new_word()
    create_empty_list()
    display_info()
    get_input()
    check_guess()

run_game()