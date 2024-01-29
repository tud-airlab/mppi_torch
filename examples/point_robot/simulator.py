from urdfenvs.robots.generic_urdf import GenericUrdfReacher
from urdfenvs.urdf_common.urdf_env import UrdfEnv
from mpscenes.goals.static_sub_goal import StaticSubGoal
import gymnasium as gym
import torch


class Simulator:
    def __init__(self, cfg, dt, goal, device) -> None:
        self._device = device
        self._goal = goal
        self._dt = dt
        self._environment = self._initalize_environment(cfg)

    def _initalize_environment(self, cfg) -> UrdfEnv:
        """
        Initializes the simulation environment.

        Adds an obstacle and goal visualizaion to the environment and
        steps the simulation once.

        Params
        ----------
        render
            Boolean toggle to set rendering on (True) or off (False).
        """
        robots = [
            GenericUrdfReacher(urdf=cfg["urdf"], mode=cfg["mode"]),
        ]
        env: UrdfEnv = gym.make("urdf-env-v0", dt=self._dt, robots=robots, render=cfg['render'])
        # Set the initial position and velocity of the point mass.
        env.reset()
        goal_dict = {
            "weight": 1.0,
            "is_primary_goal": True,
            "indices": [0, 1],
            "parent_link": 0,
            "child_link": 1,
            "desired_position": self._goal,
            "epsilon": 0.05,
            "type": "staticSubGoal",
        }
        goal = StaticSubGoal(name="simpleGoal", content_dict=goal_dict)
        env.add_goal(goal)
        return env

    def step(self, action: torch.Tensor) -> torch.Tensor:
        observation_dict, _, terminated, _, info = self._environment.step(action)
        observation_tensor = torch.tensor(
            [
                [*observation_dict["robot_0"]["joint_state"]["position"],
                *observation_dict["robot_0"]["joint_state"]["velocity"]]
            ],
            device=self._device,
        )
        return observation_tensor