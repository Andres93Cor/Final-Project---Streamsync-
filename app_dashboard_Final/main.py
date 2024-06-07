import streamsync as ss
import pandas as pd
import plotly.express as px
import numpy as np


# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://streamsync.cloud

#LECTURA DEL DATA DATAFRAME
data_link = "https://raw.githubusercontent.com/cgl-itm/ProgramacionAvanzada-ITM/main/Proyectos/04_Datos/01_PV_Elec_Gas3.csv"
data = pd.read_csv(data_link, index_col=0, parse_dates=True)


# Its name starts with _, so this function won't be exposed
def update(state):
   # print(type(state["fecha_ini"]),type(state["fecha_fin"]))
    df = data[state["fecha_ini"]:state["fecha_fin"]]
   # print(state["vari"])
    fig = px.line(df, x=df.index, y=state["vari"])
    fig2= px.histogram(df, x=state["vari"])
    state["grafico"] = fig
    state["histograma"] = fig2
    state["min"]=data[state["vari"]].min()
   # print(state["min"])
    state["max"]=data[state["vari"]].max()
   # print(state["max"])
    state["Mean"]=data[state["vari"]].mean()
   # print(state["Mean"])
    state["std"]=data[state["vari"]].std()
   # print(state["std"])

def update_Analisis_Bivariado(state):
    #print(state["fecha_ini"])
    #print(state["fecha_fin"])
    df = data[state["fecha_ini"]:state["fecha_fin"]]
    #print(df)

    state["corr"]=df.corr()

    state["corrVariables"]=state["corr"][state["rowCorr"]][state["colCorr"]]
    fig3=px.imshow(state["corr"],text_auto=True)
    state["HeatMap"]=fig3
    state["scatter"]= px.scatter(df[state["colCorr"]],df[state["rowCorr"]])

    
    #print(state["corr"])
    print(state["rowCorr"])
    print(state["colCorr"])
    #print(state["corrVariables"])
   

def update_Analisis_Mensual(state):
   # print(state["DropMensual"])
   # print(state["fecha_ini"])
   # print(state["fecha_fin"])
    df = data[state["fecha_ini"]:state["fecha_fin"]]
    

    df=df[df.index.month == int(state["DropMensual"])]
    print(df)
    state["graficoBox"]=px.box(df, x=df.index.year, y=state["DropVariable"])

    #df['']=pd.to_datetime(df[''])
    
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
        "histograma": None,
        "HeatMap": None,
        "graficoBox": None,
        "scatter": None,
        "vari": 'Cumulative_solar_power',
        "min": None,
        "max": None,
        "Mean": None,
        "std": None,
        "corr": None,
        "rowCorr": 'Cumulative_solar_power',
        "colCorr": 'Gas/day',
        "corrVariables": None,
        "DropMensual": 1,
        "DropVariable": None,
})

update(initial_state)
update_Analisis_Bivariado(initial_state)
update_Analisis_Mensual(initial_state)