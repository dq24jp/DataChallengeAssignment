
from common import *
import matplotlib.pyplot as plt



# sum revenue by state
state_revenue = (
data.groupby('shipping_state')['amount']
    .sum()
    .sort_values(ascending=False)
)

print(state_revenue.head())

# plot state revenue
state_revenue.head(10).plot(kind='bar')

# add labels
plt.title('Top 10 States by Revenue')
plt.ylabel('Total Revenue')
plt.xlabel('Shipping State')
plt.xticks(rotation=0)


plt.show()