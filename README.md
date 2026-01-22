# Homelab Network Watchdog 🛡️

A Python-based infrastructure monitoring tool designed to automate device availability checks and provide real-time alerts. This project demonstrates operational skills in network monitoring, alerting, and automation, bridging system administration and software development practices.

## Overview
This tool monitors devices on a local network, performing lightweight ICMP health checks on configured hosts. Real-time notifications are delivered via Telegram to ensure rapid awareness of potential outages. It is designed to simulate small-to-mid enterprise network monitoring in a lab or home environment.

## Features
- **Automated Health Checks**: Pings a list of IPs defined in a `servers.txt` configuration file.
- **Real-Time Alerting**: Sends notifications via Telegram when a device becomes unreachable.
- **Secure Credential Management**: Uses environment variables and `python-dotenv` to keep API tokens out of source code.
- **Lightweight & Efficient**: Leverages native system calls for fast network probing with minimal overhead.

## Installation & Setup
```bash
# Clone the repository
git clone https://github.com/n3m05/network-watchdog.git
cd network-watchdog

# Create virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
