 
import folium
import pandas as pd
import pymongo

 #########################################################################################################################
def coords_froms(s):
    list = s.replace('{','').replace('}','').replace('[','').replace(']','').split(':')
    a =[float(i) for i in list[2].replace("'",'').split(',')]
    return a

#########################################################################################################################
def creacion_mapa(n_pueblo = 'ADANERO'):
    cliente=pymongo.MongoClient('mongodb://localhost:27017')  # cliente , la conexion por defecto
    db=cliente.EmptiedSpain   # llamada a la base de datos
    entidades_pueblo=db.emptiedSpain.find({'Pueblo_desde':n_pueblo.replace(' ','_')})
    info_pueblo = pd.DataFrame(db.emptiedSpain.find({'Entidad Singular de Población':n_pueblo}))
    # display(info_pueblo)
    df = pd.DataFrame(entidades_pueblo)
    centro = info_pueblo.iloc[0].location['coordinates'][::-1] # ojo, tengo que leerlo al reves pq en mongo la longitud va antes
    informaciontiempo = info_pueblo.iloc[0]['Weather_info']
    infofibra = str(info_pueblo.iloc[0]['Cobertura redes fijas ≥ 100Mbps']*100)
    info30mb = str(info_pueblo.iloc[0]['Cobertura ≥ 30Mbps']*100)
    mapa=folium.Map(location=centro,
                    tiles='openstreetmap', zoom_start=12)
    iframe = folium.IFrame('Info del tiempo:'+informaciontiempo+'<br>'+
                            'Info internet(30Mb):'+ info30mb+'%  ,'+'Info internet(100Mb):'+ infofibra+'%')
    popamunt = folium.Popup(iframe, min_width=300, max_width=300)
    folium.CircleMarker(centro, popup=popamunt,tooltip='<strong>Información del pueblo</strong>', radius=10,fill_color='green', color = 'green', 
    icon=folium.Icon(color='green',prefix='glyphicon',icon='on')).add_to(mapa)
    for i in range(df.shape[0]):
        point = df.iloc[i]
        st = point['nombre']
        folium.Marker(point['location']['coordinates'][::-1],st ).add_to(mapa)
    return mapa

#########################################################################################################################

def find_near(geopoint, radio=1000):
    return db.emptiedSpain.find({'$and':[{'location':{
        '$near': {'$geometry': geopoint, '$maxDistance':radio}
    }},{'Entidad': 'Hospital'}]})

#########################################################################################################################
