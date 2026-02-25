# 6. What percentage of customers make repeat purchases?

import matplotlib.pyplot as plt
import numpy as np
from common import data



amounts = data.groupby('customer_id')['customer_id'].count().sort_values()
repeats = amounts[amounts>1]

num_customers = amounts.count()
num_repeats = repeats.count()

repeat_percentage = num_repeats/num_customers * 100

# print(amounts.head(5), amounts.tail(5))
print(f"{round(repeat_percentage, 1)}% repeat customers")