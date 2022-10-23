from enum import auto
from dash import html
from sympy import sec
import navigation
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/about', title="About", description="Drone Infrastructure Research Technology")

image_pixil = 'static/pixil-frame-0.png'

first_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Brandon", className="card-title"),
            html.P("Brandon is a second year Masters of Analytics Student at Georgia Institute of Technology."),
        ]
    ),
    outline=False,
    inverse=True
)


second_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Sena", className="card-title"),
            html.P(
                "Sena is a second year Computer Science student at Georgia Institute of Technology. She is pursuing Intelligence and Media threads and she is very interested in the development of video games. In her free time, she likes to animate and create digital art."
            ),
        ]
    ), 
    outline=False,
    inverse=True
)

third_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Karpagam", className="card-title"),
            html.P(
                "Karpagam is a first year Computer Science student at Georgia Institute of Technology. She is pursuing the Intelligence and Theory threads and has a strong interest in the field of cybersecurity. Her hobbies include reading, running, and playing violin."
            ),
        ]
    ),
    outline=False,
    inverse=True
)

forth_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Carina", className="card-title"),
            html.P(
                "Carina is a third year Computer Science student at Georgia Institute of Technology. She is pursuing the Devices and Intelligence threads with an interest in robotics and AI. Some of her hobbies include working out and playing video games."
            ),
        ]
    ), 
    outline=False,
    inverse=True
)

card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("About us!", className="card-title", style={"padding": "10px"}),
                html.P("This is Drone Infrastructure Research Technology, otherwise known as DIRT.Our project is based around using a drone to scan infrastructure for cracks and damage"),
                html.Ul([
                    html.Li("Camera that scans infrastructure for cracks and damage"),
                    html.Li("Makes it easier for workers to identify faults in buildings so that they don’t have to be up there just looking for damage"),
                    html.Li("Civil engineers can use it to be more productive")
                ]),
                html.H5("Meet the team!"),
                html.Br(),
                dbc.Row([
                        dbc.Col(first_card, width="3"),
                        dbc.Col(second_card, width="3"),
                        dbc.Col(third_card, width="3"),
                        dbc.Col(forth_card, width="3"),
                ]),
                
            ], style={"padding": "20px"}
        ),
    ], class_name="g-0 d-flex align-items-center", 
    style={"align-items": "center", "justify-content": "center", "margin-left": "20%", "margin-right": "20%", "margin-top": "1%"},
    color="success", 
    outline=True,
    inverse=True
)


layout = html.Div(children=[
    navigation.navbar,
    html.Div([
        html.Img(src=image_pixil, height="300px"),
    ],  style={"text_align": "center", "align-items": "center", "justify-content": "center", "margin-left": "40%", "margin-right": "40%"}),
    card,
    


])