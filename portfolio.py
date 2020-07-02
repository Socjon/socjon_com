import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from navbar import Navbar

nav = Navbar()







card_one = html.Div([
        html.Div(
            [
                html.H3("SPRING FEVER"),
                html.Div("Yllamco laboris nisi ut aliquip ex ea commodo.", className="intro"),
            ], className="title-content"),
        html.Div([html.H4("Lorem ipsum dolor sit amet, consectetur adipisicing elit, \
                          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim.")],
                className="card-info"),
        html.Div(
            [
                html.Ul(
                    [
                        html.Li("12", className="comments"),
                        html.Li("03.12.2015", className="date"),
                    ], className="utility-list"),
            ], className = "utility-info"),
        html.Div(className="gradient-overlay"),
        html.Div(className="color-overlay"),
    ], className = "blog-card spring-fever"
)

def Portfolio():
    layout = html.Div([
            nav,
            card_one,
        ], className="main"
    )
    return layout


