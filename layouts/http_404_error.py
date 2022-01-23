from dash import html


def create_layout():
    children = []
    children += [html.H1('404 ERROR Page Not Found')]
    children += [html.Label('アクセスしようとしたページが見つかりませんでした。')]
    
    layout = html.Div(children=children, className="page-layout")
    return layout
