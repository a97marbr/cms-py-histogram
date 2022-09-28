import pandas as pd
import matplotlib.pyplot as plt


# Read your data from file
file = "data.csv"
df = pd.read_csv(file, sep=",", header=None, names=['Chrome', 'Explorer', 'Firefox'])
    

# Call hist 
plt.hist(x=df['Chrome'], bins=[90, 100, 110, 120, 130, 140], align="mid", rwidth=0.4)

# Position the ticks around which bars are aligned
plt.xticks([100, 110, 120, 130, 140])

plt.xlabel('Load time ms')
plt.ylabel('Frequency')
plt.title('Chrome load-time frequency distribution')
plt.show()
