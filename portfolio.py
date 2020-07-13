import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from navbar import Navbar

nav = Navbar()


card_auditor = dbc.Container([
            html.Div(
            [
                html.H3("AuditorsAid"),
                html.Div("Yllamco laboris nisi ut aliquip ex ea commodo.", className="intro"),
            ], className="title-content"),
        html.Div([html.H4("Lorem ipsum dolor sit amet, consectetur adipisicing elit, \
                          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim.")],
                className="card-info"),
        html.Div(className="gradient-overlay"),
        html.Div(className="color-overlay"),
    ], className = "blog-card auditor-card"
)

card_socjon = dbc.Container([
        html.Div(
            [
                html.H3("AuditorsAid"),
                html.Div("Yllamco laboris nisi ut aliquip ex ea commodo.", className="intro"),
            ], className="title-content"),
        html.Div([html.H4("Lorem ipsum dolor sit amet, consectetur adipisicing elit, \
                          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim.")],
                className="card-info"),
        html.Div(className="gradient-overlay"),
        html.Div(className="color-overlay"),
    ], className = "blog-card socjon-card"
)



card_TBD = dbc.Container([
        html.Div(
            [
                html.H3("Something exciting"),
                html.Div("Digital Art? A new analysis.", className="intro"),
            ], className="title-content"),
        html.Div([html.H4("New content as soon as it is completed.")],
                className="card-info"),
        html.Div(className="gradient-overlay"),
        html.Div(className="color-overlay"),
    ], className = "blog-card TBD-card"
)

def Portfolio():
    layout = html.Div([
            nav,
            card_auditor,
            card_socjon,
            card_TBD
        ], className="main"
    )
    return layout


