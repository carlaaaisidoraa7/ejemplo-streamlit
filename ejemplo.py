import streamlit as st 
st.title('Primera página a crear')
st.header('Segundo intento')

st.header('¡Bienvenido nuevo usuario!')
ss=st.selectbox('Seleccione una opcion', ('Nuevo usuario', 'Tengo ya creada una cuenta'))

st.sidebar.write('Espero se sienta emocionado de comersar sesión en esta página')
st.sidebar.image('gatito.png')

st.sidebar.write('Deberia de iniciar sesión y averiguar que pasa')
st.sidebar.image('gatobotas.jpg')

st.write(ss)
