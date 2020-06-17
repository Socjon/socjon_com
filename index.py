import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from time_series import graph_page, build_graph
from landing_page import Landing_page
from homepage import Homepage
from about import About
from missing_page import missing_page


external_stylesheets = [dbc.themes.CYBORG, '/assets/background.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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
    if pathname == '/time-series':
        return graph_page()
    if pathname == '/projects':
        return graph_page()
    # if pathname == '/trial':
    #     return Homepage()
    if pathname == '/home':
        return Homepage()
    else:
        return missing_page()


#Go home button on 404
# @app.callback(
#     Output('page-content', 'children'),
#     [Input('goHome', 'n_clicks')]
# )

#Graph update
@app.callback(
    Output('output', 'children'),
    [Input('pop_dropdown', 'value')]
)

def update_graph(city):
    graph = build_graph(city)
    return graph

if __name__ == '__main__':
    app.run_server(debug=True)