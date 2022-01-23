from dash import dcc
from dash import html


PARAM_TITLE_LABEL_CLASS = 'param-title-label'
PARAM_DESC_LABEL_CLASS = 'param-desc-label'

PAGE_LAYOUT_CLASS = 'page-layout'


class ParamLayout:

    def __init__(self):
        pass

    def __create_input_layout(self, id, param):
        children = [html.Label(param['name'], className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        for desc in param['descs']:
            children += [html.Label(desc, className=PARAM_DESC_LABEL_CLASS), html.Br()]
        
        children += [dcc.Input(value=param['value'], id=id, type='text')]
        children += [html.Br()] * 2
        return children
    
    def __create_checkbox_layout(self, id, param):
        children = [html.Label(param['name'], className=PARAM_TITLE_LABEL_CLASS), html.Br()]
        children += [dcc.Checklist(
            options=param['options'],
            value=param['value'],
            id=id,
            className=PARAM_DESC_LABEL_CLASS
        )]
        children += [html.Br()]
        return children

    def create_param_layout(self, param_dict):
        children = []
        for key, value in param_dict.items():
            if value['type'] == 'input':
                children += self.__create_input_layout(key, value)
            elif value['type'] == 'checkbox':
                children += self.__create_checkbox_layout(key, value)
        return children


class PageLayout:

    def __init__(self):
        pass

    def create_page_layout(self, children):
        layout = html.Div(children=children, className=PAGE_LAYOUT_CLASS)
        return layout
