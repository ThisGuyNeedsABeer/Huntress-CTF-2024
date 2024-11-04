#!/bin/bash

python3 ~/CTF/tools/forensics/USB_Keyboard_Parser/Usb_Keyboard_Parser.py ~/CTF/huntress2024/forensics/keyboard_junkie/keyboard_junkie.pcap | grep -oE "flag{.*?}" --color=none
