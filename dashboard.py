import pandas as pd
import plotly.graph_objs as go
import dash
import dash_html_components as html
import dash_core_components as dcc

data = pd.read_csv('gapminder.csv')
app=dash.Dash()
app.layout=html.Div([
    html.Div(children=[html.H1("my first dashboard",
                               style={'color':'blue','text-align':'center'})],
             style={'border':'1px black solid',
                    'float':'left','width':'100%','height':'50px'}),
    html.Div(children=[dcc.Graph(id='scatter-plot',
                                 figure={'data':[go.Scatter(x=data['pop'],y=data['gdpPercap'],
                                                            mode='markers')],'layout':go.Layout(title='scatter plot')})],
             style={'border':'1px black solid',
                    'float':'left','width':'49%'}),
    html.Div(children=[dcc.Graph(id='box-plot',
                                 figure={'data':[go.Box(x=data['gdpPercap'])],'layout':go.Layout(title='box plot')})],style={'border':'1px black solid',
                    'float':'left','width':'49%'})
])
"""app.layout=html.H1(children="my first dashboard",
                   style={'color':"red",'text-align':'center'})"""

if __name__ == '__main__':
    app.run_server()