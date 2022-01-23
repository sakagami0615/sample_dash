import dash
import dash_core_components as dcc
import dash_html_components as html

from apps import menu_tree
from apps import utils


children = []
children += [html.H3('Setting User Param')]
children += [dcc.Markdown('''---''')]
children += utils.br()

children += utils.param_label('User Name', '日報メールに使用する名前を指定する。（特にこだわりがなければ名字を記入）')
children += [dcc.Input(value='', type='text')]
children += utils.br(2)

children += utils.param_label('Email address', '自身のOutlookのメールアドレスを指定する。')
children += [dcc.Input(value='', type='text')]
children += utils.br(2)

children += utils.param_label('Daily Excel File', '読み込む日報エクセルのPathを指定します。')
children += [dcc.Input(value='', type='text')]
children += utils.br(2)

children += utils.param_label('Daily Sheet Name', '読み込む日報エクセルのシート名を指定します。')
children += [dcc.Input(value='', type='text')]
children += utils.br(2)

children += [html.Label('Multi-Select Dropdown', className="param-title-label")]
children += [dcc.Dropdown(
                options=[
                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': u'Montréal', 'value': 'MTL'},
                    {'label': 'San Francisco', 'value': 'SF'}
                ],
                value=['MTL', 'SF'],
                multi=True
            )]
children += utils.br(2)

children += [html.Label('Radio Items', className="param-title-label")]
children += [dcc.RadioItems(
                options=[
                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': u'Montréal', 'value': 'MTL'},
                    {'label': 'San Francisco', 'value': 'SF'}
                ],
                value='MTL'
            )]
children += utils.br(2)

children += [html.Label('Checkboxes', className="param-title-label")]
children += [dcc.Checklist(
                options=[
                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': u'Montréal', 'value': 'MTL'},
                    {'label': 'San Francisco', 'value': 'SF'}
                ],
                value=['MTL', 'SF']
            )]
children += utils.br(2)


children += [html.Label('Text Input', className="param-title-label")]
children += [html.Br()]
children += [dcc.Input(value='MTL', type='text')]
children += utils.br(2)

children += [html.Label('Slider', className="param-title-label")]
children += [dcc.Slider(
                min=0,
                max=9,
                marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
                value=5,
            )]


layout = html.Div([
    menu_tree.layout,
    html.Div(children=children, style={'padding': 10, 'flex': 4})
], style={'display': 'flex', 'flex-direction': 'row'})
