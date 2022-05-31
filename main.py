import dash
from dash import Dash, dcc, html
import google.cloud 
import biqquery
import pandas as pd
import plotply
import plotply. express as px

app=dash.Dash(__name__)
server=app.server
client = bigquery.Client()

query = """
    SELECT * FROM
    FROM ML.FORECAST(MODEL covid19.numreports_forecast,
                     STRUCT(14 AS horizon, 0.9 AS confidence_level))
"""

query_job = client.query(query)

df = query_job.to_dataframe()

fig = px.line(df, x='time_series_timestamp', y = 'time_series_data')

app.layout = html.Div(children = [
    html.H1("Covid-19 cases forecast"),
    html.Div(children = '''An app to forecast Covid-19 cases in Romania''')
    dcc.Graph(
        id='Covid-19 cases forecast',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8080)