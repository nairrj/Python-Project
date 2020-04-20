#Essential Libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import json
import requests


#Read the json data from a json file and store it in a datafram
df = pd.read_json(r'C:/Users/rohit/source/repos/Python-Project/bid_info.json')

#Create a pivot table
#Now that the data is simply tabulated by buyer and bid status, we can build out the bars that show the various bid status count.
pv = pd.pivot_table(df, index=['requesting_department'], columns=["status"], values=['buyer'], aggfunc='count', fill_value=0)

#Each item being plotted is called a trace . Defining the traces for the final bar plot
trace1 = go.Bar(x=pv.index, y=pv[('buyer', 'Accepting Bids')], name='Accepting Bids')
trace2 = go.Bar(x=pv.index, y=pv[('buyer', 'All Bids Rejected')], name='All Bids Rejected')
trace3 = go.Bar(x=pv.index, y=pv[('buyer', 'All Proposals Rejected')], name='All Proposals Rejected')
trace4 = go.Bar(x=pv.index, y=pv[('buyer', 'Award Pending')], name='Award Pending')
trace5 = go.Bar(x=pv.index, y=pv[('buyer', 'Awarded')], name='Awarded')
trace6 = go.Bar(x=pv.index, y=pv[('buyer', 'Cancelled')], name='Cancelled')
trace7 = go.Bar(x=pv.index, y=pv[('buyer', 'Cancelled')], name='Cancelled')
trace8 = go.Bar(x=pv.index, y=pv[('buyer', 'No Award Made')], name='No Award Made')
trace9 = go.Bar(x=pv.index, y=pv[('buyer', 'No Responses Received')], name='No Responses Received')
trace10 = go.Bar(x=pv.index, y=pv[('buyer', 'RFI Closed')], name='RFI Closed')
trace11 = go.Bar(x=pv.index, y=pv[('buyer', 'Under Review')], name='Under Review')


#Final Dash app building
app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Business Opportunities in Cincinnati, Ohio'),
    html.Div(children='''Biding status report. - created by Anamika Mishra and Rohit Nair.'''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11],
            'layout':
            go.Layout(title='Biding Status by Buyer', barmode='stack')
        })
])


if __name__=="__main__":
    app.run_server(debug=True)
