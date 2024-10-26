import random
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
