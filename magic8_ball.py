# !/usr/bin/env python
"""project: Magic 8 Ball Game, created:7/29/2021, author:seraph★776, email:seraph776@gmail.com"""
import sys
from random import randint
from colors import magick8BallColors


def Intro():
    print('''\
Welcome to Magic 8-Ball.    
Ask me a question, and I'll tell your fortune!
But first, tell me your name...\n''')


def get_name():
    """This functions asks for, and returns users name."""
    name = input('Enter your name:\n>>>  ')
    return name


def get_response(question: str) -> str:
    """This function returns the eightBall's response.
    :param:
        question (str): The user's questions

    :returns:
       str: the eightBallResponse

    :note:
        The Magic 8-Ball has 20 possible answers:
        - 10 affirmative answers in range(11) which will display in green,
        - 5 non-committal answers in range(11, 15) which will display in yellow and,
        - 5 negative answers in range(15, 20) which will display in red.
    """

    all_possible_responses = {
        0: "It is Certain",
        1: "It is decidedly so",
        2: "Without a doubt",
        3: "Yes definitely",
        4: "You may rely on it",
        5: "As I see it, yes",
        6: "Most likely",
        7: "Outlook good",
        8: "Yes",
        9: "Signs point to yes",
        10: "Reply hazy, try again",
        11: "Ask again later",
        12: "Better not tell you now",
        13: "Cannot predict now",
        14: "Concentrate and ask again",
        15: "Don't count on it",
        16: "My reply is no",
        17: "My sources say no",
        18: "Outlook not so good",
        19: "Very doubtful"
    }

    # Generate a random dictionary key.
    # This key will generate the response and determine the color range of the response.
    color_key: int = randint(0, 19)

    # Get eightBall's response from dictionary.
    eightBallResponse: str = all_possible_responses.get(color_key)

    # Determine appropriate color for response and then display results.
    eightBallResponse = get_color(color_key, eightBallResponse)
    return eightBallResponse


def get_color(color_key: int, eightBallResponse: str) -> str:
    """This function determines the color for eightBall's response."""
    ColoredResponse = ''
    if color_key in range(11):  # 10 affirmative answers in green.
        ColoredResponse = magick8BallColors.green(f'"{eightBallResponse}."')
    elif color_key in range(11, 15):  # 5 non-committal answers in yellow.
        ColoredResponse = magick8BallColors.yellow(f'"{eightBallResponse}."')
    elif color_key in range(15, 20):  # 5 negative answers in red.
        ColoredResponse = magick8BallColors.red(f'"{eightBallResponse}."')
    return ColoredResponse


def get_fortune():
    """This function gets username, then returns an answers to a user's question."""
    Intro()
    name = get_name()
    while question := input('Ask a question or enter \'q\' to quit:\n>>> '):
        if question == 'q':
            print('Good-bye!')
            sys.exit()
        else:
            response = get_response(question)
            print(f'{name.title()} asks: {question}')
            print(f'Magic 8-Ball\'s answer: {response}\n')

