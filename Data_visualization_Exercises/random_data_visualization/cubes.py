import matplotlib.pyplot as plt

x_value = list(range(1, 5_001))
y_value = [x**3 for x in x_value]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.cool, s=10)
ax.set_title("Cubic numbers")

# axis labels
ax.set_ylabel("Cubes of Values",fontsize=10)
ax.set_xlabel("Values", fontsize=10)

ax.axis([0,5100, 0, 130000000000])
ax.ticklabel_format(style='sci')
ax.tick_params(labelsize=14)

plt.show()