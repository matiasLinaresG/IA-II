from A_estrella import A_estrella

import pandas as pd
import numpy as np

#cuantas convinacines de a pares se pueden hacer con 128 elementos, no importa el orden y se pueden repetir
#128*127/2=8128 combinaciones.
#128^2 / (2! * (128-2)!) = 8128


#abrir el archivo .csv en una varible llamada "Mapa" en un dataframe
Mapa=np.array(pd.read_csv('mapa.csv',header=None, index_col=None))
Costo=np.array(pd.read_csv('costo.csv',header=None, index_col=None))
#abrir el archivo .csv en una varible llamada "IdAlmacen" en un dataframe

IdAlmacen=pd.read_csv('ID_estantes.csv')
# print(IdAlmacen)


#ejemplo:
#nueva_fila = pd.DataFrame({'Nombre': ['Luis'], 'Edad': [33], 'Ciudad': ['Cusco']})
#df = pd.concat([nueva_fila, df]).reset_index(drop=True)

IdAlmacen.loc[len(IdAlmacen)]=[1001,0,0]
print("Baia en:  0,0") # TODO: Cambiar esto

# IdAlmacen.to_csv("ID_estantes.csv")

Distancias=pd.DataFrame( columns=['id','distancia'])

for i in range(len(IdAlmacen['ID'])-1):
    for j in range(i+1,len(IdAlmacen['ID'])):
        #agregar a la tabla de distancias el id de los almacenes y la distancia entre ellos
        ID_distancia=str(IdAlmacen['ID'][i])+'-'+str(IdAlmacen['ID'][j])
        comienzo=[IdAlmacen['I'][i],IdAlmacen['J'][i]]
        fin=[IdAlmacen['I'][j],IdAlmacen['J'][j]]

        distancia=A_estrella(Mapa,Costo,comienzo,fin)
        #agregar id y distancia a la tabla

        Distancias.loc[len(Distancias)]=[ID_distancia,distancia]
 
     
#mostar toda la tabla de distancias, sin truncar
pd.set_option('display.max_rows', None)
# print(Distancias)
print("Listo")

Distancias.to_csv('distancias.csv',index=False)
