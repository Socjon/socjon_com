import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import base64

from navbar import Navbar

nav = Navbar()

welcome = html.Div(
        [
            html.Div(
                    [
                        html.H1("I am Jon Tyler"),
                        html.P("And I am a Data Scientist"),
                        dbc.NavLink("Home", href="/about", className="homeButton")
                    ],
            className="welcome_text"
            )
        ],
    className="welcome_img")

def Landing_page():
    layout = html.Div([
        welcome,
    ])
    return layout



