import numpy as np
from scipy.stats import bernoulli, binom
print("----- Bernoulli Distribution -----")
p = 0.7 # Probability of passing an exam
bernoulli_samples = bernoulli.rvs(p, size=10)
print("Probability of Passing:", p)
print("Student Outcomes (1=Pass, 0=Fail):")
print(bernoulli_samples)
print("\nProbability of Pass:")
print(bernoulli.pmf(1, p))
print("Probability of Fail:")
print(bernoulli.pmf(0, p))
print("\n\n----- Binomial Distribution -----")
n = 10 # Number of students
p = 0.7 # Probability of passing
k = 8 # Probability that exactly 8 students pass
binomial_probability = binom.pmf(k, n, p)
print("Number of Students:", n)
print("Probability of Passing:", p)
print(f"\nProbability that exactly {k} students pass:")
print(binomial_probability)
random_binomial = binom.rvs(n, p, size=5)
print("\nRandom Binomial Outcomes:")
print(random_binomial)