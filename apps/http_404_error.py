import dash
import dash_core_components as dcc
import dash_html_components as html

from apps import menu_tree
from apps import utils


children = []
children += [html.H1('404 ERROR Page Not Found')]
children += [html.Label('アクセスしようとしたページが見つかりませんでした。')]


layout = html.Div([
    menu_tree.layout,
    html.Div(children=children, style={'padding': 10, 'flex': 4})
], style={'display': 'flex', 'flex-direction': 'row'})
