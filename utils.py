
import random


def place_food(snake, grid_size):
    food = tuple(random.randint(0, grid_size - 1) for _ in range(2))
    while food in snake:
        food = tuple(random.randint(0, grid_size - 1) for _ in range(2))
    return food


def step(self, action):
    self.frame_count += 1
    
    clockwise = [(1,0), (0,1), (-1,0), (0,-1)]
    idx = clockwise.index(self.direction)
    
    if action == 0:
        self.direction = clockwise[(idx - 1) % 4]
    elif action == 1:
        self.direction = clockwise[idx % 4]
    elif action == 2:
        self.direction = clockwise[(idx + 1) % 4]
    
    head = self.snake[0]
    new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
    
    # check collision or timeout
    if self.is_collision(new_head) or self.frame_count > 100 * len(self.snake):
        return -10, True, self.score
    
    # move snake
    self.snake.appendleft(new_head)
    
    # check food
    if new_head == self.food:
        self.score += 1
        reward = 10
        self.food = place_food(self.snake, self.grid_size)
    else:
        self.snake.pop()
        reward = -0.1
    
    return reward, False, self.score