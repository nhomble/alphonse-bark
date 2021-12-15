import random
import os

from groupy.client import Client


def should_bark():
    """
    10% chance of barking
    :return:
    """
    return random.randint(0, 9) == 0


def message():
    """
    bot message
    :return:
    """
    return random.choice([
        "woof",
        "chief",
        "cyber polish"
    ])


if __name__ == '__main__':
    bot_id = os.getenv("GROUPME_BOT")
    api_key = os.getenv("GROUPME_KEY")

    groupme = Client.from_token(api_key)

    if should_bark():
        print("Printing message")
        groupme.bots.post(bot_id, message())
    else:
        print("Skipping execution")
