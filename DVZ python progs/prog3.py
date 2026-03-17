import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset_Ques_1_4.csv')
product_cols = ['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']
product_sales = df[product_cols].sum()
max_sale = product_sales.max()
explode_values = [0.1 if val == max_sale else 0 for val in product_sales]

sales_labels = [str(int(val)) for val in product_sales]
plt.figure(figsize=(10,8))
plt.pie(
    product_sales,
    labels = sales_labels,
    explode = explode_values,
    startangle=60,
    labeldistance = 0.7,
    shadow = True,
    textprops = {'weight':'bold'}
)
plt.legend(product_sales.index, title="Products", loc = "center left", bbox_to_anchor = (1, 0.5))
plt.title("Total Sales of Each Product in Last Year")
plt.axis('equal')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,4))
plt.barh(['Face Cream','Face Wash'],[df['facecream'].sum(),df['facewash'].sum()],color = ['skyblue','orange'],label = 'Face Cream')
plt.xlabel("Sales")
plt.ylabel("Months")
plt.title("Face Cream vs Face wash comparision")
plt.show()