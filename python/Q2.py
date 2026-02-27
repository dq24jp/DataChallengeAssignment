
from common import *
import matplotlib.pyplot as plt


# average order amount by payment method
avg_payment = (
data.groupby('payment_method')['amount']
    .mean()
    .sort_values(ascending=False)
)

print(avg_payment)

# plot average order amounts across payment methods
avg_payment.plot(kind='bar')

# add labels
plt.title('Average Order Amount by Payment Method')
plt.ylabel('Average Order Amount')
plt.xlabel('Payment Method')
plt.xticks(rotation=0)

plt.show()