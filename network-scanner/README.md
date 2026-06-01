# NETWORK SCANNER 🔍

## Description

This Python script scans a given ip or ip range for live hosts and thier MAC adresses

## Features

* Sends an ARP Request packet to hosts on the network
* Displays the  MAC addresses of the discovered hosts.

## Requirements

* Python 3.x
* Linux operating system

## Usage

```bash
 python3 network_scanner.py --ip <ip address>
```

### Example

```bash
python3 network-scanner.py --ip 192.168.1.0/24
python3 network-scanner.py --ip 192.168.1.5

```

## Command-Line Options

| Option              | Description                                         |
| ------------------- | --------------------------------------------------- |
| --ip    |IP Address |


