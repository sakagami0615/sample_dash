import dash
import dash_core_components as dcc
import dash_html_components as html

from apps import menu_tree


layout = html.Div([
    menu_tree.layout,

    html.Div(children=[

        html.H3('Show dashboard'),

    ], style={'padding': 10, 'flex': 4})
], style={'display': 'flex', 'flex-direction': 'row'})
