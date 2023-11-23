import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def generate_random_data():
    # Función para generar datos aleatorios
    x = np.linspace(0, 10, 100)
    y = np.random.randn(100)
    return x, y

def plot_random_graph():
    # Función para crear y mostrar una gráfica aleatoria
    x, y = generate_random_data()

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Datos aleatorios')
    plt.title('Gráfica Aleatoria')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    
    st.pyplot(plt)

def main():
    st.title('Visualización de Datos Aleatorios')
    st.sidebar.button('Generar nueva gráfica', on_click=plot_random_graph)

if __name__ == "__main__":
    main()
