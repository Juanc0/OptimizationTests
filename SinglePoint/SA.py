from SinglePoint import SinglePoint
from random import random

class SA(SinglePoint):

	def __init__(self,x, f, stop, step, temp):
		#super().__init__(x, f, SimulatedAnnealing.sachildren, SimulatedAnnealing.hcreplace, stop, step)
		super().__init__(x, f, self.sachildren, self.sareplace, stop)
		self.step = step
		self.temp = temp

	#@staticmethod
	def sachildren(self, iter, X, f):
		return [x + self.step() for x  in X]
	
	#@staticmethod
	def sareplace(self, iter, x, y, f):
		new = f(y)
		old = f(x)
		if new <= old or random() <= self.temp(iter, old, new):
			return y
		return x