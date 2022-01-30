from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app

from apps.menutree import Menutree
from apps.dashboard import Dashboard
from apps.setting_daily import SettingDaily
from apps.setting_user import SettingUser
from apps.create_daily import CreateDaily
from apps.http_404 import Http404


app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    Menutree.create_layout(),
    html.Div(id="page-content")
], style={'display': 'flex', 'flex-direction': 'row'})


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == '/':
        return Dashboard.create_layout()
    elif pathname == Dashboard.PATHNAME:
        return Dashboard.create_layout()
    elif pathname == SettingUser.PATHNAME:
        return SettingUser.create_layout()
    elif pathname == SettingDaily.PATHNAME:
        return SettingDaily.create_layout()
    elif pathname == CreateDaily.PATHNAME:
        return CreateDaily.create_layout()
    else:
        return Http404.create_layout()


if __name__ == '__main__':
    app.run_server(debug=True)
