import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from navbar import Navbar

nav = Navbar()

def Portfolio():
    layout = html.Div([
            nav,
            topics,
        ], className="main"
    )
    return layout


