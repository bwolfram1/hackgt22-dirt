from click import style
import dateutil
from matplotlib import markers
import navigation
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import pandas as pd
import plotly.express as px
from Adafruit_IO import Client
from dash_bootstrap_templates import load_figure_template

load_figure_template("slate")


dash.register_page(__name__, path='/', title="D.I.R.T.", description="Drone Infrastructure Research Technology")


ADAFRUIT_IO_USERNAME = "bwolfram1"
ADAFRUIT_IO_KEY = "aio_EOsJ05WNtHaudEGCtmrArBct2HRC"
token = "pk.eyJ1IjoiYndvbGZyYW0xIiwiYSI6ImNsOWtmd3BsczAyN3gzeG54ZXM5cmVseWoifQ.l5Hyu2E1IEqC1Fdhqkd1cQ"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

data = aio.data("cracks")
df = pd.DataFrame(columns=["date", "value", "lat", "long"])
for d in data:
    datep = (dateutil.parser.isoparse(d.created_at))
    df = df.append({"date": datep, "value": d.value, "lat": float(d.lat), "long": float(d.lon)}, ignore_index=True)


temptype = []
for dd in df["value"]:
    print(dd)
    if dd=="1":
        temptype.append("overpass")
    elif dd == "2":
        temptype.append("building")
    else:
        temptype.append("bridge")
df['type'] = temptype

dfsum = df["value"].value_counts()
dfsum.to_frame()

dfsum["type"] = ["overpass", " building", "bridge"]

random_x = [2, 5, 8, 10, 11, 12, 13]
names = ['4/20222', '5/2022', "6/2022", "7/2022", "8/2022", "9/2022", "10/2022"]
colors = {
    'pink': '#F084EA',
    'green': '#84F09A',
    'blue': '#38FFF3',
    'black': '#000000'
}

# Graph 1
hh = (850/2)-5
wh = hh+400
wh2 = wh
fig = px.scatter_mapbox(df, lat="lat", lon="long", hover_name="value", hover_data=["value", "type"],color="type", zoom=12, height=850)
fig.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.update_traces(marker={"size": 20, "colorscale": "darkmint"})
fig.update_layout(legend=dict(bgcolor ='black', x=0.01, y=0.99, yanchor="top", xanchor="left", font=dict(color="white"), borderwidth=8, bordercolor="black"))

# Graph 2
fig2 = px.line(x=names, y=random_x, height=hh, width=wh, template="plotly_dark", title="Cusum of arrivals")

# Graph 3
nnames = {'1':'buildings','2':'ramps','3':'bridges'}
df3 = px.data.tips()
fig3 = px.pie(df,names="type", values='value' , height=hh, width=wh2,  template="plotly_dark", hole=0.5, title="Composition of Infurstructure Issues")


def leftLayout():
    return dbc.Container([
        dbc.Row([
            dbc.Col([dcc.Graph(
                id='graph1',
                figure=fig
            ),

            ]), 
        ], align='center', style = {'border-radius': 10,}),
    ])


def rightLayout():
    return dbc.Container([
        dbc.Row([
            dbc.Row([
                dcc.Graph(
                    id='graph2',
                    figure=fig2
                )
            ]),
            dbc.Row([
                dcc.Graph(
                    id='graph3',
                    figure=fig3
                )
            ], class_name="py-3"
            ),
            ], align='center'),
    ])


def layout():
    return html.Div([
        navigation.navbar,
        dbc.Row([
            html.Br(),
            dbc.Col(leftLayout(), width=6, style={"height": "100%", "colors": "black", "margin": "1", }),
            html.Br(),
            dbc.Col(rightLayout(), width=5, style={"margin_top" :"50px"}),
        ]), 
        
    ])
