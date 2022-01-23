import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
from apps import dashboard, create_daily, setting_daily, setting_user
from apps import http_404

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Label('', id='log-text', className='log-label'),
    html.Div(id="page-content")
])

"""
各種Divのページは入れ子になっているからみつけることができないのでは？

menu_pageを外出しすれば解決？
"""

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
    #State(setting_daily.ID_LIST[0], "value")
    #[State(id, "value") for id in setting_daily.ID_LIST]
)
def display_page(pathname):
    if pathname == "/":
        return dashboard.layout
    elif pathname == "/dashboard":
        return dashboard.layout
    elif pathname == "/setting_user":
        return setting_user.layout
    elif pathname == "/setting_daily":
        return setting_daily.layout
    elif pathname == "/create_daily":
        return create_daily.layout
    else:
        return http_404.layout


if __name__ == '__main__':
    app.run_server(debug=True)
