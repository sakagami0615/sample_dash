import dash
import dash_core_components as dcc
import dash_html_components as html


layout = html.Div(children=[

    html.H2('Daily dashboard GUI'),

    html.Label('Show Dashboard'),
    html.Br(),
    dcc.Link('dashboard', href="/dashboard"),
    html.Br(),
    html.Br(),
    html.Label('Setting app param'),
    html.Br(),
    dcc.Link('setting_app', href="/setting_app"),
    html.Br(),
    html.Br(),
    html.Label('Setting daily param'),
    html.Br(),
    dcc.Link('setting_daily', href="/setting_daily"),
    html.Br(),
    html.Br(),
    html.Label('Create daily email'),
    html.Br(),

], style={'padding': 10, 'flex': 1})
