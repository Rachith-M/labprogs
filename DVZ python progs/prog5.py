import pandas as pd
import matplotlib.pyplot as plt
x = pd.read_csv('sample.csv')

explode = []
min_val = min(x['pass_percentage'])

for i in x['pass_percentage']:
    if(i==min_val):
        explode.append(0.3)
    else:
        explode.append(0)

plt.figure(figsize=(7,7))
plt.pie(x['pass_percentage'], labels = x['subjects'], autopct ='%1.1f%%',startangle=140,
        explode=explode, shadow = True)
plt.title("Pass percentage of Subjects")
plt.show()

df = pd.read_csv('Dataset_Ques_1_4.csv')
print(df.columns)
profit_data = df['total_profit']
plt.figure(figsize=(8,6))
plt.hist(profit_data, bins=8, color = 'skyblue', edgecolor='black',alpha=0.9)
plt.xlabel("Profit Ranges")
plt.ylabel("Frequency")
plt.title("Histogram of Monthly Profits")
plt.show()