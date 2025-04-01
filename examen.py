import requests
import pandas as pd

# URL de la API de SIE del Banco de México y el token de acceso
url = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SR1501/datos/2023-01-01/2023-12-31?token=8d813e5ea0fe11db379f52b42f1913d0c8d75afc27584005bab21cc671a3565e"  # Sustituir con la URL correcta"

# Definir los parámetros de la solicitud en a url como la fecha de inicio y fin, el token y la transacción a consultar 
# en la plataforma de Banxico

# Ruta para llegar a la API de Banxico y la serie de datos que se desea consultar
# Sectores > Tipos de cambio y resultados históricos de las subastas > 
# Indice de tipo de cambio real con precios consumidor y con respecto a 111 países
# Con la ruta anterior podrias llegar al acceso de la API del tipo de cambio
# SR1501 es la transaccion que te da el  tipo de cambio del dólar estadounidense en pesos mexicanos   
# 2023-01-01 es la fecha de inicio y 2023-12-31 es la fecha de fin
# El token de acceso es necesario para autenticar la solicitud a la API, ese lo debes de obtener en la plataforma de Banxico

# Realizar la solicitud HTTP
response = requests.get(url)

# Procesar la respuesta y guardar los datos
if response.status_code == 200:
    print("Conexión exitosa. Procesando datos...")
    datos = response.json()["bmx"]["series"][0]["datos"]  # Extraer datos de la respuesta JSON
    # Crear un DataFrame con Pandas
    df = pd.DataFrame(datos)
    df.columns = ["Fecha", "Tipo de Cambio"]  # Renombrar las columnas
    df["Tipo de Cambio"] = pd.to_numeric(df["Tipo de Cambio"], errors="coerce")  # Convertir a numérico
    # Guardar los datos en un archivo CSV para análisis posterior
    df.to_csv("tipo_cambio.csv", index=False)
    print("Datos guardados exitosamente en 'tipo_cambio.csv'.")
else:
    print(f"Error al obtener datos: {response.status_code}")