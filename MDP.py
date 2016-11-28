#!/usr/bin/env python
from collections import defaultdict
class MDP(object):
	states = None
	actions = None
	rewards = None
	discountFactor = None
	transitionFunction = None
	
	def __init__(self):
		self.states = []
		self.actions = []
		self.rewards = {}
		self.transitionFunction = defaultdict(list)
	
	def addState(self, state):
		self.states.append(int(state));
		
	def setRewards(self, state, reward):
		self.rewards[int(state)] = float(reward)
	
	#def addAction(self, s, action):
	#	self.actions[s].append(action)
		
	def addTransition(self, s2, s, action, prob):
		self.transitionFunction[(int(s), action)].append((int(s2), float(prob)));