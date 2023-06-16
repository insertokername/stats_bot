import psutil
import gpiozero 
#import print_graph
#import time

def update_array(arr,push_val):
	arr.pop(0)
	arr.append(push_val)


class makeTracker:
	def __init__(self,track_length: int) -> None:
		self.temps={}
		self.track_len=track_length
		self.graph_heigth=20

		#self.cpu_temps = [0 for i in range(20)]
		#self.cpu_usage = [0 for i in range(20)]
		#self.mem_usage = [0 for i in range(20)]

	def set_track_len(self,new_len:int):
		self.track_len=new_len

	def set_graph_heigth(self,new_heigth:int):
		self.graph_heigth=new_heigth

	def tick(self) -> None:
		temperatures = psutil.sensors_temperatures()
		for name, entries in temperatures.items():
			for entry in entries:
				if not self.temps.get(entry.label):
					self.temps[entry.label]=[0 for i in range(self.track_len)]
				update_array(self.temps[entry.label],entry.current)
				#print(f" - {entry.label}: {entry.current}\n")
		#update_array(self.cpu_temps)
		#update_array(self.cpu_usage,psutil.cpu_percent())
		#update_array(self.mem_usage, psutil.virtual_memory().percent)


#def get_temperatures():
#	temperatures = psutil.sensors_temperatures()
#	for name, entries in temperatures.items():
#		print(f"Sensor: {name}")
#		for entry in entries:
#			print(f"  - {entry.label}: {entry.current}°C")

#get_temperatures()

#print(track.temps)

#print(print_graph.make_graph(track.temps['Tctl'], 50,3))

#print(CPUTemperature())