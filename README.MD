# Tic-Tac-Toe Reinforcement Learning

## Introduction

This project aimed at delving deeper into the mechanics of Reinforcement Learning (RL). The classic game of Tic-Tac-Toe serves as a sandbox for training agents using a simple neural network and the Q-Learning algorithm. The emphasis here is on understanding the interplay of exploration and exploitation, facilitated by an epsilon-greedy strategy.

## Getting Started

### Dependencies
- Python 3.10+
- PyTorch

### How to Run
1. Clone the repository.
2. Open the `arena.ipynb` notebook to run the experiments and view the results.

## Code Structure
- `environment.py`: Contains the `Board` class that simulates the Tic-Tac-Toe environment.
- `agent.py`: Houses the `Player` class, which comprises the neural network and the learning algorithm.
- `arena.ipynb`: Orchestrates the duels between the two agents.

## Exploration Strategy

An epsilon-greedy strategy is used for balancing exploration and exploitation. During the training phase, agents have a certain probability (`epsilon`) of making a random move, allowing them to explore new strategies. As training progresses, `epsilon` decays, leading the agents to rely more on their acquired knowledge—thus exploiting learned strategies.

The dynamics of the training were particularly interesting when the exploration rate was made adaptive. An agent that wins a round has its exploration rate reduced, making it more likely to exploit its learned strategies in subsequent rounds. However, to avoid getting stuck in a suboptimal policy, the exploration rate never drops below a certain threshold.

## Future Work

1. **Evaluation Metrics**: Introduce more nuanced metrics for evaluating the performance of the agents beyond mere win-loss ratios.
2. **User Interface**: Implement a simple UI to allow humans to play against the trained agents.
3. **Multi-Agent Competition**: Extend the environment to accommodate more than two agents, possibly introducing more complex board states.

## Lessons Learned

The project sheds light on the nuances of RL, particularly the balance between exploration and exploitation. One key takeaway was that an overly aggressive decay in the exploration rate could trap an agent in a suboptimal policy. This was mitigated by introducing a floor value for the exploration rate.

