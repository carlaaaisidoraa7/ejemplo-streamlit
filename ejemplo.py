import streamlit as st 
st.title('intento de codigo uno')
st.headder('intento de primera página')

st.textsidebar('Ingrese un nombre de ususario')
st.text_inputsidebar()

st.text_inputsidebar('cree una contraseña para su usuario')
st.text_inputsidebar()
globito = st.button('¡Termine de ingresar datos!')
if globito is True:
    st.balloons() and st.success('hemos terminado el proceso de inicio')
else:
    st.write('ya falta poco tu puedes')
