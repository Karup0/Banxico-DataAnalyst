import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Función para cargar los datos
def cargar_datos():
    df = pd.read_csv("tipo_cambio.csv")  # Cargar el archivo generado previamente
    df["Fecha"] = pd.to_datetime(df["Fecha"])  # Convertir la columna Fecha a datetime
    df["Tipo de Cambio"] = pd.to_numeric(df["Tipo de Cambio"], errors="coerce")  # Convertir a numérico
    df = df.dropna()  # Limpiar datos nulos
    return df

# Histograma
def generar_histograma(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df["Tipo de Cambio"], bins=20, color="skyblue", edgecolor="black")
    plt.title("Distribución del Tipo de Cambio Peso/Dólar (Histograma)", fontsize=14)
    plt.xlabel("Tipo de Cambio", fontsize=12)
    plt.ylabel("Frecuencia", fontsize=12)
    plt.grid(axis="y", alpha=0.75)
    plt.tight_layout()
    plt.savefig("histograma_tipo_cambio.png")
    print("Histograma generado correctamente y guardado en 'histograma_tipo_cambio.png'.")
    plt.show()

# Gráfica de Barras
def generar_grafica_barras(df):
    # Usar los datos del histograma para la gráfica de barras
    valores = df["Tipo de Cambio"].value_counts().sort_index()
    plt.figure(figsize=(8, 5))
    plt.bar(valores.index, valores.values, color="lightgreen")
    plt.title("Frecuencia de Tipo de Cambio Peso/Dólar (Gráfica de Barras)", fontsize=14)
    plt.xlabel("Tipo de Cambio", fontsize=12)
    plt.ylabel("Frecuencia", fontsize=12)
    plt.tight_layout()
    plt.savefig("grafica_barras.png")
    print("Gráfica de barras generada correctamente y guardada en 'grafica_barras.png'.")
    plt.show()

# Gráfica de Pastel
def generar_grafica_pastel(df):
    # Usar los datos del histograma para la gráfica de pastel
    valores = df["Tipo de Cambio"].value_counts().sort_index()
    if valores.sum() <= 0:
        print("Los datos no son válidos para generar la gráfica de pastel.")
        return

    plt.figure(figsize=(6, 6))
    plt.pie(
        valores.values,
        labels=valores.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=plt.cm.Paired(np.linspace(0, 1, len(valores)))
    )
    plt.title("Distribución de Tipos de Cambio (Gráfica de Pastel)", fontsize=14)
    plt.tight_layout()
    plt.savefig("grafica_pastel.png")
    print("Gráfica de pastel generada correctamente y guardada en 'grafica_pastel.png'.")
    plt.show()

# Diagrama de Pareto
def generar_diagrama_pareto(df):
    # Usar los datos de fecha y tipo de cambio para el diagrama de Pareto
    datos_pareto = df.groupby("Fecha")["Tipo de Cambio"].mean().sort_values(ascending=False)
    porcentaje_acumulado = datos_pareto.cumsum() / datos_pareto.sum() * 100

    fig, ax1 = plt.subplots(figsize=(8, 6))

    # Gráfica de barras
    ax1.bar(datos_pareto.index.strftime("%Y-%m-%d"), datos_pareto.values, color="lightblue")
    ax1.set_xlabel("Fecha", fontsize=12)
    ax1.set_ylabel("Tipo de Cambio Promedio", fontsize=12)
    ax1.set_xticks(ax1.get_xticks()[::len(datos_pareto)//10])  # Reducir ticks en el eje X para legibilidad

    # Gráfica de línea
    ax2 = ax1.twinx()
    ax2.plot(datos_pareto.index.strftime("%Y-%m-%d"), porcentaje_acumulado.values, color="red", marker="o", linestyle="--")
    ax2.set_ylabel("Porcentaje Acumulado", fontsize=12)

    plt.title("Diagrama de Pareto: Variación de Tipo de Cambio", fontsize=14)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("diagrama_pareto.png")
    print("Diagrama de Pareto generado correctamente y guardado en 'diagrama_pareto.png'.")
    plt.show()

# Ejecución principal
if __name__ == "__main__":
    # Cargar los datos
    df = cargar_datos()

    if not df.empty:
        # Generar el histograma
        generar_histograma(df)

        # Generar gráfica de barras y pastel usando datos del histograma
        generar_grafica_barras(df)
        generar_grafica_pastel(df)

        # Generar diagrama de Pareto usando datos de fechas y tipo de cambio
        generar_diagrama_pareto(df)
    else:
        print("No se pudieron generar las herramientas debido a datos vacíos.")