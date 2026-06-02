# 🕵️ ARP Spoofer

## 📖 Description

This project is a Python-based ARP spoofing tool developed for educational purposes and authorized network security testing. It demonstrates how Address Resolution Protocol (ARP) poisoning can manipulate ARP tables within a local network.

The tool continuously sends forged ARP replies between two hosts, causing each host to associate the attacker's MAC address with the other host's IP address.

## ✨ Features

* 🔍 Automatic MAC address discovery
* 📡 ARP request and reply packet generation using Scapy
* 🔄 Continuous ARP poisoning
* 📊 Real-time packet counter
* ⌨️ Graceful shutdown with `Ctrl + C`
* 🛠️ Simple command-line interface

## 📋 Requirements

* Python 3
* Scapy

Install Scapy:

```bash
pip install scapy
```

## 🚀 Usage

Run the script with the IP addresses of the two target hosts:

```bash
python3 arp_spoof --victim1 192.168.1.123 --victim2 192.168.1.1
```

### Arguments

| Argument    | Description                     |
| ----------- | ------------------------------- |
| `--victim1` | IP address of the first target  |
| `--victim2` | IP address of the second target |

### Example

```bash
python3 arp_spoof --victim1 192.168.1.50 --victim2 192.168.1.1
```

## ⚙️ How It Works

1. 🖥️ The user provides two target IP addresses.
2. 🔍 The program discovers their MAC addresses using ARP requests.
3. 📨 Forged ARP replies are sent to both targets.
4. 🔄 The process repeats periodically to maintain the poisoned ARP entries.
5. 📈 A packet counter displays the number of packets sent.

## 📁 Project Structure

```text
arp_spoofer/
│
├── arp_spoof
└── README.md
```

## 📝 Notes

* Run the script with administrator/root privileges.
* Both targets must be on the same local network.
* ARP spoofing only works within a local broadcast domain.
* Consider restoring ARP tables after testing to return the network to its normal state.

## ⚠️ Disclaimer

This project is intended for educational purposes, cybersecurity training, and authorized security testing only. Use it exclusively on networks and systems for which you have explicit permission. Unauthorized use may violate laws, regulations, or organizational policies.
