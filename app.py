from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# 1. Load the processed data
df = pd.read_csv('./data/formatted_sales_data.csv')

# 2. Sort the data by Date and convert the Date column to actual datetime objects to ensure they sort chronologically
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

# 3. Initialise the Dash app
app = Dash(__name__)

# 4. Create the line chart using Plotly Express
fig = px.line(
    df, 
    x='Date', 
    y='Sales', 
    title='Pink Morsel Sales Before and After Price Increase'
)

# 5. Define the layout of the app
app.layout = html.Div(children=[
    # A header which appropriately titles the visualiser
    html.H1(
        children='Soul Foods: Pink Morsel Sales Visualiser',
        style={'textAlign': 'center'}
    ),

    # The line chart
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# 6. Run the app
if __name__ == '__main__':
    app.run(debug=True)