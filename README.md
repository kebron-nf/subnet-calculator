# 🛡️ Ultimate Python Subnet Tool

A colorful, interactive, command-line network utility built in Python. Designed for network engineers, students, and cybersecurity enthusiasts to calculate IPv4 subnets, split networks into smaller chunks, and test their skills with a built-in quiz mode.

---

## ✨ Features

- **Single Network Analysis:** Instantly calculates Network IDs, Subnet Masks, Broadcast IPs, CIDR notation, Total IPs, Usable Hosts, Usable IP Ranges, and their **Binary** equivalents.
- **Network Splitter:** Breaks any parent network down into a specific number of subnets (dynamically calculates borrowed bits and new CIDR prefixes).
- **Subnet Quiz Mode:** An interactive mini-game that randomly generates subnetting challenges to test your broadcast, mask, and host calculations with live score tracking.
- **Terminal UI:** Beautiful, color-coded output using ANSI escape codes for a real hacker/terminal aesthetic.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3** installed on your system (works out of the box on Linux, macOS, and Windows since it uses Python's built-in libraries).

### Installation & Execution

1. Clone or download the script into your working directory:
   ```Bash
   git clone https://github.com/kebron-nf/first-/blob/main/subnet3_tool.py
   ```
Run the tool:
   ```Bash

    python3 subnet_tool.py

   ```
🎮 How to Use

When you launch the script, you will be greeted with an interactive menu:
Plaintext

╔══════════════════════════════════════════════════╗
║             ULTIMATE PYTHON SUBNET TOOL          ║
║         [ Calculator, Splitter & Quiz ]          ║
╚══════════════════════════════════════════════════╝

Choose an option:
  1) Single Network Analysis (with Binary & Hosts)
  2) Split Network into Smaller Subnets
  3) Subnet Quiz Mode (Test Yourself)
  4) Exit tool

    Option 1: Enter an IP with CIDR (e.g., 10.200.20.0/27) to see a full breakdown.

    Option 2: Enter a parent network and how many subnets you want (e.g., 2,3 or more ) to view the newly divided subnets.

    Option 3: Jump into Quiz Mode to practice your subnetting skills on the fly! Type q to exit the quiz anytime.

🛠️ Built With

    Python 3

    Built-in ipaddress and random libraries.
