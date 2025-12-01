"""Suppose that a population consists of 58 households and it is required to draw a random sample of size 8.
Describe direct method for selecting the random sample with and without replacement."""
import random

# Define the population of 58 households (represented as numbers 1 to 58)
population = list(range(1, 59))

# Sample size
sample_size = 8

# Simple Random Sampling Without Replacement (SRSWOR)
sample_wor = random.sample(population, sample_size)

# Simple Random Sampling With Replacement (SRSWR)
sample_wr = [random.choice(population) for _ in range(sample_size)]

# Display results
print("sample without replacement:",sample_wor)
print("sample with replacement:",sample_wr)
