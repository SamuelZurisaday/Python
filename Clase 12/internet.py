import requests

while True:
    pais = input("Ingrese el país que quiere: ")
    direccion_web = f"https://restcountries.com/v3.1/name/{pais}"
    try:
        pedido_web = requests.get(direccion_web)
        pedido_web.raise_for_status()  # Verifica si la respuesta es exitosa
        informacion = pedido_web.json()

        informacion_en_diccionario = informacion[0]
        latitud_longitud = informacion_en_diccionario.get("latlng", "No disponible")
        paises_fronterizos = informacion_en_diccionario.get("borders", "No disponible")
        nombre = informacion_en_diccionario["name"]["common"]
        capital = informacion_en_diccionario.get("capital", ["No disponible"])[0]
        print(nombre, capital, latitud_longitud, paises_fronterizos)
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
    except KeyError as e:
        print(f"Error al extraer información: falta la clave {e} en los datos recibidos")
    except IndexError as e:
        print(f"Error en la extracción de datos: {e}")

    continuar = input("¿Desea buscar otro país? (s/n): ")
    if continuar.lower() != 's':
        break