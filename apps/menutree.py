from dash import dcc
from dash import html

from apps.dashboard import Dashboard
from apps.setting_daily import SettingDaily
from apps.setting_user import SettingUser
from apps.create_daily import CreateDaily

from setting import MENU_TREE_BUTTON_CLASS
from setting import MENU_TREE_LAYOUT_CLASS


class Menutree:

    @staticmethod
    def create_layout():
        children = []
        children += [html.H2('Daily Dashboard')]
        children += [dcc.Markdown('''---''')]

        children += [dcc.Link(html.Button('Show Dashboard', className=MENU_TREE_BUTTON_CLASS), href=Dashboard.PATHNAME)]
        children += [html.Br()]
        children += [dcc.Link(html.Button('Setting User Param', className=MENU_TREE_BUTTON_CLASS), href=SettingUser.PATHNAME)]
        children += [html.Br()]
        children += [dcc.Link(html.Button('Setting Daily Param', className=MENU_TREE_BUTTON_CLASS), href=SettingDaily.PATHNAME)]
        children += [html.Br()]
        children += [dcc.Link(html.Button('Create Daily EMail', className=MENU_TREE_BUTTON_CLASS), href=CreateDaily.PATHNAME)]
        children += [html.Br()]

        layout = html.Div(children=children, className=MENU_TREE_LAYOUT_CLASS)
        return layout
