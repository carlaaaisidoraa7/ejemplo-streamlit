import streamlit as st 
st.title('intento de codigo uno')
st.header('intento de primera página')

st.sidebar.text('Ingrese un nombre de ususario')
st.sidebar.text_input('')

st.sidebar.text('cree una contraseña para su usuario')
st.sidebar.text_input('')
globito = st.button('¡Termine de ingresar datos!')
if globito is True:
    st.balloons() and st.success('hemos terminado el proceso de inicio')
else:
    st.write('ya falta poco tu puedes')
