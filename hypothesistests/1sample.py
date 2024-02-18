# Import necessary libraries
import numpy as np
from scipy import stats
from hypothesisutils import interpret_p

# Given student scores
student_scores = np.array([72, 89, 65, 73, 79, 84, 63, 76, 85, 75])

# H0: media = mu; Ha: media <> mu.
mu = 70

# Perform one-sample t-test
# alternative{‘two-sided’, ‘less’, ‘greater’}
t_stat, p_value = stats.ttest_1samp(student_scores, mu, alternative='two-sided')
print("T statistic:", t_stat)

# Interpret the results
interpret_p(p_value)