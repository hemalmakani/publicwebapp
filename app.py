import dash
from dash import dcc, html, dash_table, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from sqlalchemy import create_engine
import os

# Database connection
DATABASE_URL = 'postgresql://hemalm:IGAppEXhCPYWdjmQiS4TKQ4SPeL8tWzj@dpg-cqol16o8fa8c73btrgr0-a.ohio-postgres.render.com/test_db_yrae'

engine = create_engine(DATABASE_URL)

# Function to load data from PostgreSQL
def load_data(table_name):
    return pd.read_sql_table(table_name.lower(), engine)

# Load your data from PostgreSQL
R_SN = load_data('r_sn')
R_SN_1000 = load_data('R_SN_1000')
R_SN_1000G = load_data('R_SN_1000G')
R_SN_1000V = load_data('R_SN_1000V')
R_SN_2000 = load_data('R_SN_2000')
R_SN_2000G = load_data('R_SN_2000G')
R_SN_2000V = load_data('R_SN_2000V')
R_SN_MC = load_data('R_SN_MC')
R_SN_MCG = load_data('R_SN_MCG')
R_SN_MCV = load_data('R_SN_MCV')
R_UC_1000 = load_data('R_UC_1000')
R_UC_1000G = load_data('R_UC_1000G')
R_UC_1000V = load_data('R_UC_1000V')
R_UC_2000 = load_data('R_UC_2000')
R_UC_2000G = load_data('R_UC_2000G')
R_UC_2000V = load_data('R_UC_2000V')
R_UC_MC = load_data('R_UC_MC')
R_UC_MCG = load_data('R_UC_MCG')
R_UC_MCV = load_data('R_UC_MCV')
S_SN_1500 = load_data('S_SN_1500')
S_SN_1500G = load_data('S_SN_1500G')
S_SN_1500V = load_data('S_SN_1500V')
S_SN_400 = load_data('S_SN_400')
S_SN_400G = load_data('S_SN_400G')
S_SN_400V = load_data('S_SN_400V')
S_SN_500 = load_data('S_SN_500')
S_SN_500G = load_data('S_SN_500G')
S_SN_500V = load_data('S_SN_500V')
S_SN_600 = load_data('S_SN_600')
S_SN_600G = load_data('S_SN_600G')
S_SN_600V = load_data('S_SN_600V')
S_SN_Canada = load_data('S_SN_Canada')
S_UC_1500 = load_data('S_UC_1500')
S_UC_1500G = load_data('S_UC_1500G')
S_UC_1500V = load_data('S_UC_1500V')
S_UC_400 = load_data('S_UC_400')
S_UC_400G = load_data('S_UC_400G')
S_UC_400V = load_data('S_UC_400V')
S_UC_500 = load_data('S_UC_500')
S_UC_500G = load_data('S_UC_500G')
S_UC_500V = load_data('S_UC_500V')
S_UC_600 = load_data('S_UC_600')
S_UC_600G = load_data('S_UC_600G')
S_UC_600V = load_data('S_UC_600V')
S_UC_Canada = load_data('S_UC_Canada')

def remove_decimal_from_columns(df):
    df.columns = [col.split('.')[0] for col in df.columns]
    return df

# Define your data_frames dictionary
data_frames = {
    'Russel 1000': [R_SN_1000, R_UC_1000],
    'Russel 1000 Growth': [R_SN_1000G, R_UC_1000G],
    'Russel 1000 Value': [R_SN_1000V, R_UC_1000V],
    'Russel 2000': [R_SN_2000, R_UC_2000],
    'Russel 2000 Growth': [R_SN_2000G, R_UC_2000G],
    'Russel 2000 Value': [R_SN_2000V, R_UC_2000V],
    'Russel MidCap': [R_SN_MC, R_UC_MC],
    'Russel MidCap Growth': [R_SN_MCG, R_UC_MCG],
    'Russel MidCap Value': [R_SN_MCV, R_UC_MCV],
    'S&P 1500': [S_SN_1500, S_UC_1500],
    'S&P 1500 Growth': [S_SN_1500G, S_UC_1500G],
    'S&P 1500 Value': [S_SN_1500V, S_UC_1500V],
    'S&P 400': [S_SN_400, S_UC_400],
    'S&P 400 Growth': [S_SN_400G, S_UC_400G],
    'S&P 400 Value': [S_SN_400V, S_UC_400V],
    'S&P 500': [S_SN_500, S_UC_500],
    'S&P 500 Growth': [S_SN_500G, S_UC_500G],
    'S&P 500 Value': [S_SN_500V, S_UC_500V],
    'S&P 600': [S_SN_600, S_UC_600],
    'S&P 600 Growth': [S_SN_600G, S_UC_600G],
    'S&P 600 Value': [S_SN_600V, S_UC_600V],
    'Canada': [S_SN_Canada, S_UC_Canada]
}

