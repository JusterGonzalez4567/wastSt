import streamlit as st


home = st.Page(
    page = "Vistas/home.py",
    title = "Incio",
    icon = "🏠",
    #icon = ":material/home",
    default = True,
)

acerca_de = st.Page(
    page = "Vistas/acerca_de.py",
    title = "Acerca de",
    icon = "👤",
)

ventas = st.Page(
    page = "vistas/ventas",
    title = "ventas",
    icon = "🛒",
)

chatbot = st.Page(
    page = "vistas/chatbot.py",
    title = "ChatBot",
    icon = "🤖",
     #icon = ":material/smart_toy",
)

pg = st.navigation(
    {
        "Información:":[home,acerca_de],
        "Proyectos:":[chatbot, ventas],
    }
)

st.logo("img/ChatBot.png")
st.sidebar.markdown("Elaborador con ❤️ por [Streamlit] (https://streamlit.io/gallery)")

