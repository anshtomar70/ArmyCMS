import streamlit as st
from Add_logo import add_logo



st.set_page_config(page_title='CMS Platform',  layout='wide', page_icon='assets/imgs/lvlAlpha_logo.png', 
                   initial_sidebar_state='expanded',
                   menu_items = {
                        'Report a Bug': "mailto:contact@lvlalpha.com",
                        'About' : "The App is powered by lvlAlpha Pvt. Ltd."
                   })

add_logo(logo_url = 'assets/imgs/ArmyLogo.png')

st.title("Evacuation Details")
c1,c2,c3 = st.columns(3)
c1.checkbox("Request Ambulance")
c2.checkbox("Request Air Ambulance")
c3.checkbox("")



c4 , c5 = st.columns(2)
with c4:
    def number_system():
    #st.header("Number of Patients to be evacuated")
    
     number = c4.number_input("Enter number of patients to be evacuated:", value=0, step=1)
   
    #st.write("You entered:", number)

    #st.write("Press '+' to increase the number or '-' to decrease the number:")

     increase_btn = c4.button("+")
     decrease_btn = c4.button("-")

     if increase_btn:
           number += 1

     if decrease_btn:
            number -= 1

    #st.write("Updated number of patients:", number)

    if __name__ == "__main__":
       number_system()


c5.text_input("Additional Requirements")
st.button("Save and Submit")

#IM/Contact Support
def main():
    st.title("Contact Support")

    # Show a button to open the pop-up modal
    if st.button("Contact Support"):
        # Use Streamlit's st.form to create a pop-up modal
        with st.form(key='contact_support_form'):
            st.header("Contact Support")
            st.write("Use this form to send us a message or ask for support.")
            message = st.text_area("Your Message", height=100)
            submit_button = st.form_submit_button("Save and Submit",message)

        # Handle the form submission and display a success message
        if submit_button:
            # Process the message (you can add code here to handle the message)
            # For example, you can send the message via email or save it to a database
            # For demonstration purposes, we'll just show a success message
            st.success("Message sent successfully!")

if __name__ == "__main__":
    main()



