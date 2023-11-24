import streamlit as st
import subprocess

# Instalar dependencias
st.write("Instalando dependencias...")
subprocess.call("pip install folium streamlit-folium", shell=True)

# Importar los módulos después de la instalación
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static

# Generar datos aleatorios para las dos columnas
data_columna1 = pd.DataFrame({
    'Categoría': ['A', 'B', 'C', 'D'],
    'Valor': np.random.randint(1, 10, size=4)
})

data_columna2 = pd.DataFrame({
    'Categoría': ['E', 'F', 'G', 'H'],
    'Valor': np.random.randint(1, 10, size=4)
})

# Crear el mapa de Medellín
medellin_map = folium.Map(location=[6.2442, -75.5812], zoom_start=12)

# Generar 50 ubicaciones geográficas aleatorias en Medellín
random_locations = [(6.2442 + np.random.uniform(-0.1, 0.1), -75.5812 + np.random.uniform(-0.1, 0.1)) for _ in range(50)]

# Señalizar los puntos en el mapa como círculos
for location in random_locations:
    folium.Circle(location, radius=100, color='blue', fill=True, fill_color='blue').add_to(medellin_map)

# Crear dos columnas para los gráficos
col1, col2 = st.columns(2)

# Gráficos de barras en las columnas
col1.bar_chart(data_columna1.set_index('Categoría'))
col2.bar_chart(data_columna2.set_index('Categoría'))

# Mostrar el mapa debajo de las columnas
st.markdown("### Mapa de Medellín con Puntos Aleatorios")
folium_static(medellin_map)



