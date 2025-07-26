import html
from dash import Dash, html, dcc, dash_table, callback, Input, Output
import pandas as pd
import plotly.express as px

app = Dash()
dfEuge = pd.read_excel('miopia25.xlsx')

# Cargar un dataset (acá usás el de gapminder como en tu screenshot, podés cambiarlo por iris si querés)
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')


app.layout = [
    html.Div(children="Hola Dash", id='my-div'),

    dcc.RadioItems(
        # options=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
        options=['pop', 'lifeExp','gdpPercap' ],
        value='pop',
        id='radioItems',
    ),
    dash_table.DataTable(
        data= df.to_dict('records'),
        page_size=10,
        id='tablaMiopía',
    ),
    dcc.Graph(
        figure={      },
        id='my-graph',
    )
]

@callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='radioItems', component_property='value'),
    prevent_initial_call=True
)
def mi_primer_callback(item_Elegido):
    html.Title(item_Elegido)
    print(item_Elegido)
    # return "Se presionó la opción " + díaElegido
    fig = px.histogram(df, x='continent', y=item_Elegido, histfunc="sum" )
    return fig


app.run(debug=True)

