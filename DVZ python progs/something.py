import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset_Ques_1_4.csv')
plt.figure(figsize=(10, 5))
plt.plot(df['month_number'], df['total_profit'], linestyle = 'dotted', color = 'green', marker = 's', label = 'Total Profit')
for i,txt in enumerate(df['total_profit']):
    plt.annotate(txt , (df['month_number'][i], df['total_profit'][i]) ,textcoords="offset points", xytext = (0,5), ha = 'center')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Total Profit vs Month Number')
plt.xticks(rotation = 45)
plt.grid(True)
plt.legend()
plt.show()

fig,axes = plt.subplots(2, 1, figsize = (10,8),sharex = True)

for i,txt in enumerate(df['bathingsoap']):
    axes[0].annotate(txt, (df['month_number'][i], df['bathingsoap'][i]) ,textcoords="offset points", xytext = (0,5), ha = 'center')
    
axes[0].plot(df['month_number'], df['bathingsoap'], linestyle = 'dotted', color = 'green', marker = 's', label = 'Bathing Soap Sales')
axes[0].set_title('Bathing soap sales per month')
axes[0].set_xlabel("Month Number")
axes[0].set_ylabel("Bathing Soap Sales")
axes[0].legend()
axes[0].grid(True)

for i,txt in enumerate(df['facewash']):
    axes[1].annotate(txt, (df['month_number'][i], df['facewash'][i]) ,textcoords="offset points", xytext = (0,5), ha = 'center')
    
axes[1].plot(df['month_number'], df['facewash'], linestyle = 'dotted', color = 'green', marker = 's', label = 'Facewash Sales')
axes[1].set_title('Facewash sales per month')
axes[1].set_xlabel("Month Number")
axes[1].set_ylabel("Sales")
axes[1].legend()
axes[1].grid(True)
plt.xticks(rotation = 45)
plt.yticks(rotation = 75)
plt.tight_layout()
plt.show()