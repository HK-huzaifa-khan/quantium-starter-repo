import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_output.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Sort values
df = df.sort_values("Date")

# Create Dash app
app = Dash(__name__)

# App Layout
app.layout = html.Div(

    style={
        "backgroundColor": "#f4f4f4",
        "padding": "20px",
        "fontFamily": "Arial"
    },

    children=[

        html.H1(
            "Soul Foods Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "30px"
            }
        ),

        html.Div([

            html.Label(
                "Select Region:",
                style={
                    "fontSize": "20px",
                    "fontWeight": "bold",
                    "marginRight": "20px"
                }
            ),

            dcc.RadioItems(
                id="region-filter",
                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                ],
                value="all",
                inline=True,
                style={
                    "marginBottom": "30px"
                }
            )

        ]),

        dcc.Graph(id="sales-chart")

    ]
)

# Callback for interactive filtering
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)

def update_chart(selected_region):

    # Filter data
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]

    # Create chart
    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales - {selected_region.title()} Region",
        labels={
            "Date": "Date",
            "Sales": "Sales"
        }
    )

    # Styling graph
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(size=14),
        title_font=dict(size=24)
    )

    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)