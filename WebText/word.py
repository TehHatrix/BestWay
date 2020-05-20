import plotly.io as pio

fig = dict({
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "a figure specified by python dictionary"}}
})

pio.show(fig)
