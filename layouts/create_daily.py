import dash
from dash import dcc
from dash import html

from datetime import datetime
from dateutil.relativedelta import relativedelta


# HTML Path Name
PATHNAME = '/create_daily'


def create_layout():
    children = []
    children += [html.H3('Create Daily EMail')]
    children += [dcc.Markdown('''---''')]

    now_date = datetime.now()
    min_date = now_date + relativedelta(year=now_date.year - 1)

    # Add Calender Layout 
    children += [dcc.DatePickerSingle(
                    id='calender',
                    display_format='YYYY/MM/DD',
                    first_day_of_week=1,
                    min_date_allowed=min_date.date(),
                    max_date_allowed=now_date.date(),
                    initial_visible_month=now_date.date(),
                    date=now_date.date()
                )]
    children += [html.Button('Create Daily', className='create-daily-btn')]
    children += [html.Br()] * 2

    # Daily Text and Submit Button Layout
    children += [dash.html.Textarea('', className='daily-textarea')]
    children += [html.Br()]
    children += [html.Button('Submit', className='daily-submit-btn')]

    layout = html.Div(children=children, className="page-layout")
    return layout
