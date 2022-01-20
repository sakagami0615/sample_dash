import dash
import dash_core_components as dcc
import dash_html_components as html

from apps import menu_tree


layout = html.Div([
    menu_tree.layout,

    html.Div(children=[

        html.H3('Setting daily param'),

        html.H4('User information'),

        html.Label('User name'),
        html.Br(),
        html.Label('Email address'),

        html.H4('Daily mail param'),
        html.Label('Header string'),
        html.Br(),
        html.Label('Fooder string'),
        html.Br(),
        html.Label('EOF string'),
        html.Br(),
        html.Label('Add last daily mail'),
        dcc.Checklist(
            options=[
                {'label': '', 'value': 1},
            ],
            value=[1]
        ),
        html.Br(),
        html.Label('Search mail folder'),
        html.Br(),
        html.Label('Number of times to search past mails'),
        html.Br(),
        html.Label('To/Cc'),
        html.Br(),
        html.Br(),

    ], style={'padding': 10, 'flex': 4})
], style={'display': 'flex', 'flex-direction': 'row'})
