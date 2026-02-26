from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# 1. Load and sort the data
df = pd.read_csv('./data/formatted_sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

# 2. Initialise the Dash app
app = Dash(__name__)

# 3. Define CSS colour palette
colors = {
    'background': '#F2F2F2',  # Light gray background
    'header_bg': '#ff6b6b',   # "Pink Morsel" colored header
    'text': '#333333'         # Dark grey text
}

# 4. Define the layout of the app
app.layout = html.Div(style={'backgroundColor': colors['background'], 'fontFamily': 'Arial, sans-serif', 'minHeight': '100vh', 'padding': '20px'}, children=[
    
    # Header Section
    html.Div(style={'backgroundColor': colors['header_bg'], 'padding': '20px', 'borderRadius': '10px', 'marginBottom': '30px', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)'}, children=[
        html.H1(
            children='Soul Foods: Pink Morsel Sales Visualiser',
            style={'textAlign': 'center', 'color': 'white', 'margin': 0}
        )
    ]),

    # Radio Button Section
    html.Div(style={'textAlign': 'center', 'marginBottom': '20px', 'fontSize': '18px'}, children=[
        dcc.RadioItems(
            id='region-picker',
            options=[
                {'label': ' North ', 'value': 'north'},
                {'label': ' East ', 'value': 'east'},
                {'label': ' South ', 'value': 'south'},
                {'label': ' West ', 'value': 'west'},
                {'label': ' All ', 'value': 'all'}
            ],
            value='all', # "all" is the default selected option
            inline=True, # Keeps the buttons on a single horizontal line
            style={'padding': '10px'}
        )
    ]),

    # The Line Chart
    dcc.Graph(id='sales-line-chart')
])

# 5. Connecing radio buttons to graph
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-picker', 'value')
)
def update_graph(selected_region):
    # Filter the dataframe based on the radio button choice
    if selected_region == 'all':
        filtered_df = df
    else:
        # Assuming the column is 'Region', and making the data inside lowercase
        filtered_df = df[df['Region'].str.lower() == selected_region]

    # Generate the new line chart
    fig = px.line(
        filtered_df, 
        x='Date', 
        y='Sales', 
        title=f'Sales in Region: {selected_region.capitalize()}'
    )

    # Apply styling to the chart to match the app's theme
    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    return fig

# 6. Run the app
if __name__ == '__main__':
    app.run(debug=True)