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
                        We measure and document everything: ", style={"display": "inline"}),
                html.Span(
                    id='live-update-text'),
                dcc.Interval(
                    id='interval-component',
                    interval=10 * 1000,  # in milliseconds
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
dictionary_of_urls = {"penguin populations": "http://www.penguinmap.com/mapppd",
                      "stereotype bias in language models": "https://stereoset.mit.edu/",
                      "uniform geographic name usage throughout the Federal Government": "http://geonames.usgs.gov/index.html"}


# Updating something on an interval

@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_links(n):
    one, two, three = random.sample(list(dictionary_of_urls.keys()), 3)
    return html.Span([
        dcc.Link(one + ", ", href=dictionary_of_urls[one]),
        dcc.Link(two + ", ", href=dictionary_of_urls[two]),
        dcc.Link("and " + three + ".", href=dictionary_of_urls[three])],style={"display": "inline"})

def Homepage():
    layout = html.Div([
        nav,
        body,
    ], className="main")
    return layout
