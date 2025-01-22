import os
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Email credentials
# Replace with SMTP_USERNAME
smtp_username = os.getenv("SMTP_USERNAME")
# Replace with SMTP_PASSWORD
smtp_password = os.getenv("SMTP_PASSWORD")

# SMTP settings
# Defaults to smtp.gmail.com if not found in .env
smtp_server = os.getenv("SMTP_SERVER")
# Defaults to port 587 if not found in .env
smtp_port = int(os.getenv("SMTP_PORT"))

# Make sure the username and password are set in the .env
if not smtp_username or not smtp_password:
    raise ValueError("SMTP Username or SMTP Password not found in the .env file")

# Path for certificate folder and CSV file
# Folder where certificates are saved
output_folder = "output"
# Path to the CSV file
csv_path = "templates/nama-peserta.csv"

# Read participant data from CSV with separator ;
participants = pd.read_csv(csv_path, sep=";")

# Debug: Check the columns in the CSV
print("Columns in the CSV:", participants.columns)

# Function to send email
def send_email(to_email, recipient_name):
    subject = "Sertifikat Kehadiran"
    body = f"""\
Selamat, {recipient_name}!

Sertifikat Kehadiran di anda sudah tersedia. Anda dapat mendownload pada attachment.
Terima kasih, semoga bermanfaat.

Salam,
Pengurus Event."""

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add text to the email
    msg.attach(MIMEText(body, 'plain'))

    # Path for the certificate based on name
    cert_path = os.path.join(output_folder, f"Sertifikat_{recipient_name}.png")

    # Attach the certificate if found
    if os.path.exists(cert_path):
        try:
            with open(cert_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename=Sertifikat_{recipient_name}.png",
                )
                msg.attach(part)
        except Exception as e:
            print(f"Error attaching certificate for {recipient_name}: {e}")
            return
    else:
        print(f"Certificate for {recipient_name} not found. Skipping...")
        return

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            # Use SMTP_USERNAME and SMTP_PASSWORD
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, to_email, msg.as_string())
            print(f"Email successfully sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")

# Loop through participants and send email
for _, row in participants.iterrows():
    # Check if 'nama' and 'email' columns exist in CSV
    if 'nama' in row and 'email' in row:
        name = row['nama']
        email = row['email']
        send_email(email, name)
    else:
        print(f"'nama' or 'email' column not found in this row: {row}")
