import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from navbar import Navbar

nav = Navbar()


card_auditor = html.A(
        dbc.Container([
            html.Div(
                [
                    html.H3("AuditorsAid"),
                    html.Div("Leveraging machine learning to help the IRS.", className="intro"),
                ], className="title-content"),
            html.Div(
                [
                    html.H4("A project to detect unusual behavior in Non-for-Profits 990 filings to the IRS.")
                ],className="card-info"),
            html.Div(className="gradient-overlay"),
            html.Div(className="color-overlay"),
                    ], className = "blog-card auditor-card"),
    href="https://github.com/Socjon/AuditorsAid#auditors-aid---anomaly-detection-in-not-for-profit-data"
)

card_socjon = dbc.NavLink(
        dbc.Container([
            html.Div(
                [
                    html.H3("Socjon.com"),
                    html.Div("This site, that you are on.", className="intro"),
                ], className="title-content"),
            html.Div(
                [
                    html.H4("A web-based application written with Dash, HTML, and CSS then hosted on AWS.")
                ],className="card-info"),
            html.Div(className="gradient-overlay"),
            html.Div(className="color-overlay"),
    ], className = "blog-card socjon-card"),
    href="/blog"
)



card_TBD = dbc.Container([
        html.Div(
            [
                html.H3("Something exciting"),
                html.Div("Digital Art? A new analysis?", className="intro"),
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
        ], className="main portfolio-page"
    )
    return layout