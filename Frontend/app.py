import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.CYBORG],
                suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div(children=[
    dash.page_container
])

# change to false for demo
if __name__ == "__main__":
    app.run_server(debug=False, port=8080)
