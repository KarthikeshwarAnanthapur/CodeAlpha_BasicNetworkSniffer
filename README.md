# 🛡️ Basic Network Sniffer using Python & Scapy

A real-time network packet monitoring tool developed using Python and Scapy.  
This project captures and analyzes live network traffic to display useful packet information such as IP addresses, protocols, ports, packet sizes, and payload previews.

---

# 🚀 Features

✅ Capture live network packets  
✅ Detect TCP and UDP protocols  
✅ Display Source & Destination IP addresses  
✅ Show Source & Destination Ports  
✅ Monitor packet size in bytes  
✅ Preview packet payload data  
✅ Log captured packet details into a text file  
✅ Real-time traffic monitoring  

---

# 🧠 Concepts Explored

This project helped in understanding:

- Packet Sniffing
- Network Traffic Analysis
- TCP/IP Protocol Suite
- TCP vs UDP Communication
- IP Addressing
- Packet Structure
- Payload Inspection
- Real-Time Packet Monitoring

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming Language |
| Scapy | Packet Capturing & Analysis |
| Npcap | Packet Capture Driver for Windows |

---

# 📂 Project Structure

```txt
CodeAlpha_BasicNetworkSniffer/
│
├── sniffer.py
├── README.md
├── requirements.txt
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone <your-repository-link>
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd CodeAlpha_BasicNetworkSniffer
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Install Npcap (Windows Only)

Download and install Npcap from:

https://npcap.com/#download

✅ During installation, enable:

```txt
Install Npcap in WinPcap API-compatible Mode
```

---

# ▶️ Running the Program

```bash
python sniffer.py
```

OR

```bash
py sniffer.py
```

> ⚠️ Run terminal as Administrator for packet capture permissions.

---

# 📸 Sample Output

```txt
========================================
Packet Number : 1
Time          : YYYY-MM-DD HH:MM:SS
Source IP     : 192.168.x.x
Destination IP: 142.250.x.x
Protocol      : TCP
Source Port   : 443
Destination Port : 62543
Packet Length : 458 bytes
Payload Preview: b'...'
```

---

# 🔍 How It Works

The program continuously listens to network traffic flowing through the system using Scapy.

For each captured packet, it:
1. Identifies the IP layer
2. Extracts source & destination IP addresses
3. Detects TCP/UDP protocols
4. Reads port information
5. Displays packet metadata
6. Logs packet details for analysis

---

# 🌐 Understanding Packet Sniffing

Packet sniffing is the process of monitoring and capturing data packets traveling across a network.

This technique is commonly used in:
- Network Monitoring
- Cybersecurity Analysis
- Traffic Debugging
- Intrusion Detection
- Protocol Analysis

---

# 🎯 Internship Task Objective

This project was developed as part of a Cyber Security Internship task focused on:
- Capturing network packets
- Understanding network communication
- Learning protocol analysis
- Exploring real-time traffic monitoring

---

# ⚠️ Ethical Use Disclaimer

This project is intended strictly for:
- Educational purposes
- Ethical cybersecurity learning
- Personal network analysis

Do NOT use packet sniffing tools on unauthorized systems or networks.

---

# ⭐ Future Improvements

- Protocol Filtering
- GUI-based Interface
- Live Dashboard Visualization
- DNS/HTTP Packet Analysis
- Export Logs to CSV
- Advanced Traffic Monitoring

---

# 👨‍💻 Author

Developed by Karthikeshwar Ananthapur 🚀