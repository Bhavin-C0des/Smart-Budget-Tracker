import plotly.graph_objects as go
from plotly.io import to_html

def create_pie_chart(expenses_by_category):
    labels = list(expenses_by_category.keys())
    values = list(expenses_by_category.values())

    figure = go.Figure(data=[go.Pie(labels=labels, values=values)])
    figure.update_traces(textinfo='percent+label')

    return to_html(figure, full_html=False)




