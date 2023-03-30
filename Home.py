import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def create_bookingtable():
	c.execute("""CREATE TABLE IF NOT EXISTS BOOKINGTABLE(NAME TEXT(50),EMAIL TEXT(50),PHN_NO TEXT(10),ADDRESS TEXT(50),DATE TEXT(50),PLACE TEXT(50),PKG TEXT(50),PKG_TYPE TEXT(70),BUS_TYPE TEXT(50),NUM_OF_SEAT TEXT(50));""")


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def add_bookingdata(name,email,phn_no,address,date,place,pkg,pkg_type,bus_type,Num_of_Seat):
	c.execute('INSERT INTO bookingtable(name,email,phn_no,address,date,place,pkg,pkg_type,bus_type,Num_of_Seat) VALUES (?,?,?,?,?,?,?,?,?,?)',(name,email,phn_no,address,date,place,pkg,pkg_type,bus_type,Num_of_Seat))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def main():
	"""Tour & Travel App"""

	st.title("Tour & Travel App")
	placeholder=st.empty()
	with placeholder:
		video_file = open('travel.mp4', 'rb')
		video_bytes = video_file.read()
		st.video(video_bytes)
	
	
	
	menu = ["Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	

	if choice == "Login":
		st.sidebar.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')

		if st.sidebar.checkbox("Login"):
			placeholder.empty()
			
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			st.sidebar.success("Logged In as {}".format(username))
			if result:

				#placeholder.empty()
				
				

				selected = option_menu(
                menu_title=None,
                options=["Packages", "Booking"],
                icons=["bar-chart-fill", "pencil-fill"],  # https://icons.getbootstrap.com/
                orientation="horizontal",
                )
				if selected == "Packages":
					tab1, tab2, tab3 = st.tabs(["Chennai", "Ooty", "Rameshwaram"])
					with tab1:
						
						
						col1, col2 =st.columns(2)
						with col1:
							st.image("images/2.jpeg", width=300)
						with col2:
							st.write("pkg-01")
							st.write("Marina-Beach")
							st.write("Timing-6.00pm to 10.00pm")
							st.write("Amount-10,000")
							btn=st.button("Book")
							if btn:
								st.write("Please go to Booking menu")

						st.markdown("____________________________________________________________________________________")
						
						col1, col2 =st.columns(2)
						with col1:
							st.image("images/6.jpeg", width=300)
						with col2:
							st.write("pkg-02")
							st.write("mahabalipuram")
							st.write("Timing-10:23 am to 12:51pm        2 hr 28 mins")
							st.write("10:23 am from chennai")
							st.write("Timing-10:43 am to 1:11pm         2 hr 28 mins")
							st.write("10:43 am from chennai")
							st.write("Timing-10:50 am t0 1:18 pm         2 hr 28 mins")
							st.write("10:50 am from chennai")
							st.write(" Amount-10,000")
							btn1=st.button("Book", key="btn1")
							if btn1:
								st.write("Please go to Booking menu")

						st.markdown("____________________________________________________________________________________")
						
						col1, col2 =st.columns(2)
						with col1:
						    st.image("images/27.jpeg", width=300)
						with col2:
							st.write("pkg-03")
							st.write("santhome cathedral")
							st.write("timing-9:00 am to 10:00 am    1 hr")
							st.write("9:00 am from chennai")
							st.write("amount-2,100")
							btn2=st.button("Book", key="btn2")
							if btn2:
								st.write("please go to booking menu")
						st.markdown("_____________________________________________________________________________________")
						with tab2:
							
							col1, col2 =st.columns(2)
							with col1:
								st.image("images/25.jpeg", width=300)
							with col2:
								st.write("pkg-04")
								st.write("ooty")
								st.write("timing-8:15 pm to 7:08 am       10 hr 53 min")
								st.write("8:15 pm from chennai")
								st.write("timing-4:00 pm to 5:53 am       13 hr 53 min")
								st.write("4:00 pm from guduvancheri")
								st.write("Amount=5,600")
								btn3=st.button("book", key="btn3")
								if btn3:
									st.write("please go to booking menu")
							st.markdown("____________________________________________________________________________________")	
							
							col1, col2 =st.columns(2)	
							with col1:			
								st.image("images/16.jpeg", width=300)
							with col2:
								st.write("pkg-05")
								st.write("nilgris")
								st.write("3:20 pm to 5:53")
								st.write("Amount=5,100")
								btn8=st.button("Book", key="btn8")
								if btn8:
								    st.write("please go to booking menu")
							st.markdown("____________________________________________________________________________________")
							
							col1, col2 =st.columns(2)
							with col1:
								st.image("images/19.jpeg", width=300)
							with col2:
								st.write("pkg-06")
								st.write("coonor")
								st.write("timing-11:00 pm to 6:30")
								st.write("11:00 pm from chengalpattu")
								st.write("Amount=6,300")
								btn4=st.button("book", key="btn4")
								if btn4:
									st.write("please go to booking menu")
							st.markdown("____________________________________________________________________________________")
						with tab3:
							
							col1, col2 =st.columns(2)
							with col1:
								st.image("images/26.jpg", width=300)
							with col2:
								st.write("pkg-07")
								st.write("rameshwaram")
								st.write("timing-1:00 pm to 10:00 am")
								st.write("1:00 pm from chennai")
								st.write("amount=690")
								btn5=st.button("book", key="btn5")
								if btn5:
									st.write("please go to booking menu")
							st.markdown("____________________________________________________________________________________")
							
							col1, col2 =st.columns(2)
							with col1:
								st.image("images/20.jfif", width=300)
							with col2:
								st.write("pkg-08")
								st.write("dhanushkodi")
								st.write("timing-1:00 pm to 10:45 am")
								st.write("1:00 pm from chennai")
								st.write("amount=750")
								btn6=st.button("book",key="btn6")
								if btn6:
									st.write("please go to booking menu")
							st.markdown("____________________________________________________________________________________")
							
							col1, col2 =st.columns(2)
							with col1:
								st.image("images/21.jpeg", width=300)
							with col2:
								st.write("pkg-09")
								st.write("kaniyakumari")
								st.write("timing-7:45 pm to 11:45 am")
								st.write("7:45 pm from chennai")
								st.write("Amount=970")
								btn7=st.button("book", key="btn7")
								if btn7:
									st.write("please go to booking menu")
							st.markdown("____________________________________________________________________________________")
					
				elif selected == "Booking":
			

					def form():
						st.write("Booking Form")
						with st.form(key="information form"):
							name = st.text_input("name:")
							email = st.text_input("email")
							phn_no = st.text_input("phone number")
							address = st.text_input("address")
							date = st.date_input("enter the date:")
							
							place =st.selectbox('select the place', ["chennai", "Ooty", "Kanchipuram"])
							pkg = st.selectbox('select the package id', ["pkg-01", "pkg-02", "pkg-03", "pkg-04", "pkg-05", "pkg-06", "pkg-07", "pkg-08", "pkg-09",], key="pkg")
							pkg_type = st.selectbox('select the package type', ["couple", "family", "friends","others"], key="pkg_type")
							with st.expander("Bus Details"):
								bus_type = st.selectbox('select the bus_type', ["A/C", "NON A/C"], key="bud_type")
								Num_of_Seat = st.text_input("Num.of.Seat")
							submission = st.form_submit_button(label="submit")
							if submission == True:
								create_bookingtable()
								
								add_bookingdata(name,email,phn_no,address,date,place,pkg,pkg_type,bus_type,Num_of_Seat)
								st.success("successfully submitted")
								
					form()

					 
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		placeholder.empty()
		
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")



if __name__ == '__main__':
	main()