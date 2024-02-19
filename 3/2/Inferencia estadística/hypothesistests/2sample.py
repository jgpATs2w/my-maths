import seaborn as sns
import numpy as np
from scipy import stats
from hypothesisutils import interpret_p

iris = sns.load_dataset('iris')

setosa = iris[iris['species'] == 'setosa']
versicolor = iris[iris['species'] == 'versicolor']
setosa_petal_lengths = setosa['petal_length']
versicolor_petal_lengths = versicolor['petal_length']

t_stat, p_value = stats.ttest_ind(setosa_petal_lengths, versicolor_petal_lengths)

interpret_p(p_value)
