import streamlit as st
import sqlite3
conn = sqlite3.connect('data.db')
cur = conn.cursor()
st.header("Contact Us")
st.write("Company/Agency Name: Tour & Travel")
st.write("Address: Chennai")
st.write("Phone_No: 987654321")
st.write("Email: travel@gmail.com")
def form():
    st.write("If any Query with us share details")
    with st.form(key="information form"):
      name = st.text_input("name:")
      email = st.text_input("email")
      phn_no = st.text_input("phone number")
      sub = st.text_input("subject")
      date = st.date_input("enter the date:")
      submission = st.form_submit_button(label="submit")
      if submission == True:
        st.write("Our agency connect with you very soon")
        addData(name,email,phn_no,sub,date)

          
def addData(a,b,c,d,e):
    cur.execute("""CREATE TABLE IF NOT EXISTS contact_form(NAME TEXT(50),EMAIL TEXT(50),PHN_NO TEXT(10),SUB TEXT(50),DATE TEXT(50));""")
    cur.execute("insert into contact_form VALUES(?,?,?,?,?)",(a,b,c,d,e))
    conn.commit()
    conn.close()
    st.success("successfully submitted")
form()