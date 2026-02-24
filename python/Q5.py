# 5. Is there a relationship between product category and customer age?

import matplotlib.pyplot as plt
import numpy as np
from common import data


x_dat = data['product_category']
y_dat = data['customer_age']

categories = data['product_category'].unique()
means = data.groupby('product_category')['customer_age'].mean()
medians = data.groupby('product_category')['customer_age'].median()
stdevs = data.groupby('product_category')['customer_age'].std()

plot = plt.figure()
plt.plot(x_dat, y_dat, "k .")
plt.plot(categories, means, "r x")
plt.plot(categories, medians, "b x")
plt.errorbar(categories, medians, 2*stdevs, fmt="b x", alpha=0.2, elinewidth=20)

plt.legend(["ages", "mean age", "median age", "expected range"])

plt.title("Age across categories")
plt.xlabel("Product category")
plt.ylabel("Customer age")
plt.show()
