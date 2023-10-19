import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
  'Product' : [
    'Tide', 'Ariel', 'Surf', 'Champion', 'Calla'
  ],
  'Consumers' : [
    400, 1000, 500, 800, 700
  ]
}

data2 = {
  'Product' : [
    'Joy', 'Smart', 'Dash', 'Axion', 'Brand X'
  ],

  'Consumers' : [
    5000, 3000, 2000, 1000, 8000
  ]
}

df = pd.DataFrame(data)
df = pd.DataFrame(data2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 7))

ax1.bar(df['Product'], df['Consumers'], color='blue')
ax1.set_xlabel('Product')
ax1.set_ylabel('Total Consumers')
ax1.set_title('Total Consumers in 5 Different Products')
ax1.tick_params(axis='x', rotation=56)

ax2.bar(df['Product'], df['Consumers'], color='skyblue')
ax2.set_xlabel('Product')
ax2.set_ylabel('Total Consumers')
ax2.set_title('Total Consumers in 5 different Products')
ax2.tick_params(axis='x', rotation=60)

#plt.figure(figsize=(10, 6))
#plt.bar(df['Product'], df['Consumers'], color='skyblue')
#plt.xlabel('Product')
#plt.ylabel('Total Consumers')
#plt.title('Total Consumers in 5 Different Products')
#plt.xticks(rotation=60)

plt.tight_layout()
plt.show()
