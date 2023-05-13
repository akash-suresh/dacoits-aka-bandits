import random

class BernoulliArm():
    def __init__(self, p):
        self.p = p
    
    def draw(self):
        if random.random() > self.p:
            return 0.0
        else:
            return 1.0
        

# def test_bernoulli_arm():
#     means = [0.1, 0.1, 0.1, 0.1, 0.9]
#     n_arms = len(means)
#     random.shuffle(means)
#     arms = list(map(lambda mu: BernoulliArm(mu), means))
#     print(arms)
    
#     print(arms[0].draw())
#     print(arms[1].draw())
#     print(arms[2].draw())
#     print(arms[2].draw())
#     print(arms[3].draw())   
#     print(arms[2].draw())
#     print(arms[4].draw())


# test_bernoulli_arm()