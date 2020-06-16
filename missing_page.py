import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import base64

# from dash.dependencies import Output, Input

from navbar import Navbar

nav = Navbar()

# image_filename = 'assets/construction.png'  # replace with your own image
# encoded_image = base64.b64encode(open(image_filename, 'rb').read())

background = html.Div([
        html.H2("404",className="fourOhfour"),
        dbc.NavLink("Home", href="/about",className="homeButton"),
        ]
)

def missing_page():
    layout = html.Div([
        background,
        ],
        className = "bgSizing",
    )
    return layout
