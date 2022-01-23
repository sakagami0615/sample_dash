import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from apps import menu_tree
from apps import utils

# HTML ID Parameter
SUBJECT_TEXT_ID = 'subject-text'
HEADER_TEXT_ID = 'header-text'
FOODER_TEXT_ID = 'fooder-text'

ID_LIST = [
    SUBJECT_TEXT_ID,
    HEADER_TEXT_ID,
    FOODER_TEXT_ID
]

# Create HTML Layout
children = []
children += [html.H3('Setting Daily Param')]

children += utils.param_desc_label('文字列指定のパラメータでは下記の中括弧付き変数を指定できます。')
children += utils.param_desc_label('{name} : 名前、 {day} : 月日、 {work_time} : 業務時間')
children += [dcc.Markdown('''---''')]
children += utils.br()

children += utils.param_label('Subject String', '日報メールの件名を指定する。')
children += [dcc.Input(value='', id=SUBJECT_TEXT_ID, type='text')]
children += utils.br(2)

children += utils.param_label('Header String', '日報メールに記載するヘッダー文章を指定する。（○○さん　お疲れ様です… の部分の文章）')
children += [dcc.Input(value='', id=HEADER_TEXT_ID, type='text')]
children += utils.br(2)

"""
WorkRecord = '【作業実績】合計実動時間[{}]'

# テーブルで指定できるようにする
DailyRule : Remark = [
    '【作業実績】',
    '【問題点・懸念点・不明点など】',
    '【不在予定】',
    '【月末時点の業務時間】'
]
Matter : CommentItem = [
    '状況）',
    '原因）',
    '対策）',
    '備考）',
    ]

    ChapterRules = [
        '●',
        '■',
        '・',
    ]
]
"""

children += utils.param_label('Fooder String', '日報メールに記載するフッダー文章を指定する。（よろしくお願いします… の部分の文章）')
children += [dcc.Input(value='', id=FOODER_TEXT_ID, type='text')]
children += utils.br(2)

children += utils.param_label('EOM String', '日報メールの前日と前々日を分割するために使用する文字列を指定する。フッダーに仕込んでおいた区切り文字列をここに記載するような使い方を想定している。（ただ特に問題なければ [From:]のまま使用する）')
children += [dcc.Input(value='From:', type='text')]
children += utils.br(2)

children += utils.param_title_label('Add Last Mail Contents')
children += [dcc.Checklist(
                options=[{'label': '前日日報メールの内容を転記するかのフラグ。', 'value': 1}],
                value=[1],
                className="param-desc-label"
            )]
children += utils.br()

children += utils.param_label('Search Last EMail Folder', '前日メールを探索する試行回数を指定します。')
children += [dcc.Input(value='', type='text')]
children += utils.br(2)

children += utils.param_label('Search Last EMail Iteration', '前日メールを探索する試行回数を指定します。')
children += [dcc.Input(value='', type='text')]
children += utils.br(2)

children += utils.param_label('To/Cc EMail Address', '日報メールの宛先を指定する。')
children += [dcc.Input(value='', type='text')]
children += utils.br(2)


layout = html.Div([
    menu_tree.layout,
    html.Div(children=children, style={'padding': 10, 'flex': 4})
], style={'display': 'flex', 'flex-direction': 'row'})
