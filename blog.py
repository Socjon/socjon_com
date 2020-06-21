import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from navbar import Navbar

nav = Navbar()

topics = html.Div(
    [
        html.Div(
                [
                    html.H3("Dashboards"),
                ]
            ),
            html.Div(
                [
                    html.H3("Python"),
                ]
            ),
            html.Div(
                [
                    html.H3("Data Science"),
                ]
            ),
            html.Div(
                [
                    html.H3("Potpourri"),
                ],
            )
    ]
)

def Blog():
    layout = html.Div([
            nav,
            topics,
        ], className="main"
    )
    return layout


