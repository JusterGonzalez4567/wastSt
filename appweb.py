import streamlit as st

# Crear un menú de navegación en la barra lateral
page = st.sidebar.selectbox("Navegación", ["Inicio", "Acerca de","Ventas","ChatBot"])

# Lógica de navegación entre páginas
if page == "Inicio":
    st.title("Página de Inicio")    
    st.write("Bienvenido a la página principal.")
elif page == "Acerca de":
    st.title("Acerca de")
    st.write("Esta es una aplicación con múltiples páginas.")

if page == "ventas":
    st.title("Ventas")    
    st.write("Ventas")
elif page == "ChatBot":
    st.title("ChatBot")
    st.write("Bienvenidos")