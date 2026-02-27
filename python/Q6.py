# 6. What percentage of customers make repeat purchases?

from common import data


# amount of orders from each customer
order_counts = data.groupby('customer_id')['customer_id'].count()

# customers with more than 1 order
repeats = order_counts[order_counts>1]

num_customers = order_counts.count()
num_repeats = repeats.count()

repeat_orders = order_counts - 1

repeat_percentage = num_repeats/num_customers * 100


# output
print(f"{num_repeats} repeat customers out of {num_customers} total customers")
print(f"{round(repeat_percentage, 1)}% repeat customers")
