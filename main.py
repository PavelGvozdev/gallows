import random

WORDS = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
mistakes = 0
hidden_word = ''
visible_word = []


def initialization_of_game():
    global visible_word
    global hidden_word
    hidden_word = random.choice(WORDS)
    global mistakes
    mistakes = 0
    counter = 0

    print('Привет! Меня зовут Бендер и я загадал слово. Попробуй отгадать его по буквам. Если ошибешься четыре '
          'раза, ты проиграл.')

    while counter < len(hidden_word):
        visible_word.append('_')
        counter += 1

    temp_string = ''.join(visible_word)
    print('Загаданное слово: ' + temp_string)
    guessing_the_word()


def guessing_the_word():
    while True:
        letter = input('Напечатай букву и нажми Enter: ')
        list_of_letter_position = checking_letters(letter)
        counter = 0

        while counter < len(list_of_letter_position):
            index = list_of_letter_position[counter]
            visible_word[index] = letter
            counter += 1

        temp_string = ''.join(visible_word)
        print(''.join(temp_string))
        end_guessing = temp_string.find('_')

        if end_guessing == (-1):
            to_win()
            break


def checking_letters(letter):
    # global hidden_word
    list_of_letter_position = []
    start_position = 0

    while True:
        letter_position = find_letters(letter, start_position)
        if letter_position == (-1):
            break
        else:
            list_of_letter_position.append(letter_position)
            start_position = letter_position + 1

    if len(list_of_letter_position) == 0:
        global mistakes
        mistakes += 1
        if mistakes == 4:
            to_lose()
        else:
            print('Такой буквы нет. Попробуй еще раз')
            print('Ты допустил {} ошибок'.format(mistakes))
            guessing_the_word()
    else:
        return list_of_letter_position


def find_letters(letter, start_position):
    global hidden_word
    temp = hidden_word.find(letter, start_position)
    return temp


def to_win():
    print('Ты правильно отгадал слово:')
    print(''.join(visible_word))


def to_lose():
    print('Ты ошибся четыре раза и проиграл.')


# If you in PyCharm, press the green button in the gutter to run the script.
if __name__ == '__main__':
    initialization_of_game()
