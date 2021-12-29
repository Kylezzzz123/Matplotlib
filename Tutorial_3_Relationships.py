from matplotlib import pyplot as plt
  
x = range(11,31)
y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]

# reset the size of plot
plt.figure(figsize=(20,8), dpi=80)

# plot 
plt.plot(x,y)

# reset x and y
_xtick_labels = ["{} years old".format(i) for i in x]
plt.xticks(x, _xtick_labels, rotation=-45)
plt.yticks(range(0,9))

# labels x and y
plt.xlabel('Age')
plt.ylabel('Numbers of relationships')
plt.title('Numbers of relationships make from age 11 to 30')

# plot makeup
plt.grid(alpha=0.1)      # alpha is transparency

# save
plt.savefig('Relationships1.png')
plt.show()

