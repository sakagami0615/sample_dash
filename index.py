import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import dashboard, setting_app, setting_daily


app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/":
        return dashboard.layout
    elif pathname == "/dashboard":
        return dashboard.layout
    elif pathname == "/setting_app":
        return setting_app.layout
    elif pathname == "/setting_daily":
        return setting_daily.layout
    else:
        return "404"


if __name__ == '__main__':
    app.run_server(debug=True)
