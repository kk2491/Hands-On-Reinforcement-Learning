import gym
import sys
def run_gym_env(argv):
	env = gym.make(argv[1]) # Name of the environment supplied as 1st argument
	env.reset()
	for _ in range(int(argv[2])):
		env.render()
	env.step(env.action_space.sample())
	env.close()

if __name__ == "__main__":
	run_gym_env(sys.argv)
