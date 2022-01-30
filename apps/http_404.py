from dash import html

from setting import PAGE_LAYOUT_CLASS


class Http404:

    @staticmethod
    def create_layout():
        children = []
        children += [html.H1('404 ERROR Page Not Found')]
        children += [html.Label('アクセスしようとしたページが見つかりませんでした。')]
        
        layout = html.Div(children=children, className=PAGE_LAYOUT_CLASS)
        return layout
