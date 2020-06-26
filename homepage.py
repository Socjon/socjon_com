import dash
import random
import ast

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
                dbc.Container(
                    [
                        html.P("We live in a world of so much information. Our little blue marble is a sea of data. \
                        We measure and document everything: ", style={"display": "inline"}),
                        html.Span(
                            id='live-update-text'),
                        dcc.Interval(
                            id='interval-component',
                            interval=8 * 1000,  # in milliseconds
                            n_intervals=0
                        )
                    ], className="homeTopText_container"
                ),
                html.Div(
                    [
                        html.Img(src="assets/SU_Earth.png", className="img")
                    ],
                        className="earth_container"
                        ),
                dbc.Container(
                    [
                        html.P("All of this data tells a story. Powerful tools exist to navigate these seas. \
                            IDE and Dashboards exist as the schooners, boats, and ships that allow us to set sail. \
                            Machine learning can see the squalls coming to avoid them. The only thing left is the crew and \
                            the destination."),
                        html.Br(),
                        html.P("So this is my small vessel venturing into the great unknown. \
                            Take a look where I have been and maybe help me find where I am going.")

                    ],
                    className="homeBotText_container"
                ),
            ],
        ),
    ],
    className="homePage_background"
)


# Importing the dict from asset folder. Unsure it runs needlessly when updating so commenting it out for now.
# with open("assets/URL_dict.txt", "r") as data:
#     dictionary_of_urls = ast.literal_eval(data.read())
#     data.close()

dictionary_of_urls = {"penguin populations": "http://www.penguinmap.com/mapppd",
                      "stereotype bias in language models": "https://stereoset.mit.edu/",
                      "uniform geographic name usage throughout the Federal Government": "http://geonames.usgs.gov/index.html",
                      'public support for political executives': 'http://www.executiveapproval.org/',
                      'a library of case studies around telecommunications policy': 'https://a4ai.org/who-we-are/',
                      'how couples meet and stay together': 'https://data.stanford.edu/hcmst',
                      'species-level functional trait database of palms': 'https://www.nature.com/articles/s41597-019-0189-0',
                      'speeches given by the European Central Bank': 'https://www.ecb.europa.eu/press/key/html/downloads.en.html',
                      'citation data from the National Institutes of Health': 'https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000385',
                      'State wise gun ownership': 'https://www.thetrace.org/',
                      "the world's broadcast, print, and web news": 'https://www.gdeltproject.org/',
                      'A database of sovereign debt for advanced and emerging countries over the period 1913–46': 'https://www.imf.org/en/Publications/WP/Issues/2019/10/25/Instruments-of-Debtstruction-A-New-Database-of-Interwar-Debt-48689',
                      'food flows between counties in the United States': 'https://iopscience.iop.org/article/10.1088/1748-9326/ab29ae',
                      'storehouse of rate structure information from utilities in the United States': 'https://openei.org/wiki/Utility_Rate_Database',
                      'US census data': 'https://www.census.gov/sipp/',
                      'passes, shots, fouls, etc in soccer matches': 'https://www.nature.com/articles/s41597-019-0247-7',
                      'squirrel population in NY Central Park': 'https://www.thesquirrelcensus.com/',
                      'field operations in UN Peacekeeping missons': 'https://peacekeeping.un.org/en/open-data-portal',
                      'earthquakes in Mexico from 1787 to 2018': 'https://www.nature.com/articles/s41597-019-0234-z',
                      'who is buying homes in Greece after the international financial crisis': 'https://medium.com/athenslivegr/whose-home-is-this-f3b45d878b0b',
                      'Certificates of Competency for the State Department employees': 'https://www.state.gov/resources-bureau-of-human-resources/',
                      'a survey of graduate students about the nature of doctoral research': 'https://www.nature.com/articles/d41586-019-03459-7',
                      'a databsae of British and Irish hills': 'http://www.hills-database.co.uk/index.html',
                      'active death penalty jurisdictions since 1976': 'https://theintercept.com/series/the-condemned/',
                      'International environmental agreements': 'https://iea.uoregon.edu/',
                      'typos gathered from github': 'https://github.com/mhagiwara/github-typo-corpus'}


# Updating something on an interval

@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_links(n):
    one, two, three = random.sample(list(dictionary_of_urls.keys()), 3)
    return html.Span([
        dcc.Link(one + ", ", href=dictionary_of_urls[one]),
        dcc.Link(two + ", ", href=dictionary_of_urls[two]),
        dcc.Link("and " + three + ".", href=dictionary_of_urls[three])])

def Homepage():
    layout = html.Div([
        nav,
        body,
    ])
    return layout
