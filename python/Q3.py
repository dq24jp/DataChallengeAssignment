# 3. How does customer age affect purchase amount?

import numpy.polynomial.polynomial as polynomial
import matplotlib.pyplot as plt
from common import data

# get data to plot, excluding missing ages
valid_data = data[data['customer_age'].isna()==False]
x_dat = valid_data['customer_age']
y_dat = valid_data['amount']
(trend_b, trend_m) = polynomial.polyfit(x_dat, y_dat, deg=1)

# trend line
y_trend = trend_m*x_dat + trend_b

# plot order amount vs customer age
plot = plt.figure()
plt.plot(x_dat, y_dat, "k .")
plt.plot(x_dat, y_trend, "b-,")
plt.title("Purchase Amount vs Customer Age")
plt.xlabel("Customer age (years)")
plt.ylabel("Purchase amount (dollars)")
plt.legend(["Ages", f"Trend (m={round(trend_m, 3)})"])


# output
plt.show()
