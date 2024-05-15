from gymnasium.envs.registration import register

register(
    id='Pygame-v0',
    entry_point='gym_env.envs:CustomEnv',
    max_episode_steps=2000,
)
