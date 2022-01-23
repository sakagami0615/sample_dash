from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app
from apps import parameter
from layouts import menu_tree, dashboard, create_daily, setting_daily, setting_user, http_404_error


app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    menu_tree.layout,
    html.Div(id="page-content")
], style={'display': 'flex', 'flex-direction': 'row'})


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == '/':
        return dashboard.create_layout()
    elif pathname == dashboard.PATHNAME:
        return dashboard.create_layout()
    elif pathname == setting_user.PATHNAME:
        return setting_user.create_layout(parameter.USER_PARAM_DICT)
    elif pathname == setting_daily.PATHNAME:
        return setting_daily.create_layout(parameter.DAILY_PARAM_DICT)
    elif pathname == create_daily.PATHNAME:
        return create_daily.create_layout()
    else:
        return http_404_error.create_layout()


if __name__ == '__main__':
    app.run_server(debug=True)
