#Owner:Kunyang Wang Matriculation no.:23-069-362

import numpy as np
import matplotlib.pyplot as plt

def calculate_probability_infected_given_positive(prevalence, sensitivity=0.99, specificity=0.99):
    
    # False positive rate is 1 - specificity
    false_positive_rate = 1 - specificity
    # The overall probability of a positive test
    probability_positive = (sensitivity * prevalence) + (false_positive_rate * (1 - prevalence))
    # The probability of being infected given a positive test result
    probability_infected_given_positive = (sensitivity * prevalence) / probability_positive
    return probability_infected_given_positive

# Prevalence values from 0.001% to 50%
prevalence_values = np.linspace(0.00001, 0.5, 1000)
specificity_values = [0.99, 0.999, 0.9999, 0.99999]

plt.figure(figsize=(12, 8))

for specificity in specificity_values:
    probabilities = [calculate_probability_infected_given_positive(p, specificity=specificity) for p in prevalence_values]
    plt.plot(prevalence_values*100, probabilities, label=f'Specificity: {specificity*100}%')

plt.title('Probability of Being Infected Given a Positive Test\nVarying Prevalence and Specificity, Sensitivity Fixed at 99%')
plt.xlabel('Infection Prevalence (%)')
plt.ylabel('Probability of True Infection (%)')
plt.xscale('log')
plt.xticks([0.001, 0.01, 0.1, 1, 10, 50], ['0.001%', '0.01%', '0.1%', '1%', '10%', '50%'])
plt.legend()
plt.grid(True)
plt.show()
