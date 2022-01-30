import yaml
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

from app import app

from setting import PAGE_DESC_LABEL_CLASS

from setting import PARAM_TITLE_LABEL_CLASS
from setting import PARAM_DESC_LABEL_CLASS
from setting import PARAM_INPUT_TEXT_CLASS
from setting import PAGE_LAYOUT_CLASS

from setting import SET_USER_DIALOG_ID
from setting import SET_USER_RNAME_TEXT_ID
from setting import SET_USER_ADDRESS_TEXT_ID
from setting import SET_USER_EXCEL_PATH_TEXT_ID
from setting import SET_USER_DAILT_SHEET_TEXT_ID
from setting import SET_USER_MASTER_SHEET_TEXT_ID

from setting import SET_USER_PARAM_ID_ARGS

from setting import USER_CONFIG_PATH
from setting import USER_CONFIG


"""
Layout Class
"""
class SettingUser:

    PATHNAME = '/setting_user'

    @staticmethod
    def create_layout():
        children = []
        children += [html.Label('', id='setting-user-dummy-id')]
        children += [dcc.ConfirmDialog(
                        id=SET_USER_DIALOG_ID,
                        message='パラメータが変更されています。保存しますか？'
                    )]
        children += [html.H3('Setting User Param')]
        children += [html.Label('ユーザ情報と日報エクセルのパラメータ情報を設定するページです。', className=PAGE_DESC_LABEL_CLASS), html.Br()]
        children += [dcc.Markdown('''---''')]
        children += [html.Br()]
        
        # User Name
        children += [html.Label('User Name', className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [html.Label('日報メールに使用する名前を設定します。（特にこだわりがなければ名字を記入）', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [dcc.Input(id=SET_USER_RNAME_TEXT_ID,
                               value=USER_CONFIG[SET_USER_RNAME_TEXT_ID],
                               className=PARAM_INPUT_TEXT_CLASS,
                               type='text')]
        children += [html.Br()] * 2

        # Email address
        children += [html.Label('Email address', className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [html.Label('自身のOutlookのメールアドレスを設定します。', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [dcc.Input(id=SET_USER_ADDRESS_TEXT_ID,
                               value=USER_CONFIG[SET_USER_ADDRESS_TEXT_ID],
                               className=PARAM_INPUT_TEXT_CLASS,
                               type='text')]
        children += [html.Br()] * 2

        # Daily Excel File
        children += [html.Label('Daily Excel File', className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [html.Label('読み込む日報エクセルのPathを設定します。', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [dcc.Input(id=SET_USER_EXCEL_PATH_TEXT_ID,
                               value=USER_CONFIG[SET_USER_EXCEL_PATH_TEXT_ID],
                               className=PARAM_INPUT_TEXT_CLASS,
                               type='text')]
        children += [html.Br()] * 2

        # Daily Sheet Name
        children += [html.Label('Daily Sheet Name', className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [html.Label('読み込む日報エクセルの日次シート名を設定します。', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [dcc.Input(id=SET_USER_DAILT_SHEET_TEXT_ID,
                               value=USER_CONFIG[SET_USER_DAILT_SHEET_TEXT_ID],
                               className=PARAM_INPUT_TEXT_CLASS,
                               type='text')]
        children += [html.Br()] * 2

        # Master Sheet Name
        children += [html.Label('Master Sheet Name', className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [html.Label('読み込む日報エクセルのマスタシート名を設定します。', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [dcc.Input(id=SET_USER_MASTER_SHEET_TEXT_ID,
                               value=USER_CONFIG[SET_USER_MASTER_SHEET_TEXT_ID],
                               className=PARAM_INPUT_TEXT_CLASS,
                               type='text')]
        children += [html.Br()] * 2

        layout = html.Div(children=children, className=PAGE_LAYOUT_CLASS)
        return layout


"""
Callback Function
"""
# Global Variables
edit_user_config = None


# Create Callback Function
@app.callback(
    Output(SET_USER_DIALOG_ID, 'displayed'),
    Input('url', 'pathname'),
    [State(arg[0], arg[1]) for arg in SET_USER_PARAM_ID_ARGS]
)
def dislpay_dialog(pathname, *value):
    global edit_user_config
    edit_user_config = {arg[0]:v for arg, v in zip(SET_USER_PARAM_ID_ARGS, value)}
    if edit_user_config != USER_CONFIG:
        return True


@app.callback(
    Output('setting-user-dummy-id', 'children'),
    Input(SET_USER_DIALOG_ID, 'submit_n_clicks'),
)
def update_param(submit_n_clicks):
    global edit_user_config
    if submit_n_clicks:
        for k, v in edit_user_config.items():
            USER_CONFIG[k] = v
        
        with open(USER_CONFIG_PATH, 'w', encoding='utf-8') as f:
            yaml.dump(USER_CONFIG, f, indent=4, allow_unicode=True)
    
    return ''
