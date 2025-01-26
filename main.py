import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    # Email configuration
    sender_email = "atharvsankpal799@gmail.com"
    sender_password = "PASSWORD"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP("smtp.gmail.com", 587)  # Use Gmail SMTP server
    session.starttls()  # Enable security
    session.login(sender_email, sender_password)  # Login with credentials

    # Send email
    session.sendmail(sender_email, to_email, message.as_string())

    # Close the session
    session.quit()

    print("Email sent successfully!")

if __name__ == "__main__":
    subject = "Test Email"
    body = "This is a test email sent using Python."
    to_email = "atharvsankpal69420@gmail.com"
    send_email(subject, body, to_email)
