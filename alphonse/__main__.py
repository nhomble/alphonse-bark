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
        "chief doug",
        "Kyle cannot fail"
    ])

def keep_alive(groupme, group_id, user_id):
    group = groupme.groups.get(group_id)

    if all([m.user_id != user_id for m in group.members]):
        group.memberships.add("never die", user_id=user_id)

if __name__ == '__main__':
    bot_id = os.getenv("GROUPME_BOT")
    api_key = os.getenv("GROUPME_KEY")
    group_id = os.getenv("GROUPME_GROUP_ID")
    user_id = os.getenv("GROUPME_ALIVE")

    if bot_id is None:
        print("Missing GROUPME_BOT")
        sys.exit(1)

    if api_key is None:
        print("Missing GROUPME_KEY")
        sys.exit(1)

    if group_id is None:
        print("Missing GROUPME_GROUP_ID")
        sys.exit(1)

    if user_id is None:
        print("Missing GROUPME_ALIVE")
        sys.exit(1)

    groupme = Client.from_token(api_key)

    if should_bark():
        print("Printing message")
        groupme.bots.post(bot_id, message())
    else:
        print("Skipping execution")

    keep_alive(groupme, group_id, user_id)

