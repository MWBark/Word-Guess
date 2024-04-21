from random_word import Wordnik

wordnik_service = Wordnik()

def new_word():
    """
    Gets a new random word.
    """
    global word
    word = wordnik_service.get_random_word().lower()
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
    Displays information like word length to help user guess
    """
    print(f"\n{len(word)} letters")
    print(*empty_list)


def get_input():
    """
    Gets user's letter or word guess.
    """
    global user_guess
    user_guess = input("Enter a letter or word: \n")
    return user_guess


def check_guess():
    """
    First checks user's guess is a letter
    then updates the 'empty_list' if it is, 
    then test wether the user's guess or 'empty_string'
    matches the random word.
    """
    if len(user_guess) < 2:       
        for i in range(len([*word])):
            if [*word][i] == user_guess:
                empty_list[i] = user_guess
        

    if empty_list == [*word] or user_guess == word:
        print(f"Congrats! The word was {word}")
        run_game()
    else:
        display_info()
        get_input()
        check_guess()


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