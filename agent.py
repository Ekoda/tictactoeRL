import torch
import torch.nn as nn
import environment
import random


class QNetwork(nn.Module):
    def __init__(self):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(9, 64)
        self.fc2 = nn.Linear(64, 9)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x


class Player:
    def __init__(self, role: int, exploration_rate: float = 1.0, learning_rate: float = 0.01):
        self.q_network = QNetwork()
        self.optimizer = torch.optim.Adam(self.q_network.parameters(), lr=learning_rate)
        self.criterion = criterion = nn.MSELoss()
        self.exploration_rate = exploration_rate # epsilon
        self.role = role
        self.state = None
        self.last_action = None

    def update_exploration_rate(self, decay_factor: float, min_exploration_rate: float = 0.05):
        self.exploration_rate = max(self.exploration_rate * decay_factor, min_exploration_rate)

    def train(self, next_state: [int], reward: int, gamma: float = 0.99):
        state_tensor = torch.FloatTensor(self.state)
        next_state_tensor = torch.FloatTensor(next_state)

        Q_values = self.q_network(state_tensor)
        next_Q_values = self.q_network(next_state_tensor)
        max_next_Q_value = torch.max(next_Q_values).item()

        target = Q_values.clone().detach()
        target[self.last_action] = reward + gamma * max_next_Q_value

        loss = self.criterion(Q_values, target)
        loss.backward()

        self.optimizer.step()
        self.state = next_state

    def make_move(self, state: [int], available_moves: [int], epsilon: float) -> int:
        self.state = state
        if random.random() < epsilon:
            self.last_action = random.choice(available_moves)
            return self.last_action
        else:
            state_tensor = torch.FloatTensor(state)
            Q_values = self.q_network(state_tensor)
            Q_values = {move: Q_values[move] for move in available_moves}
            self.last_action = max(Q_values, key=Q_values.get)
            return self.last_action