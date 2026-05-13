import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load processed data
df = pd.read_csv("formatted_output.csv")

# Convert date column to proper datetime format
df["date"] = pd.to_datetime(df["Date"])

# Sort data by date
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Sales"
    }
)

# Create Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    
    html.H1(
        "Soul Foods Sales Visualiser",
        style={"textAlign": "center"}
    ),

    dcc.Graph(
        figure=fig
    )

])

# Run app
if __name__ == "__main__":
    app.run(debug=True)