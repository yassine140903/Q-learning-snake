import pygame
from game  import SnakeGame
from agent import Agent
from utils import plot

game  = SnakeGame()
agent = Agent()

scores      = []
mean_scores = []
best_score  = 0
total_score = 0

for episode in range(3000):
    game.reset()
    state = agent.get_state(game)

    while True:
        action          = agent.get_action(state)
        reward, done, score = game.step(action)
        next_state      = agent.get_state(game)

        agent.update(state, action, reward, next_state)

        state = next_state

        game.draw()
        game.clock.tick(30)

        if done:
            agent.decay_epsilon()

            total_score += score
            mean_score   = total_score / (episode + 1)

            if score > best_score:
                best_score = score

            scores.append(score)
            mean_scores.append(mean_score)

            print(f"Episode: {episode+1} | Score: {score} | Best: {best_score} | Mean: {mean_score:.2f} | Epsilon: {agent.epsilon:.3f}")

            plot(scores, mean_scores, episode)
            break

pygame.quit()