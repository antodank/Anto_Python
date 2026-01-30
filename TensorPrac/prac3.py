import wandb
import time

# 1. Start a run
wandb.init(project="super-simple-demo")

# 2. Fake training loop
for step in range(10):
    loss = 10 - step      # pretend loss decreases
    accuracy = step / 10  # pretend accuracy increases

    # 3. Log metrics
    wandb.log({"loss": loss, "accuracy": accuracy})

    time.sleep(1)

wandb.finish()