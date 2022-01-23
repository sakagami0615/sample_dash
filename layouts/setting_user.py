from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

from app import app
from layouts.common.create_layout import ParamLayout, PageLayout

from apps import parameter


# HTML Path Name
PATHNAME = '/setting_user'

def create_layout(init_value_dict):
    # Custom Parameter Layout
    param_layout_dict = {
        'user-name-text': {
            'name': 'User Name',
            'descs': ['日報メールに使用する名前を指定する。（特にこだわりがなければ名字を記入）'],
            'type': 'input'
        },
        'email-address-text': {
            'name': 'Email address',
            'descs': ['自身のOutlookのメールアドレスを指定する。'],
            'type': 'input'
        },
        'excel-file-text': {
            'name': 'Daily Excel File',
            'descs': ['読み込む日報エクセルのPathを指定します。'],
            'type': 'input'
        },
        'excel-sheet-text': {
            'name': 'Daily Sheet Name',
            'descs': ['読み込む日報エクセルのシート名を指定します。'],
            'type': 'input'
        }
    }

    # Set Init Value
    for k, v in init_value_dict.items():
        param_layout_dict[k]['value'] = v


    # Create Parameter Layout
    param_layout_obj = ParamLayout()
    page_layout_obj = PageLayout()

    children = []
    children += [html.Label('', id='user-dummy')]
    children += [dcc.ConfirmDialog(
                    id='user-save-dialog',
                    message='パラメータが変更されています。保存しますか？'
                )]
    children += [html.H3('Setting User Param')]
    children += [html.Label('ユーザ情報と日報エクセルのパラメータ情報を設定するページです。'), html.Br()]
    children += [dcc.Markdown('''---''')]
    children += [html.Br()]
    children += param_layout_obj.create_param_layout(param_layout_dict)

    layout = page_layout_obj.create_page_layout(children)
    return layout


# Global Variables
user_param_dict = None


# Create Callback Function
@app.callback(
    Output('user-save-dialog', 'displayed'),
    Input('url', 'pathname'),
    [State(id, 'value') for id in parameter.USER_PARAM_DICT.keys()]
)
def dislpay_dialog(pathname, *value):
    global user_param_dict
    user_param_dict = {k:v for k, v in zip(parameter.USER_PARAM_DICT.keys(), value)}
    if user_param_dict != parameter.USER_PARAM_DICT:
        return True


@app.callback(
    Output('user-dummy', 'children'),
    Input('user-save-dialog', 'submit_n_clicks'),
)
def update_param(submit_n_clicks):
    global update_param_dict
    if submit_n_clicks:
        for k, v in user_param_dict.items():
            parameter.USER_PARAM_DICT[k] = v
        parameter.save_user_param()
        return ''
