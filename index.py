from time import time

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Individual pages
from homepage import Homepage
from about import About
from blog import Blog
from auditor import Auditor

# Pages that didn't make it
# from missing_page import missing_page
# from time_series import graph_page, build_graph
# from landing_page import Landing_page

external_stylesheets = [dbc.themes.CYBORG, '/assets/background.css']

application = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app = application

# app.enable_dev_tools(dev_tools_hot_reload=True)

# app.scripts.config.serve_locally = True
# app.css.config.serve_locally = True
app.config.suppress_callback_exceptions = True



app.layout = html.Div([
    dcc.Location(id = 'url',refresh = False),
    html.Div(id = 'page-content')
])

#Navigation callbacks
@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/about':
        return About()
    if pathname == '/blog':
        return Blog()
    # if pathname == '/projects':
    #     return graph_page()
    if pathname == '/auditor':
        return Auditor()
    if pathname == '/home':
        return Homepage()
    else:
        return Homepage()

# @app.callback(
#     Output('output', 'children'),
#     [Input('pop_dropdown', 'value')]
# )
#
# def update_graph(city):
#     graph = build_graph(city)
#     #Graph update
#     return graph

# Beanstalk looks for application by default, if this isn't set you will get a WSGI error.
application = app.server

if __name__ == '__main__':
    application.run(debug=True)