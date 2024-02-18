import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style(style="darkgrid")

tips =  sns.load_dataset("tips")
sns.relplot(data=tips, x="total_bill", y="tip")
plt.show()