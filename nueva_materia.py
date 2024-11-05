import streamlit as st 
st.title('Primera página a crear')
st.header('Segundo intento')

st.header('¡Bienvenido nuevo usuario!')
ss=st.selectbox('Seleccione una opcion', ('Me gustan los gatitos', 'Prefiero los perritos', 'abejita'))

st.sidebar.write('Espero se sienta emocionado de ver sus opciones en esta página')
st.sidebar.image('gatitito.png')
st.sidebar.image('abejita{.jpeg')

st.sidebar.write('Deberia seleccionar una función y averiguar que pasa')

st.balloons()
if ss== 'Me gustan los gatitos':
  st.image('gatito.botitas.jpg')
  st.video('gatitobeso.mp4')
else:
  st.image('perrito.jpeg')
  st.image('perrito2.jpg')
elif:
  st.audio('cancionabejita.mp3')
st.write(ss)

