from SinglePoint import SinglePoint

class HC(SinglePoint):
	def __init__(self, x, f, stop, step):
		#super().__init__(x, f, HillClimb.hcchildren, HillClimb.hcreplace, stop)
		super().__init__(x, f, self.hcchildren, self.hcreplace, stop)
		self.step = step

	#@staticmethod
	def hcchildren(self, iter, X, f):
		return [x + self.step() for x  in X]

	#@staticmethod
	def hcreplace(self, iter, x, y, f):
		if f(y) <= f(x):
			return y
		return x