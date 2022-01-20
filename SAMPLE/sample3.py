"""
https://www.kkaneko.jp/pro/webui/dashtable.html
"""

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import seaborn as sns
import plotly.graph_objs as go

X = sns.load_dataset('iris')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

X_ = X.head(5)

app.layout = html.Div(children=[
    html.H1(children='Iris DataSet'),

    html.Div(children='''
        Iris DataSet Display
    '''),

    dash_table.DataTable(
        id='table', data=X_.to_dict('records'),
        columns=[{"name": i, "id": i} for i in X_.columns],
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                go.Scatter(
                    x = X.iloc[:,0], 
                    y = X.iloc[:,1],
                    mode = 'markers', 
                    marker={
                        'size': 10, 
                        'line': {'width': 0.5, 'color': 'white'}
                    }
                )
            ],
            'layout': {
                'title': 'Iris DataSet Graph'
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)