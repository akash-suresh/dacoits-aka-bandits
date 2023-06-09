import random
from algorithms.BanditAlogrithm import BanditAlgorithm

def ind_max(x):
    m = max(x)
    return x.index(m)

class EpsilonGreedy(BanditAlgorithm):
    def __init__(self, epsilon, counts, values):
        self.epsilon = epsilon
        self.counts = counts
        self.values = values
        return
    
    def initialize(self, n_arms):
        self.counts = [0 for col in range(n_arms)]
        self.values = [0.0 for col in range(n_arms)]
        return
    
    
    def select_arm(self):
        if random.random() > self.epsilon:
            # exploitation
            return ind_max(self.values)
        else:
            # exploration
            return random.randrange(len(self.values))
        
    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] = self.counts[chosen_arm] + 1
        n = self.counts[chosen_arm]
        value = self.values[chosen_arm]
        new_value = ((n - 1) / float(n)) * value + (1 / float(n)) * reward
        self.values[chosen_arm] = new_value
        # print('counts = ' + str(self.counts))
        # print('values = ' + str(self.values))
        return
    

