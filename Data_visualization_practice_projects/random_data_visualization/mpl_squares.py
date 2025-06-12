import matplotlib.pyplot as plt

# pyplot contains a number of functions that help generate charts and p
input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25] # a list to hold the date we'll plot

plt.style.use('_mpl-gallery-nogrid')
fig, ax = plt.subplots()                         # return tuple (figure, axes)
ax.plot(input_value, squares, linewidth=3)       # plot() ,method which tries to plot the date in meaningfull way

# set chart title and lable axes.
ax.set_title("Square Number", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("square of values", fontsize=14)

# set size of tick lables.
ax.tick_params(labelsize=14)

plt.show()