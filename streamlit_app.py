#import streamlit as st
#import matplotlib.pyplot as plt
#import plotly.express as px
#st.balloons()
#st.title("Hola mundo...UPRH")

import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

####################
## ajustar el layout
#################### 

st.set_page_config(layout="wide")


##################
## tamaño del plot
################## 

fig, ax = plt.subplots()


#########
## titulo
######### 

col1,col2,col3 =st.columns([1,3,1]) #esto dice que la primera y ultima columna van hacer pequenas mientras que la segunda va a ser ancha

col1.image ("https://github.com/elioramospr/hola_streamlit_mj/blob/main/logouprh.png?raw=true",width=150)
#tambien puede ser algo asi = st.image("/Users\UPRH\Desktop\COMP3005LD5\logouprh.png")

col2.title("Datos de Covid - Variante Omicron")

col3.image("https://github.com/elioramospr/hola_streamlit_mj/blob/main/covid.png?raw=true", width=150)


##############################################
## esto es para que salga una linea horizontal
############################################## 

st.divider()

#################
## datos de covid 
################# 

df_covid = pd.read_csv("https://raw.githubusercontent.com/elioramosweb/archivo_datos/main/datos_diarios-2022-03-22_10_20_15.csv",parse_dates=['date'])

##################
#seleccionar columna
##################

nombres = list(df_covid.columns)[1:] #no empienza desde 0 si no desde el 1 que seria tests_rate

columna = st.sidebar.selectbox("Columna de interes:", nombres)


#########################################
#indicar si se quiere suavizar la grafica
#########################################

suavizado = st.sidebar.checkbox("Suavizado")

####################################
# indicar si se quiere mostrar tabla 
####################################

tabla = st.sidebar.checkbox ("Mostrar datos")


df_covid.plot(x= "date", y= columna, ax=ax,
              xlabel= "Fecha",
              ylabel= columna)

col1, col2= st.columns(2)

if suavizado:
    ventana = st.sidebar.slider("Ventana de suavizado [dias]", 
                         1,15,7)
    df_rolling = df_covid[columna].rolling(ventana,center = True).mean()
    df_covid[columna+"_rolling"] = df_rolling 
    df_covid.plot(x="date", y=columna+"_rolling", ax=ax)
    st.sidebar.divider()
    
col1.pyplot(fig)

if tabla: 
    df_covid["date"] = df_covid ["date"].dt.strftime("%d-%b-%Y") #d- dia b- mes Y- ano completo
    df_filtrado = df_covid[["date", columna]] 
    col2.write(df_filtrado)
    
st.sidebar.divider

st.sidebar.markdown("""Aplicacion desarrollada por: Joyce S. Laboy Figueroa <br>
                    Comp3005<br> Universidad de Puerto Rico en Humacao""",
                    unsafe_allow_html=True)