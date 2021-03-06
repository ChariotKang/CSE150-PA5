from MDP import *
mdp = MDP()
mdp.discountFactor = 0.99
mdp.actions.append('EAST')
mdp.actions.append('WEST')
mdp.actions.append('SOUTH')
mdp.actions.append('NORTH')
f = open("rewards.txt")
i = 1
for line in f:
	mdp.addState(i)
	mdp.setRewards(i, line[:-1])
	i = i+1
f.close()
#print (mdp.rewards)
f = open("prob_east.txt")
for line in f:
	splitList = line.split()
	mdp.addTransition(splitList[1], splitList[0], 'EAST', splitList[2])
	#mdp.addAction(int(splitList[0]),'E')
f.close()
#print (mdp.transitionFunction)
f = open("prob_west.txt")
for line in f:
	splitList = line.split()
	mdp.addTransition(splitList[1], splitList[0], 'WEST', splitList[2])
	#mdp.addAction(splitList[0],'W')
f.close()

f = open("prob_south.txt")
for line in f:
	splitList = line.split()
	mdp.addTransition(splitList[1], splitList[0], 'SOUTH', splitList[2])
	#mdp.addAction(splitList[0],'S')
f.close()

f = open("prob_north.txt")
for line in f:
	splitList = line.split()
	mdp.addTransition(splitList[1], splitList[0], 'NORTH', splitList[2])
	#mdp.addAction(splitList[0],'N')
f.close()
#print (mdp.transitionFunction)"""
def value_iteration(mdp, e):
	U = []
	U2 = []
	for s in mdp.states:
		U.append(0)
		U2.append(0)
	maxChange = 0
	#timesOfLoop = 0
	while True:
	#for i in range(1, 1000):
		#timesOfLoop = timesOfLoop + 1
		for i in range(0, len(U2)):
			U[i] = U2[i]
		maxChange = 0
		for s in mdp.states:
			listPU = []
			for action in mdp.actions:
				PU = 0
				for (s2, prob) in mdp.transitionFunction[(s, action)]:
					PU = PU + prob*U[s2-1]
				listPU.append(PU)
			U2[s-1] = mdp.rewards[s] + mdp.discountFactor*max(listPU)
			if abs(U2[s-1] - U[s-1]) > maxChange:
				maxChange = abs(U2[s-1] - U[s-1])
				#print (maxChange)
		#print (U2)
		if(maxChange == 0):
			break
	return U
U = value_iteration(mdp,0.1)
pi = {}
for s in mdp.states:
	maxPU = float("-inf")
	maxAction = None
	for action in mdp.actions:
		PU = 0
		for (s2, prob) in mdp.transitionFunction[(s, action)]:
			PU = PU + prob*U[s2-1]
		if PU > maxPU:
			maxPU = PU
			maxAction = action
	pi[s] = maxAction
listOfStateUtilityPolicy = []
for i in range (1, 81):
	if U[i-1] > 0:
		listOfStateUtilityPolicy.append((i, U[i-1], pi[i]))
for element in listOfStateUtilityPolicy:
	print element
