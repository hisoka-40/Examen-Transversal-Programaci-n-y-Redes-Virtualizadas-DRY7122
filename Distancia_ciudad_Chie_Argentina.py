import requests
import json
import time

# Configura tu clave de API de GraphHopper aquí
GRAPHHOPPER_API_KEY = '0c584c8b-9f3a-4c63-9cde-aa00652b3fa8'

def obtener_coordenadas(ciudad):
    url = f"https://graphhopper.com/api/1/geocode?q={ciudad}&locale=es&key={GRAPHHOPPER_API_KEY}"
    response = requests.get(url)
    data = json.loads(response.text)
    if 'hits' in data and data['hits']:
        return data['hits'][0]['point']['lat'], data['hits'][0]['point']['lng']
    else:
        return None, None

def obtener_ruta(ciudad_origen, ciudad_destino, vehicle='car'):
    lat_origen, lng_origen = obtener_coordenadas(ciudad_origen)
    lat_destino, lng_destino = obtener_coordenadas(ciudad_destino)
    
    if lat_origen is None or lat_destino is None:
        return None
    
    url = f"https://graphhopper.com/api/1/route?point={lat_origen},{lng_origen}&point={lat_destino},{lng_destino}&vehicle={vehicle}&locale=es&key={GRAPHHOPPER_API_KEY}"
    response = requests.get(url)
    data = json.loads(response.text)
    
    if 'paths' in data and data['paths']:
        ruta = data['paths'][0]
        distancia_km = ruta['distance'] / 1000
        distancia_millas = distancia_km * 0.621371
        duracion_segundos = ruta['time']
        duracion_formateada = time.strftime("%H:%M:%S", time.gmtime(duracion_segundos))
        narrativa = ruta['instructions']
        
        return distancia_km, distancia_millas, duracion_formateada, narrativa
    else:
        return None

if __name__ == "__main__":
    print("Bienvenido al sistema de consulta de distancias y tiempos de viaje con GraphHopper")
    
    # Opciones de medios de transporte disponibles
    opciones_vehiculo = {
        'car': 'Coche',
        'foot': 'A pie',
        'bike': 'Bicicleta',
        'truck': 'Camión',
        'plane': 'Avión'
        # Puedes agregar más opciones según los tipos de vehículos soportados por la API de GraphHopper
    }
    
    while True:
        ciudad_origen = input("Ingrese la ciudad de origen (en español): ").strip()
        ciudad_destino = input("Ingrese la ciudad de destino (en español): ").strip()
        
        # Mostrar opciones de vehículos disponibles
        print("\nSeleccione el medio de transporte:")
        for key, value in opciones_vehiculo.items():
            print(f"{key}: {value}")
        
        # Solicitar al usuario que elija un vehículo
        vehiculo_elegido = input("Elija una opción de vehículo (por ejemplo, 'car' para Coche): ").strip().lower()
        
        if vehiculo_elegido in opciones_vehiculo:
            resultado_ruta = obtener_ruta(ciudad_origen, ciudad_destino, vehiculo_elegido)
            
            if resultado_ruta:
                distancia_km, distancia_millas, duracion, narrativa = resultado_ruta
                
                print(f"\nInformación del viaje de {ciudad_origen} a {ciudad_destino}:")
                print(f"Distancia: {distancia_km:.2f} km | {distancia_millas:.2f} millas")
                print(f"Duración del viaje: {duracion}")
                print("Narrativa del viaje:")
                if isinstance(narrativa, list):
                    for idx, instruccion in enumerate(narrativa, start=1):
                        print(f"{idx}. {instruccion['text']}")
                else:
                    print("No se encontró una narrativa para esta ruta.")
            else:
                print("No se pudo obtener la información de la ruta. Verifique las ciudades ingresadas.")
        else:
            print("Opción de vehículo no válida. Por favor, elija una de las opciones mostradas.")
        
        continuar = input("\n¿Desea consultar otra ruta? Presione Enter para continuar o 's' para salir: ")
        if continuar.lower() == 's':
            break








