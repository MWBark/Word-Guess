from random_word import Wordnik

wordnik_service = Wordnik()

word = wordnik_service.get_random_word()

print(word)