import random
from brain_games.games import play_game


def is_even(number):
    return number % 2 == 0


def get_correct_answer(number):
    return 'yes' if is_even(number) else 'no'


def rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    number = random.randint(1, 100)
    return number, get_correct_answer(number)


def main():
    play_game(generate_question, rules)


if __name__ == '__main__':
    main()
