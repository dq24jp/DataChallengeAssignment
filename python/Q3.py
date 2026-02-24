# 3. How does customer age affect purchase amount?

import matplotlib.pyplot as plt
from common import data


x_dat = data['customer_age']
y_dat = data['amount']

plot = plt.figure()
plt.plot(x_dat, y_dat, "k .")
plt.title("Purchase Amount vs Customer Age")
plt.xlabel("Customer age (years)")
plt.ylabel("Purchase amount (dollars)")
plt.show()
