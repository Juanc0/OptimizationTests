from multiprocessing.pool import ThreadPool
from HC import HC

class PHC:
	def __init__(self, x, f, stop, step, threads):
		self.f = f
		self.HC = HC(x, f, stop, step)
		self.pool = ThreadPool(processes = threads)
		self.threads = threads
		
	def exe(self):
		#exes = [self.pool.apply_async(self.HC.exe(), args=()) for i in range(self.threads)]
		exes = [self.HC.exe() for i in range(self.threads)]
		#minimizers = [ret.get() for ret in exes]
		#return PHC.minimizer(minimizers, self.f)
		return PHC.minimizer(exes, self.f)

	@staticmethod
	def minimizer(minimizers, f):
		minimizer = minimizers[0]
		minimum = f(minimizer)
		for mini in minimizers:
			new = f(mini)
			if new < minimum:
				minimizer = mini
		return minimizer