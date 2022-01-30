import yaml
from dash import dcc
from dash import html
from dash import dash_table
from dash.dependencies import Input, Output, State

from app import app

from setting import PAGE_DESC_LABEL_CLASS
from setting import PAGE_LAYOUT_CLASS

from setting import PARAM_TITLE_LABEL_CLASS
from setting import PARAM_DESC_LABEL_CLASS
from setting import PARAM_INPUT_TEXT_CLASS
from setting import PARAM_INPUT_NUMBER_CLASS
from setting import PARAM_TABLE_CLASS
from setting import PARAM_SINGLE_COLUMN_CLASS
from setting import PARAM_TABLE_ADD_BTN_CLASS

from setting import SET_DAILY_DIALOG_ID
from setting import SET_DAILY_CATEGORY_TABLE_ADD_BUTTON_ID
from setting import SET_DAILY_EMAIL_TABLE_ADD_BUTTON_ID
from setting import SET_DAILY_MATTER_ITEMS_TABLE_ADD_BUTTON_ID
from setting import SET_DAILY_SUBJECT_TEXT_ID
from setting import SET_DAILY_HEADER_TEXT_ID
from setting import SET_DAILY_FOOTER_TEXT_ID
from setting import SET_DAILY_EOM_TEXT_ID
from setting import SET_DAILY_CATEGORY_TABLE_ID
from setting import SET_DAILY_MATTER_ITEMS_TABLE_ID
from setting import SET_DAILY_CHAPTER_MARK_TABLE_ID
from setting import SET_DAILY_ADD_LAST_MAIL_CHECKBOX_ID
from setting import SET_DAILY_EMAIL_FOLDER_TEXT_ID
from setting import SET_DAILY_SEARCH_EMAIL_ITER_NUM_ID
from setting import SET_DAILY_SEND_EMAIL_TABLE_ID

from setting import SET_DAILY_PARAM_ID_ARGS

from setting import DAILY_CONFIG_PATH
from setting import DAILY_CONFIG


