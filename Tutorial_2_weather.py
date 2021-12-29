from matplotlib import pyplot as plt
import random

x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

# set size of plot
plt.figure(figsize=(20,8), dpi=80)

plt.plot(x,y)

# reset the x-asix 
_x = list(x)
_xtick_labels = ["10:{}".format(i) for i in range(60)]
_xtick_labels +=["11:{}".format(i) for i in range(60)]       # list += []

plt.xticks(_x[::3], _xtick_labels[::3], rotation=-45)   # rotation is to rotatge the x-aixs labels

# Add labels and Title
plt.xlabel('Time')
plt.ylabel('Tempearture in C')
plt.title("Delta Temperature From 10 to 11 o'clock ")
plt.savefig("Weather1")

plt.show()
