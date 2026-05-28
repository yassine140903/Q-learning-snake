import numpy as np
import random

class Agent:
    def __init__(self):
        self.q_table = {}
        self.alpha   = 0.1
        self.gamma   = 0.9
        self.epsilon = 1.0

    def get_state(self, game):
        head = game.snake[0]
        food = game.food

        clockwise    = [(1,0), (0,1), (-1,0), (0,-1)]
        idx          = clockwise.index(game.direction)
        dir_straight = clockwise[idx % 4]
        dir_left     = clockwise[(idx - 1) % 4]
        dir_right    = clockwise[(idx + 1) % 4]

        straight = (head[0] + dir_straight[0], head[1] + dir_straight[1])
        left     = (head[0] + dir_left[0],     head[1] + dir_left[1])
        right    = (head[0] + dir_right[0],    head[1] + dir_right[1])

        danger_straight = int(game.is_collision(straight))
        danger_left     = int(game.is_collision(left))
        danger_right    = int(game.is_collision(right))

        food_left  = int(food[0] < head[0])
        food_right = int(food[0] > head[0])
        food_up    = int(food[1] < head[1])
        food_down  = int(food[1] > head[1])

        dir_right = int(game.direction == (1,  0))
        dir_left  = int(game.direction == (-1, 0))
        dir_down  = int(game.direction == (0,  1))
        dir_up    = int(game.direction == (0, -1))

        return (
            danger_straight, danger_left, danger_right,
            food_left, food_right, food_up, food_down,
            dir_left, dir_right, dir_up, dir_down
        )

    def get_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, 2)
        else:
            q_values = self.q_table.get(state, [0, 0, 0])
            return int(np.argmax(q_values))

    def update(self, state, action, reward, next_state):
        current_q = self.q_table.get(state, [0, 0, 0])[action]
        next_q    = max(self.q_table.get(next_state, [0, 0, 0]))

        new_q = current_q + self.alpha * (reward + self.gamma * next_q - current_q)

        if state not in self.q_table:
            self.q_table[state] = [0, 0, 0]

        self.q_table[state][action] = new_q

    def decay_epsilon(self):
        self.epsilon = max(self.epsilon * 0.995, 0.01)