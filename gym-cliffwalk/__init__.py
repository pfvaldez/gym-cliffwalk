from gym.envs.registration import register

register(
    id='cliffwalk-v0',
    entry_point='gym_cliffwalk.envs:CliffWalkEnv',
)