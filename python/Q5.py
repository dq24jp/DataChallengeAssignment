# 5. Is there a relationship between product category and customer age?

import matplotlib.pyplot as plt
import numpy as np
from common import data

# points to plot
x_dat = data['product_category']
y_dat = data['customer_age']

category_ages = data.groupby('product_category')['customer_age']

# per-category age data (mean, median, stdev)
categories = data['product_category'].unique()
medians = category_ages.median()
stdevs = category_ages.std()

# total age data
total_median = y_dat.median()
total_stdev = y_dat.std()

# category age data
cat_stdev = medians.std()
cat_zscores = (medians-total_median)/total_stdev

# plot customer ages vs category
plot = plt.figure()
plt.plot(x_dat, y_dat, "k .")
plt.title("Age across categories")
plt.xlabel("Product category")
plt.ylabel("Customer age (years)")

# plot median, outlier boundary
plt.plot(categories, medians, "b x")
plt.errorbar(categories, medians, 2*stdevs, fmt="b x", alpha=0.2, elinewidth=15) # 2*stdev is boundary for outliers

plt.legend(["ages", "median age", "expected range"])


def beautify_category_data(cat_name, cat_data):
	"""
		formats `cat_name`, `cat_data` into a pretty string for printing outputs
	"""
	return (
		f"{(cat_name+":").ljust(14)}"			# category name, left-justified
		f"{"" if cat_data<0 else " "}"			# even out negative and positive numbers
		f"{str(round(cat_data, 2)).ljust(6)}"	# category data, left-justified
	)

# output
print(f"standard deviation of ages between categories: {round(medians.std(), 3)}")
print(f"z-scores of category medians:")
for cat in categories:
	print(f"\t{beautify_category_data(cat, cat_zscores[cat])}")
plt.show()