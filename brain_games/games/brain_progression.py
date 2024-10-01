import random
from brain_games.games import play_game


def generate_progression():
    first_number = random.randint(1, 30)
    step_of_progression = random.randint(1, 20)
    correct_progression = [
        first_number + step_of_progression * i for i in range(10)
    ]

    return correct_progression


def hide_element(progression):
    hide_element = random.choice(progression)
    index_of_hide_element = progression.index(hide_element)
    progression[index_of_hide_element] = '..'

    return progression, hide_element


def generate_question():
    progression = generate_progression()
    progression_with_hidden, correct_answer = hide_element(progression)
    question = ' '.join(map(str, progression_with_hidden))

    return question, correct_answer


def rules():
    return 'What number is missing in the progression?'


def main():
    play_game(generate_question, rules)


if __name__ == '__main__':
    main()
