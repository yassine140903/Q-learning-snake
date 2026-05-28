import matplotlib
matplotlib.use('Agg')  # non-interactive backend, no GUI window
import matplotlib.pyplot as plt

def plot(scores, mean_scores, episode):
    # only plot every 10 episodes to avoid slowdown
    if episode % 10 != 0:
        return
    
    plt.clf()
    plt.title("Training Progress")
    plt.xlabel("Episode")
    plt.ylabel("Score")
    plt.plot(scores,      label="Score")
    plt.plot(mean_scores, label="Mean Score")
    plt.legend()
    plt.ylim(bottom=0)
    plt.savefig("progress.png")
    plt.close()