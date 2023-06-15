import random

import print_graph


def get_response(message: str) -> str:
	message=message.lower().split(": ")
	command = message[0]

	if command == '!help':
		return '`usage - usage graph`'

	if command == 'usage':
		return print_graph.make_graph(values=[10,20,30,40,50],heigth=20,col_width=3)
			

	return 'I didn\'t understand what you wrote. Try typing "!help".'
