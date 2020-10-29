# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import simplejson as json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

with open("1.json") as json_file:
    temp = json.load(json_file, parse_float=Decimal)
    df = pd.json_normalize(temp['SearchResults'])
    
keep=['UniqueId','Specification.Title','Specification.Make.Value',
      'Seller.City','Specification.Color.Primary','Prices.SearchPrice',
      'Seller.DealerScore','Specification.Odometer','Specification.YearModel']

num = ['Prices.SearchPrice', 'Specification.Odometer', 'Specification.YearModel']

fig = px.bar(df, x="Seller.City", y="Prices.SearchPrice", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='WebMotors | Soma de Preços Carros Por Estado'),

    html.Div(children='''
        Essa aplicação tem como objetivo futuro analisar os dados colhidos via webscraping e armazenados no DynamoDb.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
