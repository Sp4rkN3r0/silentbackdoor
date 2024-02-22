# Pay Attention:
the program is currently sniffing on the first interface that can be found (mostly eth0) you can specify a specific interface in the scapy settings or by adding "iface=<INTERFACE>" in the places scapy sniffs, or send packets!

# Author:
Sp4rkn3r0
# License:
MIT

# SilentBackDoor
a backdoor that does not capture a port on the pc, so no one will see that a backdoor exists...

# Usage
the main operation of the backdoor is to use scapy and sniff for packets without capturing the port, the commands are currently being separated from the arguments using : and the arguments are being passed as string.
for example, currently, we have the command is_alive to check if the backdoor is alive.
to run the command send from the attacker PC the command:
is_alive:
pay attention even if we don't have parameters we have to add the ":" and the function has to get args because it is being held in a dict for easy functions adding.
