#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

people = ['Farrah', 'Fred', 'Felicia']

# Names for the fruit types (for the legend)
fruit_names = ['apples', 'bananas', 'oranges', 'peaches']

# Colors for each fruit
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']  # red, yellow, orange, peach

# X positions for the bars
x = np.arange(len(people))

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Initialize the bottom positions for the stacked bars
bottom = np.zeros(3)

# Create the stacked bars
for i in range(len(fruit_names)):
    ax.bar(x, fruit[i], bottom=bottom, width=0.5, label=fruit_names[i], color=colors[i])
    bottom += fruit[i]

# Add labels, title, and legend
ax.set_xlabel('Person')
ax.set_ylabel('Quantity of Fruit')
ax.set_title('Number of Fruit per Person')

# Set the x-tick positions and labels
ax.set_xticks(x)
ax.set_xticklabels(people)

# Set the y-axis range and ticks
ax.set_ylim(0, 80)
ax.set_yticks(np.arange(0, 81, 10))

# Add a grid on the y-axis for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add the legend
ax.legend()

plt.tight_layout()
plt.show()

# Print the fruit matrix for reference
print("Fruit matrix (rows: apples, bananas, oranges, peaches; columns: Farrah, Fred, Felicia):")
print(fruit)