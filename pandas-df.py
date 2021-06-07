import pandas as pd
from IPython.display import display as dsp
import subprocess as sproc

removeZip = "rm /content/dataset.zip"
removeCsv = "rm /content/2008.csv"
getDataSet = "wget -O dataset.zip 'archive.org/download/US-Flights-Data-2008/2008%20%28dataset%29.zip'"
unzipDataSet = "unzip dataset.zip"

def PrepararDataset():
  global outputGdS
  global outputUdS
  print("Descargando archivo ZIP...")
  outputGdS = sproc.call(getDataSet, shell = True)
  print("Archivo Zip Descargado")
  print("Status: ", outputGdS)
  print("Extrayendo CSV")
  outputUdS = sproc.call(unzipDataSet, shell = True)
  print("CSV Extraido")
  print("Status: ", outputUdS)

def DestruirDataset():
  global outputRmZ
  global outputRmC
  outputRmZ = sproc.call(removeZip, shell = True)
  print("Zip Eliminado")
  print("Status: ", outputRmZ)
  outputRmC = sproc.call(removeCsv, shell = True)
  print("Database eliminado")
  print("Status: ", outputRmC)
  
# dataset de prueba disponible en
# https://www.kaggle.com/vikalpdongre/us-flights-data-2008

# mirror-backup realizada en:
# https://archive.org/details/US-Flights-Data-2008

archiveDataset = "https://archive.org/download/US-Flights-Data-2008/2008%20%28dataset%29.zip/2008.csv"

dataset = "/content/2008.csv"

#!rm /content/dataset.zip
#!rm /content/2008.csv
#!wget -O dataset.zip "https://archive.org/download/US-Flights-Data-2008/2008%20%28dataset%29.zip"
#!unzip dataset.zip

# Carga OK Testeado
def CargarDatasetEnMemoria(datset):
  global df
  # especificar dataset o cambiar variable con alguna funcion personalizada o manualmente
  df = pd.read_csv(datset, nrows=100000)

# A partir de aqui algo falla
# Solucionado con IPython
def LeerHeadDataset(numHead):
  # numero es cantidad de filas
  dsp(df.head(numHead))

def LeerUltimasFilasDataset(numero):
  dsp(df.tail(numero))

def ReordenarDB():
  dsp(df.sample(frac = 1))

def ListarColumnas():
  dsp(df.columns)

def ListarTiposDeVariables():
  dsp(df.dtypes)

def MostrarArrays():
  dsp(df.values)

def NuevoDataframeDeNfilas(nu):
  global df2
  df2 = df.head(nu)

def MostrarNuevoDataFrame(numf):
  global df2
  dsp(df2.head(numf))
  
def FiltrarColumnaEspecifica(columna):
  # el valor en columna debe ser un string
  global column
  column = str(columna)
  dsp(df[columna].head())

def FiltrarPorFilas(numfilasp, numfilasf):
  dsp(df[numfilasp:numfilasf])

def FiltrarPorValorConcreto(columna, valor, numf):
  global column
  column = str(columna)
  # ejemplo:
  # df[df["ArrDelay"] < 60].head(5)
  # el valor < se podría establecer como una variable o argumento?
  df[df[columna] < valor].head(numf)

def FiltrarPorDato(que, donde):
  # deberia tener un syntax similar a
  # df[df[]]
  df[df[que]==donde]

