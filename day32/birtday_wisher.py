"""
==============================================================
AUTOMATED BIRTHDAY EMAIL SENDER
==============================================================

Description:
------------
This Python script automatically sends personalized birthday
wishes via email to people listed in a CSV file.

Workflow:
---------
1. Reads birthday data (name, email, birthdate) from 'birthdays.csv'.
2. Compares today's date with each person's birthday.
3. If a match is found, selects a random birthday letter template.
4. Personalizes the message with the recipients name.
5. Sends the message using Gmails SMTP server.

Modules Used:
--------------
- datetime: To handle current date operations.
- pandas: To read and process CSV data.
- smtplib: To send emails via SMTP.
- random: To choose a random letter template.

Configuration Requirements:
---------------------------
- A CSV file named 'birthdays.csv' with columns:
  name, email, year, month, day
- A directory named 'letter_templates' containing:
  letter_1.txt, letter_2.txt, letter_3.txt, etc.
- Gmail account credentials (address + app password).

Security Note:
--------------
Storing passwords in plain text is not secure.
   Consider using environment variables or an encrypted
   configuration manager for production use.
==============================================================
"""

# ============================== IMPORTS ==============================
from datetime import datetime   # Handles date and time operations
import pandas as pd             # For reading and manipulating CSV data
import smtplib                  # For sending emails through SMTP protocol
import random                   # For selecting random birthday templates
import os                       # For calling email password environment variable


# ====================== LOAD AND PREPARE BIRTHDAY DATA ======================
# Read the CSV file containing birthday data
df_birthday = pd.read_csv('birthdays.csv')

# Extract individual columns into Python lists for convenience
name_list = df_birthday["name"].to_list()
email_list = df_birthday["email"].to_list()
year_list = df_birthday["year"].to_list()
month_list = df_birthday["month"].to_list()
day_list = df_birthday["day"].to_list()

# Combine all data into a list of dictionaries for easy access
day_month_list = []
for name, email, year, month, day in zip(name_list, email_list, year_list, month_list, day_list):
    day_month_list.append({
        "name": name,
        "email": email,
        "year": year,
        "month": month,
        "day": day
    })


# ============================ GET CURRENT DATE =============================
today = datetime.now()         # Get current date and time
birth_month = today.month      # Extract the current month
birth_day = today.day          # Extract the current day


# ================== SELECT A RANDOM LETTER TEMPLATE ==================
# Randomly choose a template file from 1 to 3
template_number = random.randint(1, 3)

# Read the selected birthday letter template
with open(f'letter_templates/letter_{template_number}.txt') as letter_file:
    letter = letter_file.read()


# =================== SEND EMAILS TO BIRTHDAY MATCHES ===================
# Loop through each record in the birthday list
for person in day_month_list:
    # Check if today's date matches the person's birthday
    if person["day"] == birth_day and person["month"] == birth_month:
        # ----- Email account credentials -----
        my_email = "awakiyang9@gmail.com"         # Sender's email address
        password = os.getenv("email_password")           # Gmail App Password (called using os module)

        # ----- Personalize the letter -----
        personalized_letter = letter.replace('[NAME]', person["name"])
        subject = "Happy Birthday!"
        message = f"Subject: {subject}\n\n{personalized_letter}"

        # ----- Establish SMTP connection and send email -----
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()            # Identify ourselves to the mail server
                smtp.starttls()        # Secure the connection
                smtp.ehlo()            # Re-identify after encryption
                smtp.login(user=my_email, password=password)  # Log in
                smtp.sendmail(
                    from_addr=my_email,
                    to_addrs=person["email"],
                    msg=message
                )
            print(f"Birthday email sent successfully to {person['name']} ({person['email']})")

        except Exception as e:
            print(f" Failed to send email to {person['name']}: {e}")
