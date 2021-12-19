import random
import os
import sys

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
        "cyber polish",
        "chief doug"
    ])


if __name__ == '__main__':
    bot_id = os.getenv("GROUPME_BOT")
    api_key = os.getenv("GROUPME_KEY")

    if bot_id is None:
        print("Missing GROUPME_BOT")
        sys.exit(1)

    if api_key is None:
        print("Missing GROUPME_KEY")
        sys.exit(1)

    groupme = Client.from_token(api_key)

    if should_bark():
        print("Printing message")
        groupme.bots.post(bot_id, message())
    else:
        print("Skipping execution")
