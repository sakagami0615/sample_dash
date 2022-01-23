from dash import dcc
from dash import html


# HTML Path Name
PATHNAME = '/dashboard'

def create_layout():
    children = []
    children += [html.H3('Show Dashboard')]
    children += [dcc.Markdown('''---''')]

    layout = html.Div(children=children, className="page-layout")
    return layout
