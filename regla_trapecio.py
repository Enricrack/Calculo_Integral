import streamlit as st
import math

# Configuración de la página
st.set_page_config(page_title="Calculadora de Integrales", page_icon="📈")

st.title("Calculadora de Integrales Numéricas")
st.write("Esta herramienta aplica la **Regla del Trapecio** para aproximar el área bajo la curva.")

# Entradas del usuario
st.sidebar.header("Parámetros de configuración")
f_str = st.text_input("Ingrese la función f(x):", "x**2")
a = st.number_input("Límite inferior (a):", value=0.0)
b = st.number_input("Límite superior (b):", value=1.0)
n = st.sidebar.slider("Número de subdivisiones (n):", 10, 5000, 1000)

# Lógica del algoritmo
def calcular():
    try:
        # Creamos la función lambda segura
        f = lambda x: eval(f_str.replace('x', f'({x})'))
        
        # Algoritmo de la Regla del Trapecio
        h = (b - a) / n
        suma = f(a) + f(b)
        for i in range(1, n):
            suma += 2 * f(a + i * h)
        resultado = (h / 2) * suma
        
        return resultado
    except Exception as e:
        return None

# Acción al presionar el botón
if st.button("Calcular Integral"):
    resultado = calcular()
    if resultado is not None:
        st.success(f"El resultado aproximado es: **{resultado:.6f}**")
    else:
        st.error("Error en la función. Asegúrate de usar 'x' y operadores válidos (ej: x**2 + 3*x)")

st.info("Nota: Este algoritmo calcula la integral de forma numérica, ideal para funciones complejas.")