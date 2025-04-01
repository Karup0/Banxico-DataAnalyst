import pandas as pd

# Cargar los datos desde el archivo CSV generado
df = pd.read_csv("tipo_cambio.csv")

# Crear rangos para clasificar los tipos de cambio
bins = [18, 19, 20, 21, 22]  # Ajustar los rangos según los datos reales
labels = [f"{bins[i]}-{bins[i+1]}" for i in range(len(bins)-1)]

# Clasificar los tipos de cambio en los rangos definidos
df["Rango"] = pd.cut(df["Tipo de Cambio"], bins=bins, labels=labels, right=False)

# Calcular las frecuencias por rango
frecuencias = df["Rango"].value_counts().sort_index()

# Crear una hoja de verificación
hoja_verificacion = pd.DataFrame({
    "Rango de Tipo de Cambio": frecuencias.index,
    "Frecuencia": frecuencias.values
})

# Guardar la hoja de verificación en un archivo CSV
hoja_verificacion.to_csv("hoja_verificacion.csv", index=False)