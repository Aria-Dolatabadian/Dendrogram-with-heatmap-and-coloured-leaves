# Libraries
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

# Data set
df = pd.read_csv (r'mtcars.csv')
print (df)
df = df.set_index('model')
df

# Prepare a vector of color mapped to the 'cyl' column
my_palette = dict(zip(df.cyl.unique(), ["orange", "yellow", "brown"]))
row_colors = df.cyl.map(my_palette)

# plot
sns.clustermap(df, metric="correlation", method="single", cmap="Blues", standard_scale=1, row_colors=row_colors)
plt.show()
