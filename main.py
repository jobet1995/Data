import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Product': ['Tide', 'Ariel', 'Surf', 'Champion', 'Calla'],
    'Consumers': [400, 1000, 500, 800, 700]
}

data2 = {
    'Product': ['Joy', 'Smart', 'Dash', 'Axion', 'Brand X'],
    'Consumers': [5000, 3000, 2000, 1000, 8000]
}

pie_graph = {
    'Product': ['Tide', 'Ariel', 'Surf', 'Champion', 'Calla'],
    'Consumers': [1.0, 5.0, 7.0, 9.1, 11.1]
}

df = pd.DataFrame(data)
df = pd.DataFrame(data2)
df = pd.DataFrame(pie_graph)

fig, (ax1, ax2, ax3) = plt.subplots(1, 2, 3, figsize=(12, 7, 8))

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

ax3.pie(df['Market Share'],
        labels=df['Consumers'],
        autopct='%1.1f%%',
        startangle=90,
        colors=['blue', 'green', 'skyblue', 'orange', 'lightblue'])
ax3.axis('equal')
ax3.set_title('Market Shares')

#plt.figure(figsize=(10, 6))
#plt.bar(df['Product'], df['Consumers'], color='skyblue')
#plt.xlabel('Product')
#plt.ylabel('Total Consumers')
#plt.title('Total Consumers in 5 Different Products')
#plt.xticks(rotation=60)

plt.tight_layout()
plt.show()
