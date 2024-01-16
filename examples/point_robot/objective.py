import torch


class Objective(object):
    def __init__(self, goal=[1.0, 1.0], device="cuda:0"):
        self.nav_goal = torch.tensor(goal, device=device)

    def compute_running_cost(self, state: torch.Tensor):
        positions = state[:, 0:2]
        goal_dist = torch.linalg.norm(positions - self.nav_goal, axis=1)
        return goal_dist * 1.0
