"""
https://deepblue-ts.co.jp/visualization/python-dash/
"""

import dash
# グラフやインプットに使うパーツ
import dash_core_components as dcc
# HTMLを記述するためのパーツ
import dash_html_components as html
# コールバックを実装するためのもの
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)
app.layout = html.Div(
    children=[
        html.H1("Hello World!")
    ]
)
if __name__ == '__main__':
    app.run_server(debug=False)
