import random
import json
import pandas as pd
from datetime import datetime, timedelta

locacoes = {
    "insper": (-23.567536, -46.684048),  
    "trabalho": (-23.588596, -46.686024),  
    "casa": (-23.589517, -46.687481), 
    "missa_paulista": (-23.563988, -46.654545),  
    "supermercado": (-23.650792, -46.703596),  
    "missa_nsb": (-23.564125, -46.673206), 
    "colinas_sjc": (-23.2237, -45.8995), 
    "rodoviaria_tiete": (-23.517532, -46.628872) 
}

def gerar_dados_localizacao_app(dias=30, registros_por_dia=100):
    dados = []
    horario_inicial = datetime.now() - timedelta(days=dias)
    
    for dia in range(dias):
        data_atual = horario_inicial + timedelta(days=dia)
        
        for _ in range(registros_por_dia):
            hora = data_atual + timedelta(minutes=random.randint(0, 1440))  
        
            if hora.weekday() < 5: 
                if 7 <= hora.hour <= 17: 
                    loc = locacoes["trabalho"]
                else: 
                    loc = locacoes["casa"]
            elif hora.weekday() == 5:
                if 9 <= hora.hour <= 11:
                    loc = locacoes["missa_paulista"]
                elif 12 <= hora.hour <= 14:
                    loc = locacoes["supermercado"]
                else:
                    loc = locacoes["casa"]
            else: 
                if 14 <= hora.hour <= 16:
                    loc = locacoes["missa_nsb"]
                elif 17 <= hora.hour <= 18:
                    loc = locacoes["colinas_sjc"]
                elif 20 <= hora.hour <= 21:
                    loc = locacoes["rodoviaria_tiete"]
                else:
                    loc = locacoes["casa"]
            
            dados.append({
                "latitude": loc[0] + random.uniform(-0.0001, 0.0001), 
                "longitude": loc[1] + random.uniform(-0.0001, 0.0001),
                "timestamp": hora.strftime("%Y-%m-%d %H:%M:%S"),
                "local": [key for key, val in locacoes.items() if val == loc][0]
            })
    
    return dados

# ================================================================================ #

def get_lat_lon():
    '''
    return a random latitude and longitude
    '''
    lat = random.uniform(-23.725, -23.435) 
    lon = random.uniform(-46.825, -46.365) 

    return round(lat,6) , round(lon,6)

def get_severity():
    '''
    return a random severity type 
    '''
    severity = ['low', 'median', 'high']
    return random.choice(severity)

def get_incident_type():
    '''
    return a random type of 'disaster' 
    '''
    types = ['flood', 'tree falls', 'landslide']
    return random.choice(types)

def get_time():
    '''
    return a random time 
    '''
    hour = random.randint(0, 23)  
    minute = random.randint(0, 59)  
    return f"{hour:02d}:{minute:02d}"  


data_list = []

for i in range(100):  
    latitude, longitude = get_lat_lon()
    severity = get_severity()
    incident_type = get_incident_type()
    time = get_time()

    data = {
            "id": i + 1,
            "latitude": latitude,
            "longitude": longitude,
            "severity": severity,
            "incident_type": incident_type,
            "time": time
        }
    
    data_list.append(data)

with open('data_partner_api.json', 'w') as arquivo_json:
    json.dump(data_list, arquivo_json, indent=4)

print("JSON file created successfully!")