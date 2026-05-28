# Q-Learning Snake Game

An implementation of a Q-learning reinforcement learning agent trained to play the classic Snake game using Python and Pygame.

## Overview

This project demonstrates how a machine learning agent can learn to play Snake through Q-learning, a model-free reinforcement learning algorithm. The agent learns an optimal policy by interacting with the environment, receiving rewards for eating food and penalties for collisions.

## Project Structure

```
├── agent.py          # Q-learning agent implementation
├── game.py           # Snake game environment
├── train.py          # Training loop
├── utils.py          # Plotting utilities
└── requirements.txt  # Project dependencies
```

## Files Description

### `agent.py`
Implements the Q-learning agent with:
- **State Representation**: 11-dimensional feature vector including:
  - Danger detection (straight, left, right)
  - Food location relative to head (left, right, up, down)
  - Current direction (left, right, up, down)
- **Q-Table**: Dictionary-based storage for state-action values
- **Hyperparameters**:
  - Learning rate (α): 0.1
  - Discount factor (γ): 0.9
  - Initial exploration rate (ε): 1.0
- **Epsilon Decay**: Reduces exploration rate by 0.995 per episode

### `game.py`
Implements the Snake game environment using Pygame:
- 10x10 grid-based game board
- Snake starts with 3 segments
- Food randomly placed on the grid
- Collision detection with walls and self
- Reward system:
  - +10 for eating food
  - -10 for collision
  - -0.1 per step (encourages efficiency)
- Frame limit based on snake length to prevent infinite loops

### `train.py`
Main training loop that:
- Runs 3000 training episodes
- Uses epsilon-greedy exploration for action selection
- Updates Q-values based on rewards
- Tracks scores and mean scores
- Plots training progress every 10 episodes
- Prints episode statistics

### `utils.py`
Visualization utility:
- Plots score and mean score over training episodes
- Saves progress to `progress.png`
- Uses non-interactive matplotlib backend

## Requirements

- Python 3.11+
- pygame
- numpy
- matplotlib
- contourpy
- cycler
- python-dateutil
- fonttools
- kiwisolver
- pillow
- pyparsing

## Installation

1. Clone or download this project
2. Navigate to the project directory
3. Create and activate a virtual environment:
   ```bash
   python -m venv my_env
   my_env\Scripts\activate  # Windows
   source my_env/bin/activate  # macOS/Linux
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the training script:
```bash
python train.py
```

The agent will train for 3000 episodes, displaying:
- Episode number
- Score achieved in that episode
- Best score so far
- Mean score across all episodes
- Current epsilon value

Training progress will be saved to `progress.png`.

## How Q-Learning Works

Q-learning is a model-free RL algorithm that learns the value of actions in different states:

1. **State**: 11-dimensional vector describing the game situation
2. **Action**: One of three moves (turn left, go straight, turn right)
3. **Reward**: Feedback from the environment
4. **Q-Value Update**: `Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') - Q(s,a)]`

The agent balances exploration (trying random actions) with exploitation (using learned knowledge) through epsilon-greedy selection.

## Performance

The agent starts with random play and gradually improves as it learns:
- Early episodes: Low scores, high exploration
- Later episodes: Increasing scores as the policy converges
- Epsilon decay reduces exploration rate over time

## Customization

You can modify hyperparameters in `agent.py`:
- `alpha`: Learning rate (higher = faster learning)
- `gamma`: Discount factor (higher = values future rewards more)
- `epsilon`: Exploration rate (controlled by decay function)

And game parameters in `game.py`:
- `grid_size`: Board dimensions
- `cell_size`: Pixel size of each cell

## License

This project is open source and available for educational purposes.

## Author

Created as a reinforcement learning demonstration project.
