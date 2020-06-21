import dash
import random

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from navbar import Navbar
from application import app

nav = Navbar()

body = dbc.Container(
    [
        dbc.Col(
            [
                html.P("We live in a world of so much information. Our little blue marble is a sea of data. \
                        We measure and document everything:", style={"display": "inline"}),
                html.Span(
                       className="homePage_text", id='live-update-text'),
                dcc.Interval(
                    id='interval-component',
                    interval=2 * 1000,  # in milliseconds
                    n_intervals=0
                ),
                html.Img(src="assets/SU_Earth.png"),
                html.P("All of this data tells a story. Powerful tools exist to navigate these seas. \
                        IDE and Dashboards exist as the schooners, boats, and ships that allow us to set sail. \
                        Machine learning can see the squalls coming to avoid them. The only thing left is the crew and \
                        the destination.",
                       className="homePage_text"),
                html.Br(),
                html.P("So this is my small vessel venturing into the great unknown. \
                        Take a look where I have been and maybe help me find where I am going.",
                       className="homePage_text")
            ],
            # className="homePage_img_container"
        ),
    ]
)
dictionary_of_urls = {"This stuff": "here", "earth": "saturn", "moon": "Aliens are attacking us"}


# Updating something on an interval

@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_links(n):
    dataset, urls = random.choice(list(dictionary_of_urls.items()))
    return html.Span("from the earliest sounds on a wax cylinder <sub>subscript</sub>, \
                        the futures of the Dow Jones, to our current heart rates. This is a fact.")

def Homepage():
    layout = html.Div([
        nav,
        body,
    ], className="main")
    return layout
