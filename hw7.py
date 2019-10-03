#hw 7 completed Spring 2019
import time
import random
import matplotlib.pyplot as plt
class hw:
	def __init__(self):
		self.times = []
		self.size = []
		for i in range(0,1000):
			x = random.randint()
			smple = random.sample(x)
			start_time = time.time()
			smple.sort()
			stop_time = time.time()
			time_total = stop_time - start_time
			self.size.append(len(smple))
			self.time.append(time_total)
	def graphOutput(self):		
		plt.plot(self.times, self.size)
		plt.show()

HPlotter = hw()
HPlotter.graphOutput()

