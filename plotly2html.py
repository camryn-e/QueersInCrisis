"""
This code was tested using Anaconda 3.7

Render the plotly figure as an HTML section using a CDN link for the required js.
"""

import plotly.express as px

CR_inset_path = "docs/crisis-resources-inset.html"

## Test code -- this should be the actual figure!!
fig = px.scatter(x=range(10), y=range(10))

## Write a valid <div> section to embed in an HTML doc
## Use a CDN instead of embedding the js into the HTML
## Source: https://plotly.com/python/interactive-html-export/
fig.write_html(CR_inset_path, include_plotlyjs="cdn")
