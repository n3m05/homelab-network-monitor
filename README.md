# 🛡️ Homelab Network Watchdog

A Python-based infrastructure monitoring tool that bridges the gap between System Administration and Software Development. This tool performs lightweight ICMP health checks on local devices and provides real-time alerts.

## 📝 Overview
This project was built to automate the manual task of checking server uptime in my homelab. It utilizes a `servers.txt` configuration file for scalability and environment variables for secure API credential management.

## 🚀 Features
- **Automated Health Checks:** Pings a list of IPs defined in a local configuration file.
- **Security First:** Utilizes `python-dotenv` to keep API tokens out of the source code.
- **Linux Integration:** Leverages native system calls for high-performance network probing.

## 🛠️ Setup & Installation
1. Clone the repository.
2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

   🔍 Engineering Log: Troubleshooting & Known Issues
During development, a ConnectTimeoutError was identified when attempting to reach the Telegram API (api.telegram.org) from certain local network segments.
Status: Under Investigation
* Diagnosis: The script successfully performs local pings, but outbound HTTPS requests to the Telegram API are currently being dropped by the local gateway or firewall.
* Resolution Path: Implemented a robust try...except block with a 10-second timeout to prevent script hanging. Future iterations may include a proxy configuration or a secondary alerting method (e.g., local logging/email) to bypass API-specific network blocks.
👨‍💻 Author
Scott Niemi System Administrator | Aspiring Full Stack Developer