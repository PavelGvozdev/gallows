import pytest
import main

hidden_word = 'skillfactory'
STANDARD_LETTER_POSITION = 1
LIST_OF_LETTER_POSITION = [1]
letter = 'k'


def test_initialization_of_game_set_mistakes():
    main.initialization_of_game()
    assert main.mistakes == 0


def test_initialization_of_game_set_hidden_word():
    words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
    main.initialization_of_game()
    assert main.hidden_word in words == True


def test_initialization_of_game_set_visible_word():
    main.initialization_of_game()
    for _ in main.visible_word:
        assert _ == '_'


def test_find_letters_have_letter():
    main.hidden_word = 'blackbox'
    assert main.find_letters('c', 1) == 3


def test_find_letters_not_have_letter():
    main.hidden_word = 'blackbox'
    assert main.find_letters('w', 1) == -1


def test_checking_letters_return():
    list_of_letter_position = main.checking_letters(letter)
    assert list_of_letter_position == LIST_OF_LETTER_POSITION
