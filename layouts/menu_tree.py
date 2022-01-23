from dash import dcc
from dash import html

from layouts import dashboard, create_daily, setting_daily, setting_user


children = []
children += [html.H2('Daily Dashboard')]
children += [dcc.Markdown('''---''')]

children += [dcc.Link(html.Button('Show Dashboard', className='menu-tree-btn'), href=dashboard.PATHNAME)]
children += [html.Br()]
children += [dcc.Link(html.Button('Setting User Param', className='menu-tree-btn'), href=setting_user.PATHNAME)]
children += [html.Br()]
children += [dcc.Link(html.Button('Setting Daily Param', className='menu-tree-btn'), href=setting_daily.PATHNAME)]
children += [html.Br()]
children += [dcc.Link(html.Button('Create Daily EMail', className='menu-tree-btn'), href=create_daily.PATHNAME)]
children += [html.Br()]

layout = html.Div(children=children, className="menu-tree-layout")
