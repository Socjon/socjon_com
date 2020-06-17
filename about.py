import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar

nav = Navbar()

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            """\
                        I am a geek and dreamer. I watch science fiction movies and read science fiction books as much \
                        for the powerful narrative as I do for the possibilities. I’ve watched every Star Trek episode \
                        because I choose to believe with hard work and equality we can reach a new potential and be our \
                        best selves."""
                        ),
                        dbc.Button("I am a button", color="secondary"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("Graph"),
                    ],
                ),
            ]
        )
    ],
    className="mt-4",
)


def About():
    layout = html.Div([
        nav,
        body
    ])
    return layout

