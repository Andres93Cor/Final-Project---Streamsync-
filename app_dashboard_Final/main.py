import streamsync as ss
import pandas as pd
import plotly.express as px

# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://streamsync.cloud

#LECTURA DEL DATA DATAFRAME
data_link = "https://raw.githubusercontent.com/cgl-itm/ProgramacionAvanzada-ITM/main/Proyectos/04_Datos/01_PV_Elec_Gas3.csv"
data = pd.read_csv(data_link, index_col=0, parse_dates=True)


# Its name starts with _, so this function won't be exposed
def update(state):
    print(type(state["fecha_ini"]),type(state["fecha_fin"]))
    df = data[state["fecha_ini"]:state["fecha_fin"]]
    fig = px.line(df, x=df.index, y="L06_347")
    state["grafico"] = fig
    
def update_Analisis_Bivariado(state):
    pass

def update_Analisis_Mensual(state):
    pass

# Initialise the state

initial_state = ss.init_state({
    "my_app": {
        "title": "My App"
    },
        "columnas": {str(key):str(key) for key in data.columns},
        "fecha_ini": data.index.min().date(),
        "fecha_fin": data.index.max().date(),
        "grafico": None,
        "graficoBox": None,
})

update(initial_state)