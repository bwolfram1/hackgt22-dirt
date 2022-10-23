import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
from dash_bootstrap_components._components.Container import Container


image_pixil = 'static/pixil-frame-0.png'

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("FAQ",  href="/faq")),
        dbc.NavItem(dbc.NavLink("About us", href="/about")),
        html.Img(src=image_pixil, height="40px", style={
            "margin-left": "20px",
            "margin-top": "5px",
            "padding-right": "-10px"
        }),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Profile", header=True),
                dbc.DropdownMenuItem("Logout", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="",
        ),
    ],
    brand="DIRT",
    brand_href="/",
    color="dark",
    dark=True,
)

navbar2 = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=image_pixil, height="30px")),
                        dbc.Col(dbc.NavbarBrand("D.I.R.T", className="ms-2")),
                        dbc.Col(
                            dbc.NavItem(dbc.NavLink(
                                "Dashboard", href="/"
                                ), 
                                className='text-white font-weight-bold'
                            )
                        , class_name="text-white"),
                        dbc.Col(dbc.NavLink("About", href="/about")),
                        dbc.Col(dbc.NavLink("FAQ", href="/faq")),
                        dbc.Col(dbc.NavLink("Profile", href="/profile"))
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                id="navbar-collapse",
                is_open=True,
                navbar=True,
            ),
        ]
    ),
    class_name="navbar-dark bg-dark text-white, navbar-expand-lg",
    color="dark",
    dark=True,
    style={
        
    }
)
@dash.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
