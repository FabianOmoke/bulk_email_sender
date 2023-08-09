# Personalized Email Sender Script

This script is designed to send personalized emails to a list of recipients using the `smtplib` library. It reads necessary information from a DataFrame and sends emails with customized salutations and subject lines.

## Prerequisites

Before running the script, make sure you have the following:

1. Python installed on your system.
2. Required libraries: `smtplib`, `ssl`, `pandas`.

## Setup

1. Clone this repository or download the script.
2. Install the required libraries using the following command:

   ```bash
   pip install pandas

Open the script in a text editor or Python IDE.

Usage
Replace [Email Subject] in the script with your desired email subject.
Replace [Your Email] with your own Gmail email address (both sender and login).
Replace [Your Password] with the password for your Gmail account. Note: Using your actual Gmail password in the script is not secure. You might want to consider using an App Password or better yet, use environment variables for storing sensitive information.
Customize the email body by replacing [INSERT BODY HERE] with your email content.
DataFrame Format
The script assumes that you have a DataFrame named data with the following columns:

Title: Recipient's title (e.g., Mr., Mrs., Dr.).
Name: Recipient's name.
Email: Recipient's email address.
The script generates personalized salutations based on the Title and Name columns.

Running the Script
Navigate to the directory containing the script and run it using the following command:

python your_script_name.py

**Important Notes
**Using your actual email password directly in the script is not secure. Consider using environment variables or other secure methods for storing sensitive information.
Be cautious while sending a large number of emails to avoid being flagged as spam by email providers.
