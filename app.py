"""
Contains web layout and server function. This is the main file.
"""

"""
importing relevant libraries
"""
from distutils.log import debug
import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt

"""
creating a dash instance
"""

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div(
                html.Div(
                    [
                        html.P("Stock Visualization and Prediction App", className="start"),
                        html.Div([
                            # stock code input
                        ]),
                        html.Div([
                            # Date range picker input
                        ]),
                        html.Div([
                            # Stock price button
                            # indicators button
                            # Number of days of forecast input
                            # forecast button
                        ]),
                    ],
                    className="nav"),
                html.Div(
                    [
                        html.Div(
                            [# Logo
                             # company name
                            ],
                            className="header"),
                        html.Div(#desc
                            id="description", className="description_ticker"),
                        html.Div([
                            #stock price plot
                        ], id="graphs-content"),
                        html.Div([
                            #indicator plot
                        ], id="main-content"),
                        html.Div([
                            #forecast plot
                        ], id="forecast-content")
                    ],
                    className="content")
                )



if __name__ == '__main__':
    app.run_server(debug=True)