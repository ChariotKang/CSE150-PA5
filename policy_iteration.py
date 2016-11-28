from MDP import *
import random
import numpy as np
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

def policyEvaluation(pi, mdp):
	matrix = np.zeros((len(mdp.states),len(mdp.states)))
	left = np.zeros((len(mdp.states), 1))
	for i in range(1, len(mdp.states)+1):
		matrix[i-1][i-1] = 1
		#print (matrix)
		for (s2, prob) in mdp.transitionFunction[(i, pi[i])]:
			#print ((s2, prob))
			matrix[i-1][s2-1] = matrix[i-1][s2-1] - mdp.discountFactor*prob
		left[i-1][0] = mdp.rewards[i]
	mati = np.mat(matrix)
	matLeft = np.mat(left)
	result = np.linalg.solve(mati, matLeft)
	arrResult = result.getA()
	U2 = []
	for i in range (len(mdp.states)):
		U2.append(arrResult[i][0])
	return U2
	

def policyIteration(mdp):
	pi = {}
	for i in range(1, len(mdp.states)+1):
		pi[i] = mdp.actions[random.randint(0, 3)]
	U = []
	while True:
		U = policyEvaluation(pi, mdp)
		unchanged = True
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
			PU = 0
			for (s2, prob) in mdp.transitionFunction[(s, pi[s])]:
				PU = PU + prob*U[s2-1]
			if maxPU > PU:
				pi[s] = maxAction
				unchanged = False
		if unchanged == True:
			break
	print (pi)
	return pi
		
	
	
pi = policyIteration(mdp)