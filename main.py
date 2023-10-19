import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
  'Product' : [
    'Tide', 'Ariel', 'Surf', 'Champion'
  ],
  'Consumers' : [
    900, 700, 200, 10000
  ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.bar(df['Product'], df['Consumers'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Total Consumers')
plt.title('Total Consumers in 4 Different Products')
plt.xticks(rotation=60)

plt.tight_layout()
plt.show()
