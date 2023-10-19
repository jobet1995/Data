import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Product': ['Tide', 'Ariel', 'Surf', 'Champion', 'Calla'],
    'Consumers': [400, 1000, 500, 800, 700]
}

#data2 = {
#'Product': ['Joy', 'Smart', 'Dash', 'Axion', 'Brand X'],
#'Consumers': [5000, 3000, 2000, 1000, 8000]
#}

pie_graph = {
    'Product': ['Tide', 'Ariel', 'Surf', 'Champion', 'Calla'],
    'Market Shares': [10, 23, 45, 60, 90]
}

data_line = {
  'Month' : [
    'Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
  ],
  'Sales' :[
    400, 700, 100, 300, 500, 600, 450, 890, 900, 1000, 940, 189
  ]
}
df1 = pd.DataFrame(data)
#df = pd.DataFrame(data2)
dfpie = pd.DataFrame(pie_graph)
dfline = pd.DataFrame(data_line)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 7))

ax1.bar(df1['Product'], df1['Consumers'], color='skyblue')
ax1.set_xlabel('Product')
ax1.set_ylabel('Total Consumers')
ax1.set_title('Total Consumers in 5 Different Products')
ax1.tick_params(axis='x', rotation=56)

#ax2.bar(df['Product'], df['Consumers'], color='skyblue')
#ax2.set_xlabel('Product')
#ax2.set_ylabel('Total Consumers')
#ax2.set_title('Total Consumers in 5 different Products')
#ax2.tick_params(axis='x', rotation=60)

ax2.pie(dfpie['Market Shares'],
        labels=dfpie['Market Shares'],
        autopct='%1.1f%%',
        startangle=90,
        colors=['blue', 'green', 'skyblue', 'orange', 'lightblue'])
ax2.axis('equal')
ax2.set_title('Market Shares')

ax3.plot(dfline['Month'], dfline['Sales'], marker='o',color='green')
ax3.set_xlabel('Month')
ax3.set_ylabel('Sales')
ax3.set_title('Monthly Market Sales')
ax3.grid(True)

#plt.figure(figsize=(10, 6))
#plt.bar(df['Product'], df['Consumers'], color='skyblue')
#plt.xlabel('Product')
#plt.ylabel('Total Consumers')
#plt.title('Total Consumers in 5 Different Products')
#plt.xticks(rotation=60)

plt.tight_layout()
plt.show()
