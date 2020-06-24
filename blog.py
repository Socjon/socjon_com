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
                    html.Ul(
                        [
                            dcc.Link("Part 1: What is Dash?", href="", className="comingSoon"),
                            dcc.Link("Part 2: Dash and Multipage Functionality", href="", className="comingSoon"),
                            dcc.Link("Part 3: Hosting your Dash app", href="", className="comingSoon"),
                        ]
                    )
                ]
            ),
            html.Div(
                [
                    html.H3("Python"),
                    html.Ul(
                        [
                            dcc.Link("ipywidgets Handler", href="https://medium.com/@socjon/ipywidgets-handler-quick-overview-c9b9246345d9?source=friends_link&sk=495817948770e5b32051cb04a31ffdd2"),
                            dcc.Link("missingno", href="https://medium.com/@socjon/missingno-convex-hulls-beb0537c663a?source=friends_link&sk=83991b617b2b44b3a95ac90f573d7730"),
                        ]
                    )
                ]
            ),
            html.Div(
                [
                    html.H3("Data Science"),
                    html.Ul(
                        [
                            dcc.Link("Overview — VGG16 and ResNet",href="https://medium.com/@socjon/tba-920219647404?source=friends_link&sk=1fa7480c0c509a8af576b18e86cb1980"),
                            dcc.Link("Big data on a small laptop (Python)",href="https://medium.com/@socjon/big-data-on-a-small-laptop-python-c5101ca873a7?source=friends_link&sk=e0f0319bc0b9b2ea49e51360869b20da"),
                            dcc.Link("SQL and Hypothesis testing",href="https://medium.com/@socjon/northwind-sql-and-hypothesis-testing-50523d51a99d?source=friends_link&sk=b57b8b812972f137c3f955f29f53bea6")
                        ]
                    )
                ]
            ),
            html.Div(
                [
                    html.H3("Potpourri"),
                    html.Ul(
                        [
                            dcc.Link("Regular Expressions — Basics and Tools",href="https://medium.com/@socjon/regular-expressions-basics-and-tools-a4001309fd99?source=friends_link&sk=dfba8594eda67fb22d5a3638aeec119a"),
                            dcc.Link("Time Series — a bit of context",href="https://medium.com/@socjon/where-time-series-come-from-45555a3f8bf8?source=friends_link&sk=10efd28ed0d15602b2a8334809e75eb9"),
                        ]
                    )
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


