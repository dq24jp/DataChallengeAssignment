# 6. What percentage of customers make repeat purchases?

import matplotlib.pyplot as plt
import numpy as np
from common import data


# amount of orders from each customer
amounts = data.groupby('customer_id')['customer_id'].count()

# customers with more than 1 order
repeats = amounts[amounts>1]

num_customers = amounts.count()
num_repeats = repeats.count()

repeat_percentage = num_repeats/num_customers * 100

print(f"{num_repeats} repeat customers out of {num_customers} total customers")
print(f"{round(repeat_percentage, 1)}% repeat customers")