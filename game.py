import pygame
import random
from collections import deque

BLACK = (0,   0,   0)
GREEN = (0, 255,   0)
RED   = (255,  0,   0)

def place_food(snake, grid_size):
    food = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    while food in snake:
        food = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    return food

class SnakeGame:
    def __init__(self, grid_size=10, cell_size=40):
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.width     = grid_size * cell_size
        self.height    = grid_size * cell_size

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Q-Learning")
        self.clock = pygame.time.Clock()

        self.reset()

    def reset(self):
        center = self.grid_size // 2
        self.snake     = deque([
            (center,     center),
            (center - 1, center),
            (center - 2, center)
        ])
        self.direction  = (1, 0)
        self.food       = place_food(self.snake, self.grid_size)
        self.score      = 0
        self.frame_count = 0

    def is_collision(self, point):
        if point[0] < 0 or point[0] >= self.grid_size:
            return True
        if point[1] < 0 or point[1] >= self.grid_size:
            return True
        if point in self.snake:
            return True
        return False

    def step(self, action):
        self.frame_count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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

        if self.is_collision(new_head) or self.frame_count > 100 * len(self.snake):
            return -10, True, self.score

        self.snake.appendleft(new_head)

        if new_head == self.food:
            self.score += 1
            reward      = 10
            self.food   = place_food(self.snake, self.grid_size)
        else:
            self.snake.pop()
            reward = -0.1

        return reward, False, self.score

    def draw(self):
        self.screen.fill(BLACK)

        for segment in self.snake:
            pygame.draw.rect(
                self.screen,
                GREEN,
                (segment[0] * self.cell_size,
                 segment[1] * self.cell_size,
                 self.cell_size,
                 self.cell_size)
            )

        pygame.draw.rect(
            self.screen,
            RED,
            (self.food[0] * self.cell_size,
             self.food[1] * self.cell_size,
             self.cell_size,
             self.cell_size)
        )

        pygame.display.flip()