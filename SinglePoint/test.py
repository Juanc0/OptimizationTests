import math
from random import random
from HC import HC
from PHC import PHC
from SA import SA

#	init

executions = 100
iterations = 1e+5
theads = 50

a = -50
b = 50
dim = 10
f = lambda X: 10*len(X) + sum([x**2 - 10*math.cos(2*math.pi*x) for x in X])

HCstop = lambda iter, x, f: iter >= iterations
PHCstop = lambda iter, x, f: iter >= iterations/theads
SAstop = HCstop

step = lambda : random() - 0.5

temp = lambda iter, old, new : math.e**(-iter/2e+4)


hcexes  = []
phcexes = []
saexes  = []

hcres  = []
phcres = []
sares  = []

hcx = []
phcx = []
sax = []

hcmin = math.inf
phcmin = math.inf
samin = math.inf
hcminidx = 0
phcminidx = 0
saminidx = 0

#	Calcs
for i in range(executions):
	#	same start point to all
	x = [random()*(b-a)+a for i in range(dim)]

	hc  = HC(x, f, HCstop, step)
	phc = PHC(x, f, PHCstop, step, theads)
	sa  = SA(x, f, SAstop, step, temp)

	#	compute

	hcexes.append(hc.exe())
	phcexes.append(phc.exe())
	saexes.append(sa.exe())

	hcres.append(f(hcexes[-1]))
	phcres.append(f(phcexes[-1]))
	sares.append(f(saexes[-1]))

	#	each min and it point

	if hcres[-1] < hcmin:
		hcmin = hcres[-1]
		hcx = hcexes[-1]
	if phcres[-1] < phcmin:
		phcmin = phcres[-1]
		phcx = phcexes[-1]
	if sares[-1] < samin:
		samin = sares[-1]
		sax = saexes[-1]

	#	Progress

	if not i%10:
		print(i)
print()

#	stats

hcavg = sum(hcres)/executions
hcres.sort()
hcmed = hcres[int(executions/2)]

phcavg = sum(phcres)/executions
phcres.sort()
phcmed = phcres[int(executions/2)]

saavg = sum(sares)/executions
sares.sort()
samed = sares[int(executions/2)]

#	Print

file = open('_results exp.txt', 'w+')
file.write('Hill Climb:\n')
file.write('Average\t\t\t\t\t\t\t\tMedian\t\t\t\t\t\t\t\tMax\t\t\t\t\tMin\n')
file.write('{:0.4f} ± {:0.4f}\t{:0.4f} ± {:0.4f}\t{:0.4f}\t{:0.4f}\n'.format(
  hcavg,
	math.sqrt(sum([(r - hcavg)**2 for r in hcres])/(executions-1)),
  hcres[int(executions/2)],
	math.sqrt(sum([(r - hcmed)**2 for r in hcres])/(executions-1)),
  hcres[-1],
	hcres[0]
))
file.write('Minimizer:\n' + str(['{:0.6f}'.format(i) for i in hcx]) + '\n\n')

file.write('Parallel Hill Climb:\n')
file.write('Average\t\t\t\t\t\t\t\tMedian\t\t\t\t\t\t\t\tMax\t\t\t\t\tMin\n')
file.write('{:0.4f} ± {:0.4f}\t{:0.4f} ± {:0.4f}\t{:0.4f}\t{:0.4f}\n'.format(
  phcavg,
	math.sqrt(sum([(r - phcavg)**2 for r in phcres])/(executions-1)),
  phcres[int(executions/2)],
	math.sqrt(sum([(r - phcmed)**2 for r in phcres])/(executions-1)),
  phcres[-1],
	phcres[0]
))
file.write('Minimizer:\n' + str(['{:0.6f}'.format(i) for i in phcx]) + '\n\n')

file.write('Simulated Annealling:\n')
file.write('Average\t\t\t\t\t\t\t\tMedian\t\t\t\t\t\t\t\tMax\t\t\t\t\tMin\n')
file.write('{:0.4f} ± {:0.4f}\t{:0.4f} ± {:0.4f}\t{:0.4f}\t{:0.4f}\n'.format(
  saavg,
	math.sqrt(sum([(r - saavg)**2 for r in sares])/(executions-1)),
  sares[int(executions/2)], 
	math.sqrt(sum([(r - samed)**2 for r in sares])/(executions-1)),
  sares[-1],
	sares[0]
))
file.write('Minimizer:\n' + str(['{:0.6f}'.format(i) for i in sax]) + '\n\n')
