import matplotlib.pyplot as plt
import json

# Load training loss values from the JSON files
with open('training_losses1.json', 'r') as f:
    training_losses1 = json.load(f)

with open('training_losses2.json', 'r') as f:
    training_losses2 = json.load(f)

# Determine the length of the longer array
max_length = max(len(training_losses1), len(training_losses2))

# Extend the shorter array with None values
training_losses1.extend([None] * (max_length - len(training_losses1)))
training_losses2.extend([None] * (max_length - len(training_losses2)))

# Prepare data for plotting
epochs = range(1, max_length + 1)

# Plot the training loss values
plt.plot(epochs, training_losses1, 'bo-', label='Tfmr-scratch')
plt.plot(epochs, training_losses2, 'ro-', label='Tfmr-finetune')
plt.title('Training Loss Comparison')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# Save the plot to a PNG file
plt.savefig('training_loss_comparison.png')
plt.show()