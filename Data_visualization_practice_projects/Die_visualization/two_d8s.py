import plotly.express as px

from die import Die

# create a two D8s.
die_1 = Die(8)
die_2 = Die(8)

results = []
# Roll both the dies.
for _ in range(1_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the result.
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
poss_results = list(range(2, max_results+1))
for value in poss_results:
    frequecy = results.count(value) # count same value in list
    frequencies.append(frequecy)

title = 'Rolling The Two D8, 1_000 times'
labels = {'x':'Result', 'y':'Frequencies of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()