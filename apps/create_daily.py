from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from datetime import datetime
from dateutil.relativedelta import relativedelta

from app import app

from setting import DAILY_TEXTAREA_CLASS
from setting import DAILY_CREATE_BUTTON_CLASS
from setting import DAILY_SEND_BUTTON_CLASS
from setting import PAGE_LAYOUT_CLASS

from setting import DAILY_TEXT_AREA_ID
from setting import DAILY_CREATE_BUTTON_ID
from setting import DAILY_SEND_BUTTON_ID



class CreateDaily:
    
    PATHNAME = '/create_daily'

    @staticmethod
    def create_layout():
        children = []
        children += [html.Label('', id='create-daily-dummy-id')]
        children += [html.H3('Create Daily EMail')]
        children += [dcc.Markdown('''---''')]

        now_date = datetime.now()
        min_date = now_date + relativedelta(year=now_date.year - 1)

        # Add Calender Layout 
        children += [dcc.DatePickerSingle(
                        display_format='YYYY/MM/DD',
                        first_day_of_week=1,
                        min_date_allowed=min_date.date(),
                        max_date_allowed=now_date.date(),
                        initial_visible_month=now_date.date(),
                        date=now_date.date()
                    )]
        children += [html.Button('Create Daily',
                                 id=DAILY_CREATE_BUTTON_ID,
                                 className=DAILY_CREATE_BUTTON_CLASS)]
        children += [html.Br()] * 2

        # Daily Text and Submit Button Layout
        children += [dcc.Textarea(id=DAILY_TEXT_AREA_ID,
                                  value='',
                                  className=DAILY_TEXTAREA_CLASS)]
        children += [html.Br()]
        children += [html.Button('Send',
                                 id=DAILY_SEND_BUTTON_ID,
                                 className=DAILY_SEND_BUTTON_CLASS)]

        layout = html.Div(children=children, className=PAGE_LAYOUT_CLASS)
        return layout


@app.callback(
    Output(DAILY_TEXT_AREA_ID, 'value'),
    Input(DAILY_CREATE_BUTTON_ID, 'n_clicks')
)
def create_daily_text(n_clicks):
    if n_clicks:
        message = 'comming soon'
        return message

@app.callback(
    Output('create-daily-dummy-id', 'children'),
    Input(DAILY_SEND_BUTTON_ID, 'n_clicks')
)
def send_daily_mail(n_clicks):
    if n_clicks:
        print('click [DAILY_SEND_BUTTON]')
    return ''
