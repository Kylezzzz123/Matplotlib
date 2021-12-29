from matplotlib import pyplot as plt
# set the size of plot
plt.figure(figsize = (20,8), dpi = 80)   #(20, 8) is wight and height, dpi is dot per inch

x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,24,22,18,15]

plt.plot(x,y)

# reset x-aixs
# plt.xticks(x)    reset the x to default (2,26,2)
# plt.xticks(range(2,25,1))    # reset the x to (2,25,1)
xtick_labels = [i/2 for i in range(4,49)]  # from 2, 2.5,3,3.5,.....
# plt.xticks(xtick_labels[])   
plt.xticks(xtick_labels[::3])  # too crow, make every 3 in x

# reset y-axis
plt.yticks(range(min(y), max(y)+1))

#save 
plt.savefig("plt1.png")

#show the plot
plt.show()