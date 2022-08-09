import numpy as np
from robosuite.environments.manipulation.stack import Stack

if __name__ == '__main__':
    env = Stack(robots=['Panda'],
                has_renderer=False,
                has_offscreen_renderer=True,
                render_camera='agentview',
                use_camera_obs=True,
                render_gpu_device_id=0)

    obs = env.reset()

    for key, value in obs.items():
        print(key, np.array(value).shape)
        # print(value)
    '''

    for i in range(100):
        low, high = env.action_spec
        action = np.random.uniform(low=low, high=high)
        env.step(action)
    '''