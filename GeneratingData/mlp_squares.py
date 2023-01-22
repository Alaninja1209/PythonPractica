import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 10)

#Information of the graffic
ax.set_title("Square numbers", fontsize = 24) #Fontsize controls the size of the text
ax.set_xlabel("Values", fontsize = 14)
ax.set_ylabel("Squares of Values", fontsize = 14)

#Set range for each axis
ax.axis([0, 1100, 0, 1100000])

#plt.show()
plt.savefig('squaresPlot.png')
