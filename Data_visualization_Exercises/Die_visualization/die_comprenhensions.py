import plotly.express as px

from die import Die

# create a D6
die = Die()

# Rolling the die
results = [die.roll() for roll in range(1_0000)]
# analuze the results
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

title = 'Rolling The D6 1_000 Times'
labels = {'x':'result', 'y':'Frquency of result'}
fig = px.line(x=range(1, die.num_sides+1), y=frequencies, title=title, labels=labels)
fig.show()