
from abc import abstractmethod#, ABCMeta

class General:
	def __init__(self, initPopulationSize):
		self.initPopulationSize = initPopulationSize
	
	@abstractmethod
	def initPopulation(self, initPopulationSize):
		print("Initalization Pupulation function")
	
	@abstractmethod
	def stop(self):
		print("Stop condition function")

	@abstractmethod
	def vary(self):
		print("Vary condition function")

	@abstractmethod
	def best(self, population):
		print("Best condition function")

	def exe(self):
		t = 0
		population = self.initPopulation(self.initPopulationSize)
		while not self.stop():
			population = self.vary()
			t = t + 1
		return self.best(population)
