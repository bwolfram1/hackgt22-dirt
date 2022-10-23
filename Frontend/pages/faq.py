from dash import html
import navigation
import dash
import dash_bootstrap_components as dbc


dash.register_page(__name__, path='/faq', title="FAQ", description="Drone Infrastructure Research Technology")

card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Welcome to D.I.R.T. FAQ", className="card-title", style={"padding": "10px"}),
                dbc.ListGroup(
                    [
                        dbc.ListGroupItem(
                            html.Div([
                                html.H5("What is DIRT?"),
                                html.P("The primary goal of DIRT is to monitor infrastructure autonomously so the workers can focus on fixing the problems rather than surveying manually. This is done by attaching an autonomous drone to collect the necessary data.")
                                
                            ])
                        ),
                        dbc.ListGroupItem(
                            html.Div([
                                html.H5("Who uses DIRT?"),
                                html.P("DIRT is used by city civil engineers to assess the city’s structural support systems and overall condition of the organizational structures and facilities of the surrounding areas.")
                            ])
                        ),
                        dbc.ListGroupItem(
                            html.Div([
                                html.H5("How does DIRT work? "),
                                html.P("This is done through an edge camera system that can be attached to a drone to classify different issues with infrastructure such as cracks or serious rust in bridges and other large structures.")
                            ])
                        ),
                    ], 
                    flush=True,
                    class_name="w-100",
                )
            ]
        ),
    ], class_name="d-flex", 
    style={"align-items": "center", "justify-content": "center", "margin-left": "20%", "margin-right": "20%", "margin-top": "10%"},
    color="success", 
    outline=True,
    inverse=True
)

layout = html.Div(children=[
    navigation.navbar,
    card,

])