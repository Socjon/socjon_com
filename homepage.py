import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar

nav = Navbar()

body = dbc.Container(
    [
                dbc.Col(
                    [
                        html.P("We live in a world of so much information. Our little blue marble is a sea of data. \
                        We measure and document everything: from the earliest sounds on a wax cylinder <sub>subscript</sub>, \
                        the futures of the Dow Jones, to our current heart rates. This is a fact.",
                               className="homePage_text"),
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

def Homepage():
    layout = html.Div([
        nav,
        body,
    ], className="main")
    return layout