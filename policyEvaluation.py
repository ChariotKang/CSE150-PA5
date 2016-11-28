from MDP import *
import numpy as np
mdp = MDP()
mdp.addState(0)
mdp.addState(1)
mdp.setRewards(0, -2)
mdp.setRewards(1, 4)
mdp.discountFactor = 2.0/3.0
mdp.action = [0, 1]
mdp.addTransition(0, 0, 0, 3.0/4.0)
mdp.addTransition(1, 0, 0, 1.0/4.0)
mdp.addTransition(0, 1, 0, 1.0/4.0)
mdp.addTransition(1, 1, 0, 3.0/4.0)
mdp.addTransition(0, 0, 1, 0.5)
mdp.addTransition(1, 0, 1, 0.5)
mdp.addTransition(0, 1, 1, 0.5)
mdp.addTransition(1, 1, 1, 0.5)
pi = {}
pi[0] = 0
pi[1] = 0
U = []
for s in mdp.states:
	U.append(0)
	
	
	
"""def policyEvaluation(pi, U, mdp):
	matrix = np.zeros((len(mdp.states),len(mdp.states)+1))
	for i in range(0, len(mdp.states)):
		matrix[i][i] = 1
		#print (matrix)
		for (s2, prob) in mdp.transitionFunction[(i, pi[i])]:
			#print ((s2, prob))
			matrix[i][s2] = matrix[i][s2] - mdp.discountFactor*prob
		matrix[i][len(mdp.states)] = mdp.rewards[i]
	subMatrix = np.zeros((len(mdp.states),len(mdp.states)))
	for i in range(0, len(mdp.states) ):
		for j in range(0, len(mdp.states)):
			subMatrix[i][j] = matrix[i][j]
	mati = np.mat(matrix)
	print (subMatrix)
	subMatI = np.mat(subMatrix).I
	result = np.dot(subMatI, mati)"""
	#print (result)
	
def policyEvaluation(pi, U, mdp):
	matrix = np.zeros((len(mdp.states),len(mdp.states)))
	left = np.zeros((len(mdp.states), 1))
	for i in range(0, len(mdp.states)):
		matrix[i][i] = 1
		#print (matrix)
		for (s2, prob) in mdp.transitionFunction[(i, pi[i])]:
			#print ((s2, prob))
			matrix[i][s2] = matrix[i][s2] - mdp.discountFactor*prob
		left[i][0] = mdp.rewards[i]
	mati = np.mat(matrix)
	matLeft = np.mat(left)
	result = np.linalg.solve(mati, matLeft)
	arrResult = result.getA()
	U2 = []
	for i in range (len(mdp.states)):
		U2.append(arrResult[i][0])
	return U2
	
policyEvaluation(pi, U, mdp)