"""
Layout Class
"""
class SettingDaily:

    PATHNAME = '/setting_daily'

    @staticmethod
    def create_layout():
        children = []
        children += [html.Label('', id='setting-daily-dummy-id')]
        children += [dcc.ConfirmDialog(
                        id=SET_DAILY_DIALOG_ID,
                        message='パラメータが変更されています。保存しますか？'
                    )]
        children += [html.H3('Setting Daily Param')]
        children += [html.Label('日報作成に必要なパラメータ情報を設定するページです。', className=PAGE_DESC_LABEL_CLASS), html.Br()]
        children += [html.Label('文字列指定のパラメータでは下記の中括弧付き変数を指定できます。', className=PAGE_DESC_LABEL_CLASS), html.Br()]
        children += [html.Label('・{name} : 名前', className=PAGE_DESC_LABEL_CLASS), html.Br()]
        children += [html.Label('・{day} : 月日', className=PAGE_DESC_LABEL_CLASS), html.Br()]
        children += [dcc.Markdown('''---''')]
        children += [html.Br()]

        # Subject String
        children += [html.Label('Subject String', className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [html.Label('日報メールの件名を設定します。', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [dcc.Input(id=SET_DAILY_SUBJECT_TEXT_ID,
                               value=DAILY_CONFIG[SET_DAILY_SUBJECT_TEXT_ID],
                               className=PARAM_INPUT_TEXT_CLASS,
                               type='text')]
        children += [html.Br()] * 2

        # Header String
        children += [html.Label('Header String', className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [html.Label('日報メールに記載するヘッダー文章を設定します。（○○さん お疲れ様です… の部分の文章）', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [dcc.Input(id=SET_DAILY_HEADER_TEXT_ID,
                               value=DAILY_CONFIG[SET_DAILY_HEADER_TEXT_ID],
                               className=PARAM_INPUT_TEXT_CLASS,
                               type='text')]
        children += [html.Br()] * 2

        # Fooder String
        children += [html.Label('Footer String', className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [html.Label('日報メールに記載するフッター文章を設定します。（よろしくお願いします… の部分の文章）', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [dcc.Input(id=SET_DAILY_FOOTER_TEXT_ID,
                               value=DAILY_CONFIG[SET_DAILY_FOOTER_TEXT_ID],
                               className=PARAM_INPUT_TEXT_CLASS,
                               type='text')]
        children += [html.Br()] * 2

        # EOM String
        children += [html.Label('EOM String', className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [html.Label('日報メールの前日と前々日を分割するために使用する文字列を設定します。', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [html.Label('フッターに仕込んでおいた区切り文字列をここに記載するような使い方を想定しています。', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [html.Label('（ただ特に問題なければ [From:]のまま使用する', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [dcc.Input(id=SET_DAILY_EOM_TEXT_ID,
                               value=DAILY_CONFIG[SET_DAILY_EOM_TEXT_ID],
                               className=PARAM_INPUT_TEXT_CLASS,
                               type='text')]
        children += [html.Br()] * 2

        # Daily Mail Contents
        SET_DAILY_CATEGORY_TABLE_COL = [
            ['Name', 'input'],
            ['Type', 'dropdown']
        ]
        children += [html.Label('Daily Mail Categories', className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [html.Label('日報メールの構成(カテゴリ)を設定します。Typeは下記の通りです。', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [html.Label('・Matter : 案件の内容を記載するカテゴリ', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [html.Label('・Copy   : 前日の日報メールの内容を転記するカテゴリ', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [html.Label('・None   : 前日の日報メールの内容を転記しないカテゴリ', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [html.Div([
            dash_table.DataTable(
                id=SET_DAILY_CATEGORY_TABLE_ID,
                data=[
                    {key:value for key, value in data.items()}
                    for data in DAILY_CONFIG[SET_DAILY_CATEGORY_TABLE_ID]
                ],
                columns=[{
                    'id': col[0],
                    'name': col[0],
                    'presentation': col[1]
                } for col in SET_DAILY_CATEGORY_TABLE_COL],

                editable=True,
                row_deletable=True,
                dropdown={
                    'Type': {
                        'options': [
                            {'label': 'Matter', 'value': 'Matter'},
                            {'label': 'Copy', 'value': 'Copy'},
                            {'label': 'None', 'value': 'None'}
                        ]
                    }
                }
            )], className=PARAM_TABLE_CLASS
        )]
        children += [html.Button('Add Row',
                                 id=SET_DAILY_CATEGORY_TABLE_ADD_BUTTON_ID,
                                 className=PARAM_TABLE_ADD_BTN_CLASS,
                                 n_clicks=0)]
        children += [html.Br()] * 2

        # Matter Item Labels
        children += [html.Label('Matter Item Labels', className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [html.Label('案件カテゴリの構成する項目を設定します。', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [html.Div([
            dash_table.DataTable(
                id=SET_DAILY_MATTER_ITEMS_TABLE_ID,
                data=[
                    {key:value for key, value in data.items()}
                    for data in DAILY_CONFIG[SET_DAILY_MATTER_ITEMS_TABLE_ID]
                ],
                columns=[{'id': 'Item', 'name': 'Item'}],
                editable=True,
                row_deletable=True,
            )], className=PARAM_SINGLE_COLUMN_CLASS
        )]
        children += [html.Button('Add Row',
                                 id=SET_DAILY_MATTER_ITEMS_TABLE_ADD_BUTTON_ID,
                                 className=PARAM_TABLE_ADD_BTN_CLASS,
                                 n_clicks=0)]
        children += [html.Br()] * 2

        # Daily Chapter Marks
        SET_DAILY_CHAPTER_MARK_TABLE_COL = [
            ['Matter', 'input'],
            ['Class', 'input'],
            ['Task', 'input']
        ]
        children += [html.Label('Daily Chapter Marks', className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [html.Label('日報メールの章立てマークを設定します。', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [html.Div([
            dash_table.DataTable(
                id=SET_DAILY_CHAPTER_MARK_TABLE_ID,
                data=[
                    {key:value for key, value in data.items()}
                    for data in DAILY_CONFIG[SET_DAILY_CHAPTER_MARK_TABLE_ID]
                ],
                columns=[{
                    'id': col[0],
                    'name': col[0],
                    'presentation': col[1]
                } for col in SET_DAILY_CHAPTER_MARK_TABLE_COL],

                editable=True,
            )], className=PARAM_TABLE_CLASS
        )]
        children += [html.Br()]

        # Add Last Mail Body
        children += [html.Label('Add Last Mail Body', className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [dcc.Checklist(id=SET_DAILY_ADD_LAST_MAIL_CHECKBOX_ID,
                                   options=[
                                       {"label": "日報メール作成時、前日の日報メールの内容を末端に追加します。",
                                        "value": "enable"}],
                                   value=DAILY_CONFIG[SET_DAILY_ADD_LAST_MAIL_CHECKBOX_ID],
                                   className=PARAM_DESC_LABEL_CLASS)]
        children += [html.Br()]

        # Search Last EMail Folder
        children += [html.Label('Search Last EMail Folder', className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [html.Label('前日メールを探索するOutlookのフォルダを設定します。', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [dcc.Input(id=SET_DAILY_EMAIL_FOLDER_TEXT_ID,
                               value=DAILY_CONFIG[SET_DAILY_EMAIL_FOLDER_TEXT_ID],
                               className=PARAM_INPUT_TEXT_CLASS,
                               type='text')]
        children += [html.Br()] * 2

        # Search Last EMail Iteration
        children += [html.Label('Search Last EMail Iteration', className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [html.Label('前日メールを探索する試行回数を指定します。', className=PARAM_DESC_LABEL_CLASS), html.Br()]

        children += [dcc.Input(id=SET_DAILY_SEARCH_EMAIL_ITER_NUM_ID,
                               value=DAILY_CONFIG[SET_DAILY_SEARCH_EMAIL_ITER_NUM_ID],
                               className=PARAM_INPUT_NUMBER_CLASS,
                               type='number',
                               max=100,
                               min=1,
                               step=1)]
        children += [html.Br()] * 2

        # To/Cc EMail Address
        SET_DAILY_SEND_EMAIL_TABLE_COL = [
            ['Name', 'input'],
            ['Type', 'dropdown'],
            ['Address', 'input']
        ]
        children += [html.Label('To/Cc EMail Address', className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [html.Label('日報メールの宛先を指定します。', className=PARAM_DESC_LABEL_CLASS), html.Br()]
        children += [html.Div([
            dash_table.DataTable(
                id=SET_DAILY_SEND_EMAIL_TABLE_ID,
                data=[
                    {key:value for key, value in data.items()}
                    for data in DAILY_CONFIG[SET_DAILY_SEND_EMAIL_TABLE_ID]
                ],
                columns=[{
                    'id': col[0],
                    'name': col[0],
                    'presentation': col[1]
                } for col in SET_DAILY_SEND_EMAIL_TABLE_COL],

                editable=True,
                row_deletable=True,
                dropdown={
                    'Type': {
                        'options': [
                            {'label': 'To', 'value': 'To'},
                            {'label': 'Cc', 'value': 'Cc'}
                        ]
                    }
                }
            )], className=PARAM_TABLE_CLASS
        )]
        children += [html.Button('Add Row',
                                 id=SET_DAILY_EMAIL_TABLE_ADD_BUTTON_ID,
                                 className=PARAM_TABLE_ADD_BTN_CLASS,
                                 n_clicks=0)]
        children += [html.Br()] * 2
        
        layout = html.Div(children=children, className=PAGE_LAYOUT_CLASS)
        return layout


"""
Callback Function
"""
# Global Variables
edit_daily_config = None


# Create Callback Function
@app.callback(
    Output(SET_DAILY_DIALOG_ID, 'displayed'),
    Input('url', 'pathname'),
    [State(arg[0], arg[1]) for arg in SET_DAILY_PARAM_ID_ARGS]
)
def dislpay_dialog(pathname, *value):
    global edit_daily_config
    edit_daily_config = {arg[0]:v for arg, v in zip(SET_DAILY_PARAM_ID_ARGS, value)}
    if edit_daily_config != DAILY_CONFIG:
        return True


@app.callback(
    Output('setting-daily-dummy-id', 'children'),
    Input(SET_DAILY_DIALOG_ID, 'submit_n_clicks'),
)
def update_param(submit_n_clicks):
    global edit_daily_config
    if submit_n_clicks:
        for k, v in edit_daily_config.items():
            DAILY_CONFIG[k] = v

        with open(DAILY_CONFIG_PATH, 'w', encoding='utf-8') as f:
            yaml.dump(DAILY_CONFIG, f, indent=4, allow_unicode=True)
    return ''


@app.callback(
    Output(SET_DAILY_CATEGORY_TABLE_ID, 'data'),
    Input(SET_DAILY_CATEGORY_TABLE_ADD_BUTTON_ID, 'n_clicks'),
    State(SET_DAILY_CATEGORY_TABLE_ID, 'data'),
    State(SET_DAILY_CATEGORY_TABLE_ID, 'columns'))
def add_category_table_row(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows


@app.callback(
    Output(SET_DAILY_MATTER_ITEMS_TABLE_ID, 'data'),
    Input(SET_DAILY_MATTER_ITEMS_TABLE_ADD_BUTTON_ID, 'n_clicks'),
    State(SET_DAILY_MATTER_ITEMS_TABLE_ID, 'data'),
    State(SET_DAILY_MATTER_ITEMS_TABLE_ID, 'columns'))
def add_matter_item_table_row(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows


@app.callback(
    Output(SET_DAILY_SEND_EMAIL_TABLE_ID, 'data'),
    Input(SET_DAILY_EMAIL_TABLE_ADD_BUTTON_ID, 'n_clicks'),
    State(SET_DAILY_SEND_EMAIL_TABLE_ID, 'data'),
    State(SET_DAILY_SEND_EMAIL_TABLE_ID, 'columns'))
def add_email_table_row(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c['id']: '' for c in columns})
    return rows
