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
                        html.H2("Yo, my name is on and i want to be...."),
                        html.P(
                            """\
                        Filler, FillerFillerFillerFillerFiller, Filler.."""
                        ),
                        dbc.Button("I am a button", color="secondary"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("Graph"),
                        dcc.Graph(
                            figure={"data": [{"x": [1, 2, 3], "y": [1, 10, 4]}]}
                        ),
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

