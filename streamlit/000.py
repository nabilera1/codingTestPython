import streamlit as st

# st.title('My First Streamlit App')
st.write('Hello, world!')

if st.button('Say hello'):
    st.write('Why hello there!')
else:
    st.write('Goodbye')