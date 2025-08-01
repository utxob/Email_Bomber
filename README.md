# Email_Bomber

# Email Bomber Tool

A simple Python script that sends multiple emails to a target email address by rotating through multiple Gmail sender accounts.

## ⚠️ Important Notice

- This tool is for educational and testing purposes only.
- **Do NOT use it for spamming, harassment, or any illegal activities.**
- Misuse may lead to account suspension or legal consequences.

## Features

- Supports multiple Gmail sender accounts (with App Passwords)
- Rotates senders to avoid Gmail rate limits
- Unique Message-ID in each email to reduce threading
- Adjustable delay between emails to control sending speed
- Simple command-line interface

## Requirements

- Python 3.6+
- Internet connection
- Gmail accounts with App Passwords enabled (2FA required)

## Installation

1. Make sure Python 3 is installed on your system. You can download it from [python.org](https://python.org).
2. Clone or download this script.
3. Install dependencies (if not installed):


```bash
pip install --upgrade pip
pip install secure-smtplib email
```


## Interactive Usage Example

When you run the script, you'll see a step-by-step interface like this:

```bash
$ python Email_bot.py
```
📧 EMAIL BOMBER TOOL (Educational Use Only) 📧

1. Enter number of sender Gmail accounts: 2

[Account 1]
- Gmail address: sender1@gmail.com
- App Password: ********

[Account 2] 
- Gmail address: sender2@gmail.com
- App Password: ********

2. Enter target email address: target@example.com
3. Number of emails to send: 10
4. Enter email body text:
   This is a test email sent through the bomber tool.
   You can write multiple lines here.

🚀 Starting email sending process...
[1/10] Sent using sender1@gmail.com (Waiting 5s...)
[2/10] Sent using sender2@gmail.com (Waiting 5s...)
[3/10] Sent using sender1@gmail.com (Waiting 5s...)
...
✅ Done! 10 emails sent successfully.

```bash
pip install --upgrade pip
pip install secure-smtplib email
