# NETWORK SCANNER 🔍

## Description

This Python script scans a given ip or ip range for live hosts and thier MAC adresses

## Features

* Sends an ARP Request packet to hosts on the network
* Displays the  MAC addresses of the discovered hosts.

## Requirements

* Scapy for Python 2.7+
* Linux operating system

## Usage

```bash
 python3 network_scanner.py --target <ip address>
```

### Example

```bash
python3 network-scanner.py -t 192.168.1.0/24
python3 network-scanner.py --target 192.168.1.5

```

## Command-Line Options

| Option              | Description                                         |
| ------------------- | --------------------------------------------------- |
|-t, --target    | target IP Address |


