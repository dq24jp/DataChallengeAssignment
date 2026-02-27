
from common import *
import matplotlib.pyplot as plt

# Calulate average return rate
return_rate = (
  data.groupby('product_category')['returned']
      .mean()
      .sort_values(ascending=False)
)

# convert to precentage
return_rate_percent = return_rate * 100
print(return_rate_percent)

# plot bar graph of return rate across categories
return_rate.plot(kind='bar')


# add labels
plt.title('Return Rate by Product Category')
plt.ylabel('Return Rate')
plt.xlabel('Product Category')
plt.xticks(rotation=0)

plt.show()