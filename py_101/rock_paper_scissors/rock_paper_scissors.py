import json
import random

with open("rock_paper_scissors_messages.json", "r") as file:
    MESSAGES = json.load(file)

LANGUAGE = "en"
VALID_CHOICES = MESSAGES[LANGUAGE]["valid_choices"]
ROCK = VALID_CHOICES[0]
PAPER = VALID_CHOICES[1]
SCISSORS = VALID_CHOICES[2]
VALID_ANSWERS = MESSAGES[LANGUAGE]["valid_answers"]
NO = VALID_ANSWERS[1]


def prompt(text):
    print(f"=> {text}")


def json_string(message_key, lang="en"):
    return MESSAGES[lang][message_key]


def displayWinner(user_choice, computer_choice):
    if (
        (user_choice == ROCK and computer_choice == SCISSORS)
        or (user_choice == PAPER and computer_choice == ROCK)
        or (user_choice == SCISSORS and computer_choice == PAPER)
    ):
        prompt(json_string("user_win", LANGUAGE))
    elif (
        (user_choice == ROCK and computer_choice == PAPER)
        or (user_choice == PAPER and computer_choice == SCISSORS)
        or (user_choice == SCISSORS and computer_choice == ROCK)
    ):
        prompt(json_string("computer_win", LANGUAGE))
    else:
        prompt(json_string("tie", LANGUAGE))


prompt(json_string("welcome", LANGUAGE))

while True:
    prompt(json_string("move_selection", LANGUAGE))

    user_choice = input().lower()
    while user_choice not in VALID_CHOICES:
        prompt(json_string("invalid_move", LANGUAGE))
        user_choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f"You selected {user_choice}, computer chose {computer_choice}.")

    displayWinner(user_choice, computer_choice)

    prompt(json_string("play_again", LANGUAGE))
    answer = input().lower()
    while answer not in VALID_ANSWERS:
        prompt(json_string("invalid_answer", LANGUAGE))
        answer = input().lower()

    if answer == NO:
        break
