import dash
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.CYBORG, '/assets/background.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config.suppress_callback_exceptions = True

# application = app.server