# 5. Is there a relationship between product category and customer age?

import matplotlib.pyplot as plt
import numpy as np
from common import data

# points to plot
x_dat = data['product_category']
y_dat = data['customer_age']

# per-category data (mean, median, stdev)
categories = data['product_category'].unique()
means = data.groupby('product_category')['customer_age'].mean()
medians = data.groupby('product_category')['customer_age'].median()
stdevs = data.groupby('product_category')['customer_age'].std()

# plot customer ages vs category
plot = plt.figure()
plt.plot(x_dat, y_dat, "k .")
plt.title("Age across categories")
plt.xlabel("Product category")
plt.ylabel("Customer age (years)")

# plot mean, median, outlier boundary
plt.plot(categories, means, "r x")
plt.plot(categories, medians, "b x")
plt.errorbar(categories, medians, 2*stdevs, fmt="b x", alpha=0.2, elinewidth=15) # 2*stdev is boundary for outliers


plt.legend(["ages", "mean age", "median age", "expected range"])

plt.show()
