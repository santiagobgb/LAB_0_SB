
# -- ------------------------------------------------------------------------------------ -- #

# -- Proyecto: Describir brevemente el proyecto en general                                -- #

# -- Codigo: RepasoPython.py - describir brevemente el codigo                             -- #

# -- Repositorio: https://github.com/                                                     -- #

# -- Autor: Nombre de autor                                                               -- #

# -- ------------------------------------------------------------------------------------ -- #



# -- ------------------------------------------------------------- Importar con funciones -- #

import funciones as fn

import visualizaciones as vs



import pandas as pd



# -- --------------------------------------------------------- Descargar precios de OANDA -- #



# token de OANDA

OA_Ak = 'e' + '2da67524b4531c01c0de762e3cd17a4-56c127dda990aa69b9ec0d5fb2b4d5b' + 'e'

OA_In = "EUR_USD"                  # Instrumento

OA_Gn = "D"                       # Granularidad de velas

fini = pd.to_datetime("2019-01-06 00:00:00").tz_localize('GMT')  # Fecha inicial

ffin = pd.to_datetime("2019-12-06 00:00:00").tz_localize('GMT')  # Fecha final



df_pe = fn.f_precios_masivos(p0_fini=fini, p1_ffin=ffin, p2_gran=OA_Gn,

                             p3_inst=OA_In, p4_oatk=OA_Ak, p5_ginc=4900)



# -- --------------------------------------------------------------- Graficar OHLC plotly -- #



vs_grafica1 = vs.g_velas(p0_de=df_pe.iloc[0:120, :])

vs_grafica1.show()



# -- ------------------------------------------------------------------- Conteno de velas -- #

# multiplicador de precios

pip_mult = 10000



# -- 0A.1: Hora

df_pe['hora'] = [df_pe['TimeStamp'][i].hour for i in range(0, len(df_pe['TimeStamp']))]



# -- 0A.2: Dia de la semana.

df_pe['dia'] = [df_pe['TimeStamp'][i].weekday() for i in range(0, len(df_pe['TimeStamp']))]



# -- 0B: Boxplot de amplitud de velas (close - open).

df_pe['co'] = (df_pe['Close'] - df_pe['Open'])*pip_mult



# -- ------------------------------------------------------------ Graficar Boxplot plotly -- #

vs_grafica2 = vs.g_boxplot_varios(p0_data=df_pe[['co']], p1_norm=False)

vs_grafica2.show()

#---------------------------------------------------------------------- mes en el que ocurrio la vela--#

df_pe['mes'] = [df_pe['TimeStamp'][i].month() for i in range(0, len(df_pe['TimeStamp']))]
