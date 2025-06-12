import plotly.express as px
from random_walk import RandomWalk

# Create a random walk instance and fill it with points
rw = RandomWalk()
rw.fill_walk()

# Improved title and axis labels
title = "2D Random Walk Visualization"
x_label = "X Position"
y_label = "Y Position"

# Create scatter plot with enhanced styling
fig = px.scatter(
    x=rw.x_values,
    y=rw.y_values,
    title=title,
    labels={"x": x_label, "y": y_label},
)

# Customize marker appearance
fig.update_traces(marker=dict(size=4, color=rw.y_values, colorscale='Viridis'), mode='markers')

# Improve layout
fig.update_layout(
    xaxis_title=x_label,
    yaxis_title=y_label,
    title_x=0.5,  # Center the title
    template="plotly_dark",  # Use a dark theme (optional)
    height=600,
    width=800
)

# Set equal aspect ratio for x and y axes
fig.update_yaxes(scaleanchor="x", scaleratio=1)

# Show the plot
fig.show()
print(px.colors)
