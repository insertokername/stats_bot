import psutil
from gpiozero import CPUTemperature

def update_array(arr,push_val):
	arr.pop(0)
	arr.push(push_val)

class tracker:
	def __init__(self) -> None:
		self.cpu_temps = [0 for i in range(20)]
		self.cpu_usage = [0 for i in range(20)]
		self.mem_usage = [0 for i in range(20)]

	def tick(self) -> None:
		update_array(self.cpu_temps)
		update_array(self.cpu_usage,psutil.cpu_percent())
		update_array(self.mem_usage, psutil.virtual_memory().percent)


print(CPUTemperature())