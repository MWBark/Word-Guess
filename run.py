from random_word import Wordnik

wordnik_service = Wordnik()

word = wordnik_service.get_random_word()

print(word)

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

    print(f"{len(word)} letters")
    print(*empty_list)
    return empty_list


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
    global doesnt_contain, lives, currentscore
    if len(user_guess) < 2:       
        if user_guess not in [*word]:
            doesnt_contain += user_guess
        else:
            for i in range(len([*word])):
                if [*word][i] == user_guess:
                    empty_list[i] = user_guess
        

    if empty_list == [*word] or user_guess == word:
        print(f"Congrats! The word was {word}")
    else:
        print(*empty_list)
        get_input()
        check_guess()



create_empty_list()
get_input()
check_guess()