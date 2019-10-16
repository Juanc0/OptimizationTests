class Dino:
	@staticmethod
	def exe1():
		print("al carajo 1")
	def exe2(self):
		print("al carajo 2")


class Car(Dino):
	wheels = 0
	def __init__(self, color, x, func):
		self.color = color
		self.f = func
		Car.wheels = x

while (True):
	print("yey")

Dino.exe1()
din = Dino()
din.exe2()

f = lambda x: x+1
#print(f(2))


print(Car.wheels)
car = Car("red", 5, f)
print(Car.wheels)
print(car.color)
print(car.f(50))
	