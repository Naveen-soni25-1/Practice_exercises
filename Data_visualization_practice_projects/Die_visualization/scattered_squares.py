import matplotlib.pyplot as plt

x_value = range(1, 1001)
y_value = [x**2 for x in x_value]

plt.style.use("dark_background")
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.cool, s=10)
# We pass the list of y-values to c, and then tell pyplot which colormap to use with the cmap argument

# set chart title and label axes.
ax.set_title("Square Number", fontsize=14)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')
# set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()