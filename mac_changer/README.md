# MAC Changer

## Description

This Python script changes the MAC address of a network interface on Linux systems using the `ifconfig` command. It allows users to specify the target interface and a new MAC address through command-line arguments.

## Features

* Displays the current MAC address of the selected interface.
* Validates the format of the new MAC address.
* Changes the MAC address of the specified interface.
* Verifies whether the MAC address was changed successfully.

## Requirements

* Python 3.x
* Linux operating system
* `ifconfig` utility installed
* Root privileges (sudo)

## Usage

```bash
sudo python3 mac_changer.py -i <interface> -m <new_mac>
```

### Example

```bash
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

## Command-Line Options

| Option              | Description                                         |
| ------------------- | --------------------------------------------------- |
| `-i`, `--interface` | Network interface whose MAC address will be changed |
| `-m`, `--mac`       | New MAC address                                     |

## Output Example

```text
--------------- mac changer ------------
current mac-> 08:00:27:12:34:56
[+] changing interface eth0 mac to 00:11:22:33:44:55
[+] mac changed successfully
changed mac-> 00:11:22:33:44:55
```

## Notes

* Run the script with administrator privileges.
* The script uses regular expressions to validate MAC address format.
* Changes made are temporary and may be reset after a system reboot or network restart.
* Some network interfaces or drivers may not support MAC address changes.

## Disclaimer

Use this tool only on systems and networks you own or are authorized to test. Unauthorized modification of network settings may violate organizational policies or local laws.
