import streamlit as st

st.title("FORMULIR BIODATA")
st.write("Silakan isi formulir di bawah ini:")

with st.form("my_form"):
    name = st.text_input("Masukkan nama Anda:")
    age = st.number_input("Masukkan usia Anda:", min_value=0, max_value=120, step=1)
    email = st.text_input("Masukkan email Anda:")
    noTelpon = st.number_input("Masukkan no telpon Anda:", step=1)  
    
    submitted = st.form_submit_button("Submit")
    if submitted:
      st.write("biodata yang anda :")
      st.write(f'nama lengkap: {name}')
      st.write(f'usia: {age} tahun')
      st.write(f'email: {email}')
      st.write(f'no telpon: {noTelpon}')