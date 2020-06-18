import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar

nav = Navbar()


welcome = html.Div(
    [
        html.H1("Welcome", className="welcomeHeader")
    ],
    className="welcomeBanner"
)

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            """
                        Looking for work. 
                        """
                        , className="homePage_text"),

                    ],
                    className="homePage_padding"
                ),
                dbc.Col(
                    [
                        html.Img(src="assets/nasa_shirt.jpeg", className="img")
                    ],
                    className="homePage_img_container"
                ),
            ]
        )
    ]
)

def Homepage():
    layout = html.Div([
        nav,
        welcome,
        body,
    ])
    return layout