# Define your factors dictionary
factors = {
    'Accelerating Sales': 'AS',
    'Expected Growth': 'EG',
    'Earnings Momentum': 'EM',
    'Historical Growth': 'HG',
    'Price Reversal': 'PR',
    'Small Size': 'SZ',
    'Profit Trends': 'PT',
    'Price Momentum': 'PM',
    'Relative Value': 'RV',
    'Traditional Value': 'TV',
    'Earnings Quality': 'EQ',
    'Earnings Risk': 'ER',
    'Price Volatility': 'PV',
    'Financial Leverage': 'FL'
}

for key, dfs in data_frames.items():
    R_SN_df = dfs[0]
    R_UC_df = dfs[1]

    # Applying function to R_SN DataFrames
    if R_SN_df is not None:
        R_SN_df = remove_decimal_from_columns(R_SN_df)
        print(f"{key} R_SN DataFrame columns after processing:")
        print(R_SN_df.columns)

    # Applying function to R_UC DataFrames
    if R_UC_df is not None:
        R_UC_df = remove_decimal_from_columns(R_UC_df)
        print(f"{key} R_UC DataFrame columns after processing:")
        print(R_UC_df.columns)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Navigation bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("HTS", href="/"))
    ],
    brand="Whats Working",
    brand_href="/",
    color="primary",
    dark=True,
)

# App layout
app.layout = dbc.Container([
    navbar,
    html.H1('HTS'),
    dcc.Dropdown(
        id='index-dropdown',
        options=[{'label': k, 'value': k} for k in data_frames.keys()],
        value='Russel 1000',
        style={'width': '35%', 'margin': 'auto'}
    ),
    dcc.Dropdown(
        id='factor-dropdown',
        options=[{'label': k, 'value': k} for k in factors.keys()],
        value='Accelerating Sales',
        style={'width': '35%', 'margin': 'auto'}
    ),
    dcc.Graph(id='cumulative-sum-graph', style={'width': '100%', 'height': '500px'}),
    dash_table.DataTable(
        id='hts-table',
        columns=[
            {'name': 'Date', 'id': 'Date'},
            {'name': 'Sector-Neutral', 'id': 'Sector-Neutral'},
            {'name': 'Unconstrained', 'id': 'Unconstrained'}
        ],
        data=[],
        style_table={'overflowX': 'auto', 'width': '100%', 'height': '300px', 'maxHeight': '300px'},
        style_cell={'textAlign': 'left', 'whiteSpace': 'normal', 'height': 'auto'}
    ),
    dcc.Graph(id='spread-graph', style={'width': '100%', 'height': '500px'})
])

@app.callback(
    [Output('cumulative-sum-graph', 'figure'),
     Output('hts-table', 'data'),
     Output('spread-graph', 'figure')],
    [Input('index-dropdown', 'value'),
     Input('factor-dropdown', 'value')]
)
def update_graph_and_table(selected_index, selected_factor):
    Dates = R_SN.loc[:, 'Date']
    Factor1 = data_frames[selected_index][0]
    Factor2 = data_frames[selected_index][1]

    Sector_Neutral = Factor1.loc[:, factors[selected_factor]]
    Unconstrained = Factor2.loc[:, factors[selected_factor]]
    Sector_Neutral_cumsum = Sector_Neutral.cumsum()
    Unconstrained_cumsum = Unconstrained.cumsum()

    cumulative_spread = Unconstrained_cumsum - Sector_Neutral_cumsum
    monthly_spread = Unconstrained - Sector_Neutral

    trace1 = go.Scatter(x=Dates, y=Sector_Neutral_cumsum, mode='lines', name='Sector-Neutral')
    trace2 = go.Scatter(x=Dates, y=Unconstrained_cumsum, mode='lines', name='Unconstrained')

    hts_data = pd.concat([Dates, Sector_Neutral_cumsum, Unconstrained_cumsum], axis=1)
    hts_data.columns = ['Date', 'Sector-Neutral', 'Unconstrained']

    trace_cumulative_spread = go.Scatter(x=Dates, y=cumulative_spread, mode='lines', name='Cumulative Spread')
    trace_monthly_spread = go.Bar(x=Dates, y=monthly_spread, name='Monthly Spread')

    spread_layout = go.Layout(
        title=f'Spread of {selected_factor} for {selected_index}',
        xaxis={'title': 'Date'},
        yaxis={'title': 'Spread'},
        barmode='overlay'
    )

    spread_figure = {'data': [trace_cumulative_spread, trace_monthly_spread], 'layout': spread_layout}

    return {
        'data': [trace1, trace2],
        'layout': go.Layout(
            title=f'Cumulative Sum of {selected_factor} for {selected_index}',
            xaxis={'title': 'Date'},
            yaxis={'title': 'Cumulative Sum'}
        )
    }, hts_data.to_dict('records'), spread_figure

if __name__ == '__main__':
    app.run_server(debug=True)