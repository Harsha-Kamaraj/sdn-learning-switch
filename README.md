# SDN Learning Switch Controller

## Problem Statement
Implement an SDN controller that mimics a learning switch by dynamically 
learning MAC addresses and installing forwarding rules using Ryu + Mininet.

## Setup
1. Install Mininet: `sudo apt-get install mininet`
2. Install Ryu: `pip3 install ryu`

## How to Run
Terminal 1: `ryu-manager learning_switch.py --verbose`
Terminal 2: `sudo python3 topology.py`

## Test Scenarios
- Scenario 1: pingall (normal forwarding)
- Scenario 2: Flow table inspection with ovs-ofctl

## Expected Output
- All hosts can ping each other
- Flow rules appear in switch after first packet exchange

