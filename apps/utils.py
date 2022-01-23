import dash_html_components as html


def param_label(title, desc):

    children = []
    children += param_title_label(title)
    children += param_desc_label(desc)
    return children

def param_title_label(title):
    children = [html.Label(title, className="param-title-label"),
                html.Br()]
    return children

def param_desc_label(desc):
    children = [html.Label(desc, className="param-desc-label"),
                html.Br()]
    return children

def br(number=1):
    return [html.Br()] * number