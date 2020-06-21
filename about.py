import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar

nav = Navbar()

header = html.Div(
    [
        html.H2("About Me", style={"text-align": "center", "position": "absolute"}),
        # Photo by Vincentiu Solomon on Unsplash
    ],
    className="aboutHeader"
)

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                        "I am a geek and dreamer. I watch science fiction movies and read science fiction books as much \
                        for the powerful narrative as I do for the possibilities. I’ve watched every Star Trek episode \
                        because I choose to believe with hard work and equality we can reach a new potential and be our \
                        best selves.", className="Generaltext"),
                        html.P(
                        "I have a genuine passion for numbers, conceptualizing, and data science. I want to develop my \
                        skill set so I don’t “just have a job” but instead can go and pursue a career with like minded \
                        teams that are making a positive impact on the world. Socially Distant but always available at \
                        Jonctyler@gmail.com.", className="Generaltext"),
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

def About():
    layout = html.Div([
        nav,
        header,
        body
    ], className="main")
    return layout
