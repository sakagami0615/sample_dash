import dash
import dash_core_components as dcc
import dash_html_components as html

from apps import utils


children = []
children += [html.H2('Daily dashboard GUI')]
children += [dcc.Markdown('''---''')]

children += [dcc.Link(html.Button('Show Dashboard', className='menu-tree-btn'), href="/dashboard")]
children += utils.br()
children += [dcc.Link(html.Button('Setting User Param', className='menu-tree-btn'), href="/setting_user")]
children += utils.br()
children += [dcc.Link(html.Button('Setting Daily Param', className='menu-tree-btn'), href="/setting_daily")]
children += utils.br()
children += [dcc.Link(html.Button('Create Daily EMail', className='menu-tree-btn'), href="/create_daily")]
children += utils.br()

layout = html.Div(children=children, style={'padding': 10, 'flex': 1})
