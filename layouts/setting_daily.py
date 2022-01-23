from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

from app import app
from layouts.common.create_layout import ParamLayout, PageLayout

from apps import parameter


# HTML Path Name
PATHNAME = '/setting_daily'

def create_layout(init_value_dict):
    # Custom Parameter Layout
    param_layout_dict = {
        'subject-text': {
            'type': 'input',
            'name': 'Subject String',
            'descs': ['日報メールの件名を指定する。']
        },
        'header-text': {
            'type': 'input',
            'name': 'Header String',
            'descs': ['日報メールに記載するヘッダー文章を指定する。（○○さん お疲れ様です… の部分の文章）']
        },
        'fooder-text': {
            'type': 'input',
            'name': 'Fooder String',
            'descs': ['日報メールに記載するフッダー文章を指定する。（よろしくお願いします… の部分の文章）']
        },
        'eom-text': {
            'type': 'input',
            'name': 'EOM String',
            'descs': ['日報メールの前日と前々日を分割するために使用する文字列を指定する。',
                    'フッダーに仕込んでおいた区切り文字列をここに記載するような使い方を想定している。',
                    '（ただ特に問題なければ [From:]のまま使用する']
        },
        'add-last-mail-flag': {
            'type'   : 'checkbox',
            'name'   : 'Add Last Mail Contents',
            'options': [{'label': '前日日報メールの内容を転記するかのフラグ。', 'value': 'enable'}]
        },
        'email-folder-text': {
            'type': 'input',
            'name': 'Search Last EMail Folder',
            'descs': ['前日メールを探索する試行回数を指定します。']
        },
        'search-last-email-iter': {
            'type': 'input',
            'name': 'Search Last EMail Iteration',
            'descs': ['前日メールを探索する試行回数を指定します。']
        },
        'send-email-address': {
            'type': 'input',
            'name': 'To/Cc EMail Address',
            'descs': ['日報メールの宛先を指定する。']
        }
    }

    # Set Init Value
    for k, v in init_value_dict.items():
        param_layout_dict[k]['value'] = v


    # Create Parameter Layout
    param_layout_obj = ParamLayout()
    page_layout_obj = PageLayout()

    children = []
    children += [html.Label('', id='daily-dummy')]
    children += [dcc.ConfirmDialog(
                    id='daily-save-dialog',
                    message='パラメータが変更されています。保存しますか？'
                )]
    children += [html.H3('Setting Daily Param')]
    children += [html.Label('日報作成に必要なパラメータ情報を設定するページです。'), html.Br()]
    children += [html.Label('文字列指定のパラメータでは下記の中括弧付き変数を指定できます。'), html.Br()]
    children += [html.Label('{name} : 名前、 {day} : 月日、 {work_time} : 業務時間'), html.Br()]
    children += [dcc.Markdown('''---''')]
    children += [html.Br()]
    children += param_layout_obj.create_param_layout(param_layout_dict)

    layout = page_layout_obj.create_page_layout(children)
    return layout


# Global Variables
daily_param_dict = None


# Create Callback Function
@app.callback(
    Output('daily-save-dialog', 'displayed'),
    Input('url', 'pathname'),
    [State(id, 'value') for id in parameter.DAILY_PARAM_DICT.keys()]
)
def dislpay_dialog(pathname, *value):
    global daily_param_dict
    daily_param_dict = {k:v for k, v in zip(parameter.DAILY_PARAM_DICT.keys(), value)}
    if daily_param_dict != parameter.DAILY_PARAM_DICT:
        return True


@app.callback(
    Output('daily-dummy', 'children'),
    Input('daily-save-dialog', 'submit_n_clicks'),
)
def update_param(submit_n_clicks):
    global daily_param_dict
    if submit_n_clicks:
        for k, v in daily_param_dict.items():
            parameter.DAILY_PARAM_DICT[k] = v
        parameter.save_daily_param()
        return ''


# TODO:後で追加すべきパラメータ
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