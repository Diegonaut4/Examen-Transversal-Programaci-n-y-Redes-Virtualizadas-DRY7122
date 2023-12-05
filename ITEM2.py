import requests

def obtener_distancia_duracion(ciudad_origen, ciudad_destino, api_key):
    base_url = "http://www.mapquestapi.com/directions/v2/route"
    params = {
        'key': api_key,
        'from': ciudad_origen,
        'to': ciudad_destino,
        'unit': 'k',  # Unidades en kilómetros
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code != 200 or data['info']['statuscode'] != 0:
        print("Error al obtener la información del viaje.")
        return None

    distancia = data['route']['distance']
    duracion_segundos = data['route']['time']

    return distancia, duracion_segundos

def convertir_segundos_a_horas_minutos_segundos(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    return horas, minutos, segundos

def calcular_combustible(distancia):
    # Supongamos un consumo promedio de 10 litros por cada 100 kilómetros
    consumo_litros_por_km = 10 / 100
    combustible_requerido = distancia * consumo_litros_por_km
    return round(combustible_requerido, 1)

def main():
    api_key = 'MNpD8FT26jFX7PFt7czWYVq3nhDEBZbg'
    
    ciudad_origen = input("Ingrese la ciudad de origen: ")
    ciudad_destino = input("Ingrese la ciudad de destino: ")

    info_viaje = obtener_distancia_duracion(ciudad_origen, ciudad_destino, api_key)

    if info_viaje:
        distancia, duracion_segundos = info_viaje

        horas, minutos, segundos = convertir_segundos_a_horas_minutos_segundos(duracion_segundos)
        combustible_requerido = calcular_combustible(distancia)

        print("\nInformación del viaje:")
        print(f"Distancia: {distancia:.1f} km")
        print(f"Duración: {horas} horas, {minutos} minutos, {segundos} segundos")
        print(f"Combustible requerido: {combustible_requerido:.1f} litros")

        print("\nS. ¡Buen viaje!")

if __name__ == "__main__":
    main()
