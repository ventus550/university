import matplotlib.pyplot as plt
from math import exp


# MB/month
# arctan(m)/month

def single_user(x):
	return x/30

def users_per_day(x):
	eexp = -(1/30)*x + 6
	return (10**5)/(1 + exp(eexp))

def data_per_day(x):
	if x == 0:
		return 0
	return data_per_day(x-1) + single_user(users_per_day(x))



xaxis = [x for x in range(450)]
data = [users_per_day(x) for x in xaxis]
#print(data[-1] - data[-30])
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.xlabel("Dni", fontsize=30)
plt.ylabel("Aktywni użytkownicy", fontsize=30)
plt.plot(xaxis, data)
#plt.yticks([1000, 2000, 3000])
#plt.ylim(0, 5)
plt.show()

