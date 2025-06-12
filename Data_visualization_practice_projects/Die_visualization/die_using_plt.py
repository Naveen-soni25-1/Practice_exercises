import matplotlib.pyplot as plt

from die import Die

# Create a D6.
die = Die()

results = [die.roll() for roll_num in range(1_000)]
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

title = "Rolling D6 1_000 Times."
x_label = "results."
y_label = "Frequency of Result."
style  = "dark_background"
fs = 14
ls = 14

plt.style.use(style='dark_background')
fig, ax = plt.subplots()

# set plot type
ax.bar(range(1, die.num_sides+1), frequencies, 0.3, edgecolor='white')
# labels, title, fontsize
ax.set_title(title, fontsize=fs)
ax.set_xlabel(xlabel=x_label, fontsize=fs)
ax.set_ylabel(ylabel=y_label, fontsize=fs)
ax.tick_params(labelsize=ls)

plt.show()