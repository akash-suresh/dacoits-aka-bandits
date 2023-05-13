import random
from BernoulliArm import BernoulliArm
from algorithms.EpsilonGreedy import EpsilonGreedy, ind_max

# algo = Bandit Algorithm Object
# arms = List[Bernoulli Arm Objects]
# num_sims = # of simulations
# horizon = # of trials for each simulation

def test_algorithm(algo, arms, num_sims, horizon):
    # contains list of what arms were chosen in every trial
    chosen_arms = [0.0 for i in range(num_sims * horizon)]
    # contains list of reward for every trial
    rewards = [0.0 for i in range(num_sims * horizon)]
    # ?
    cumulative_rewards = [0.0 for i in range(num_sims * horizon)]
    # ?
    sim_nums = [0.0 for i in range(num_sims * horizon)]
    # ?
    times = [0.0 for i in range(num_sims * horizon)]

    for sim in range(num_sims):
        # why is this needed?
        sim = sim + 1 
        # initializes Bandit algorithm
        algo.initialize(len(arms))
        # start running each simulation
        for t in range(horizon):
            # again this is not needed?
            t = t + 1
            index = (sim - 1) * horizon + t - 1
            sim_nums[index] = sim
            times[index] = t
            chosen_arm = algo.select_arm()
            chosen_arms[index] = chosen_arm
            reward = arms[chosen_arms[index]].draw()
            rewards[index] = reward
            if t == 1:
                cumulative_rewards[index] = reward
            else:
                cumulative_rewards[index] = cumulative_rewards[index - 1] + reward
            algo.update(chosen_arm, reward)
    return [sim_nums, times, chosen_arms, rewards, cumulative_rewards]



def test():

    random.seed(1)
    means = [0.1, 0.1, 0.1, 0.1, 0.9]
    n_arms = len(means)
    random.shuffle(means)
    arms = list(map(lambda mu: BernoulliArm(mu), means))

    print("Best arm is " + str(ind_max(means)))
    f = open("standard_results.tsv", "w")
    for epsilon in [0.1, 0.2, 0.3, 0.4, 0.5]:
        algo = EpsilonGreedy(epsilon, [], [])
        algo.initialize(n_arms)
        results = test_algorithm(algo, arms, 5000, 250)
        for i in range(len(results[0])):
            f.write(str(epsilon) + "\t")
            f.write("\t".join([str(results[j][i]) for j in range(len(results))]) + "\n")
    f.close()

test()