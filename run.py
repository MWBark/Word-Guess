from random_word import Wordnik

wordnik_service = Wordnik()

word = wordnik_service.get_random_word()

print(word)

def create_empty_list():
    """
    Creates a number of underscores equal to the random word length
    that will be updated with letters the user guesses
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

create_empty_list()