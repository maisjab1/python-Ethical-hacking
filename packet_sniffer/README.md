# HTTP Packet Sniffer

A simple network packet sniffer built with Scapy that captures HTTP requests and POST data on a specified interface.

## Requirements

- Python 3
- Scapy

```bash
pip install scapy
```

## Usage

```bash
sudo python packet_sniffer.py -i <interface>
```

### Options

| Flag | Description |
|------|-------------|
| `-i`, `--iface` | Network interface to sniff on (required) |
| `-h`, `--help` | Show help message |

### Examples

```bash
sudo python packet_sniffer.py -i eth0
sudo python packet_sniffer.py -i wlan0
```

## What It Captures

- **HTTP GET/POST requests** — method, full URL (host + path)
- **POST body** — form data including credentials sent in plaintext
- **TCP segments** — catches POST bodies that arrive in separate TCP packets

## Demo

### 1. Start the login server

```bash
python login.py
```

You should see:
```
* Running on http://0.0.0.0:8080
```

### 2. Start the sniffer (in a separate terminal)

```bash
sudo python packet_sniffer.py -i eth0
```

### 3. Open the login page in your browser

```
http://<your-ip>:8080
```

### 4. Submit the login form

Enter any username and password and hit Login. The sniffer terminal should print:

```
[POST] http://10.0.2.3:8080/login
[POST BODY] username=alice&password=hunter2
```

## Example Output

```
[*] Sniffing on eth0...

[GET] http://example.com/index.html
[POST] http://10.0.2.3:8080/login
[POST BODY] username=alice&password=hunter2
```

## Notes

- Must be run as **root** (`sudo`) for raw socket access
- Only captures **unencrypted HTTP** traffic — HTTPS traffic is encrypted and unreadable
- For use on networks and machines you own or have explicit permission to monitor

## Project Structure

```
packet_sniffer/
├── packet_sniffer.py   # main sniffer script
├── login.py            # test Flask login server
└── README.md
```
