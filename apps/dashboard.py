from dash import dcc
from dash import html

from setting import PAGE_LAYOUT_CLASS

class Dashboard:
    
    PATHNAME = '/dashboard'

    @staticmethod
    def create_layout():
        children = []
        children += [html.H3('Show Dashboard')]
        children += [dcc.Markdown('''---''')]

        layout = html.Div(children=children, className=PAGE_LAYOUT_CLASS)
        return layout
