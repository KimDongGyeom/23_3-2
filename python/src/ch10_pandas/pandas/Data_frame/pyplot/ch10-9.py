import matplotlib.pyplot as plt
import pandas as pd

countries_df = pd.read_csv('src/data/csv/countries.csv', index_col=0)

# countries_df['population'].plot(kind='bar', color=('b', 'darkorange', 'g', 'r', 'm'))
countries_df['population'].plot(kind='pie')

plt.show()
