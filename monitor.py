import os
import requests
from dotenv import load_dotenv

# Load secrets
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_msg(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        # We add a 10-second timeout here
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            print("📱 Telegram notification sent!")
        else:
            print(f"⚠️ Telegram returned an error: {response.status_code}")
    except requests.exceptions.Timeout:
        print("❌ Error: Telegram API timed out. Check your internet connection.")
    except Exception as e:
        print(f"❌ Failed to send Telegram alert: {e}")

def check_homelab():
    # 1. Setup the path
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "servers.txt")

    # 2. Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: Could not find {file_path}")
        return

    # 3. Read and Ping (Everything below is indented inside the function)
    with open(file_path, "r") as file:
        for line in file:
            ip = line.strip()
            if not ip: 
                continue 
            
            # Run the ping command
            status = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
            
            if status == 0:
                print(f"✅ {ip} is online.")
            else:
                print(f"❌ {ip} is DOWN! Sending alert...")
                send_telegram_msg(f"🚨 ALERT: Homelab device {ip} is unreachable!")

# 4. The 'Start Button' for your script
if __name__ == "__main__":
    check_homelab()