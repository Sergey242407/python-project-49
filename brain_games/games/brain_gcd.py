import random
from brain_games.games import play_game


def generate_question():
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)

    question = f"{num1} {num2}"

    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    correct_answer = num1 + num2

    return question, correct_answer


def rules():
    return 'Find the greatest common divisor of given numbers.'


def main():
    play_game(generate_question, rules)


if __name__ == '__main__':
    main()
