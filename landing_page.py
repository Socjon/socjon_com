import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import base64

from navbar import Navbar

nav = Navbar()

welcome = html.Div(
        [
            html.Div(
                    [
                        html.H1("I am Jon Tyler"),
                        html.P("And I am a Data Scientist"),
                        dbc.NavLink("Home", href="/about", className="homeButton")
                    ],
            className="welcome_text"
            )
        ],
    className="welcome_img")

# body = dbc.Container(
#     [
#         dbc.Row(
#             [
#                 dbc.Col(
#                     [
#                         html.H2("Jon Tyler - Employable"),
#                         html.P(
#                             """\
#                         I have a genuine passion for numbers, conceptualizing, and data science. I want to develop my skill set so I don’t “just have a job” but instead can go and pursue a career with like minded teams that are making a positive impact on the world. Socially Distant but always available at Jonctyler@gmail.com. """
#                         ),
#                         dbc.Button("I am a button", color="secondary")
#                     ],
#                     md=4,
#                 ),
#                 dbc.Col(
#                     [
#                         html.H2("Graph"),
#                         html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())
#                     #                        dcc.Graph(
# #                            figure={"data": [{"x": [1, 2, 3], "y": [1, 10, 4]}]}
#                         ),
#                     ],
#                 ),
#             ]
#         )
#     ],
#     className="mt-4",
# )


def landing_page():
    layout = html.Div([
        welcome,
    ])
    return layout



