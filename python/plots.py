from matplotlib import pyplot as plt
import numpy as np
import matplotlib.dates
from datetime import datetime
plt.rcParams['text.usetex'] = True
data = [
    (11, 24, 18.75),
    (12, 8, 18),
    (13, 19, 20.125),
    (14, 15, 20.25),
    (15, 23, 19),
    (17, 16, 17.75),
]

print(data[0][0])
times = [datetime(2025, 4, 10, dat[0], dat[1]) for dat in data]
values = [100*dat[2]+3000 for dat in data]
times = matplotlib.dates.date2num(times)
print(np.mean(values))
yerr = 12.5
plt.errorbar(times, values, yerr=yerr, fmt='o')
plt.gcf().autofmt_xdate()
myFmt = matplotlib.dates.DateFormatter('%H:%m')
plt.gca().xaxis.set_major_formatter(myFmt)
plt.xlabel(r"Time of day")
plt.ylabel(r"Temperature ($K$)")
# plt.show()
plt.savefig("temps.pdf")
print(times)
