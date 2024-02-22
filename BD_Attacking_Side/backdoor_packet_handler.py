"""
Author: Sp4rkN3r0
Date: 22/02/2024
Purpose: Holds the packet handler in the attacker side
"""
from scapy.all import *



class AttackerPacketHandler:
	"""
	the packet handler in the attacker side
	"""
	def __init__(self):
		pass


	def handle_packet(self, packet):
		"""
		Handles the packet
		# can be changed by the usage #
		"""
		print(packet[Raw].load.decode())