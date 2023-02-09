import dash
from dash import Dash, dcc, html, Input, Output,callback
import plotly.express as px
import pandas as pd

# Load the dataset from Kaggle
df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv?_sm_au_=isVscHQb5ZKNbbH5Q0WpHK6H8sjL6", error_bad_lines=False)
df.head()


# Initialize the Dash app
app = dash.Dash()

# Create the layout of the app
app.layout = html.Div([
    html.H1("Real Dataset2"),
    dcc.Graph(
        id="dataset-graph",
        figure=px.line(df, x="sepal_width", y="petal_length", title="sepal_width VS petal_length ")
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
