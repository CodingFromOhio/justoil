import streamlit as st
import smtplib as sp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Title of the app
st.title("Just Oil Used Oil Pickup Test")

# Description
st.write("Please fill in the details below for the pickup of your used oil")

# User input fields
name = st.text_input("Owner Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
address = st.text_input('Pickup Address')

# Date and Time input
booking_date = st.date_input("Select Booking Date", min_value=datetime.today())

# Additional details (optional)
oil_quantity = st.number_input('Enter the amount of oil (in liters): ')

# Submit button
if st.button("Submit Booking"):
    if name and email and phone and booking_date and oil_quantity and address:
        # Confirmation message to the user
        st.success(f"Oil pickup confirmed for {name}!")
        print(name, email, phone, booking_date, oil_quantity, address)

        # Email content
        admin_message = MIMEMultipart()
        admin_message["From"] = "voidmini12@gmail.com"
        admin_message["To"] = "ppratyush1509@gmail.com"
        admin_message["Subject"] = "Used Oil Pickup Booking"
        admin_body = f"""
        New oil pickup booking received:
        Owner: {name}
        Email: {email}
        Phone: {phone}
        Booking Date: {booking_date}
        Oil Quantity: {oil_quantity} liters
        Address: {address}
        """
        admin_message.attach(MIMEText(admin_body, "plain"))

        user_message = MIMEMultipart()
        user_message["From"] = "voidmini12@gmail.com"
        user_message["To"] = email
        user_message["Subject"] = "Oil Pickup Confirmation"
        user_body = f"""
        Dear {name},

        Your oil pickup has been confirmed for {booking_date}.
        \nPlease ensure the oil is ready for pickup at the address: {address}.
        \nQuantity: {oil_quantity} liters.

        Thank you for using our service!

        Best regards,
        Just Oil Pickup Team
        """
        user_message.attach(MIMEText(user_body, "plain"))

        try:
            # Set up the SMTP server and send the emails
            server = sp.SMTP("smtp.gmail.com", 587)
            server.starttls()  # Secure the connection
            server.login('voidmini12@gmail.com', 'oxky gzzj bjju ecfg')  # Use app password if 2FA is enabled
            server.sendmail("voidmini12@gmail.com", "ppratyush1509@gmail.com", admin_message.as_string())
            server.sendmail("voidmini12@gmail.com", email, user_message.as_string())
            server.quit()
            st.success("Confirmation emails have been sent!")
        except Exception as e:
            st.error(f"Error sending email: {e}")
    else:
        st.error("Please fill in all required fields.")
