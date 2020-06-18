import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar

nav = Navbar()

header = html.H2("Auditors Aid", style={"text-align": "center"})

body = dbc.Container(
    [
        html.P("Non-Profit organizations are required to self-identify their area of focus based on the type of work \
        the organization does. I created machine learning models to classify these subgroups based on their annual 990 \
        filings."),
        html.Img(src="assets/NTEE_classifcations.pdf"),
        html.P("The intent of the project was to identify inconsistencies within these subgroups. \
               This inturn would give the IRS auditors specific organizations to investigate and reduce fraud."),
        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        ),
        html.P("Given my current models, a year-over-year analysis of Non-Profits would flag any \
               inconsistencies at a 90% certainty in the 5th year of using this system. Historical reporting data of \
               Non-Profit organizations is required to bolster this claim.")

    ]
)

def Auditor():
    layout = html.Div([
        nav,
        header,
        body,
    ])
    return layout