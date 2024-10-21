from scapy.all import *


ping = ICMP(type=8)


packet = IP(src="10.6.1.137", dst="10.6.1.254")


frame = Ether(src="08:00:27:c2:a9:42", dst="08:00:27:66:7b:b2")


final_frame = frame/packet/ping


answers, unanswered_packets = srp(final_frame, timeout=10)


print(f"Pong reçu : {answers[0]}")