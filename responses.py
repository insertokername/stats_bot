import random
import psutil
import print_graph



def get_response(message: str, tracker) -> str:
	message=message.split(": ")
	command = message[0]

	#print(command)

	if command == 'help':
		return '`temp` - temp graph eg: temp: Composite \n`devices` - shows devices:\n`set_len` - cpu temp tracking history length\n`show_all` - show all temps\n`set_heigth` - set_heigth of graph'
	
	if command == "set_len":
		len=int(message[1])
		tracker.set_track_len(len)
		return f"changed to {len}"
	
	if command == "set_heigth":
		heigth=int(message[1])
		tracker.graph_heigth=heigth
		return "changed heigth"

	if command == "show_all":
		out=""
		temperatures = psutil.sensors_temperatures()
		for name, entries in temperatures.items():
			out+=(f"Sensor: {name}\n")
			for entry in entries:
				out+=(f"  - {entry.label}: {entry.current}°C\n")
		return out

	if command=="devices":
		out=""
		temperatures = psutil.sensors_temperatures()
		for name, entries in temperatures.items():
			for entry in entries:
				out+=entry.label+"\n"

		return out      

	if command == 'temp':
		#print(message[1])
		#print(tracker.temps)
		try:
			return print_graph.make_graph(values=tracker.temps.get(message[1]),heigth=tracker.graph_heigth,col_width=3)
		except Exception as ex:
			return ex

	return 'I didn\'t understand what you wrote. Try typing "help".'
