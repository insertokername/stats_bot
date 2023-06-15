import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!help':
        return '`? prefix for private response`\n `!help for help`\n '

    return 'I didn\'t understand what you wrote. Try typing "!help".'
