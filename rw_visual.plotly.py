from plotly.graph_objs import Scatter, Layout
from plotly import offline

from random_walk import RandomWalk


rw = RandomWalk(50_000)
rw.fill_walk()

data = [Scatter(
    x=rw.x_values, y=rw.y_values, mode='markers',
    marker=dict(
        color=rw.y_values, colorscale='Blues', size=1)
    )]
my_layout = Layout(
    xaxis=({
        'showgrid': False,
        'showline': False,
        'zeroline': False
        }),
    yaxis=({
        'showgrid': False,
        'showline': False,
        'zeroline': False
        })
    )
offline.plot(
    {'data': data, 'layout': my_layout}, filename='rw_visual.plotly.html'
    )
