import socket
from struct import unpack
import os
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
while(1):
	packet = s.recvfrom(65565)
	packet = packet[0]
	print("+++++++++++++++++++++++++++IP HEADER+++++++++++++++++++++++++++")
	ip_header = packet[0:20]
	print("IP Header : ",ip_header)
	iph = unpack('!BBHHHBBH4s4s',ip_header)
	version_ihl = iph[0]
	version = version_ihl >> 4
	ihl = version_ihl & 0xF
	iph_length = ihl * 4
	ttl = iph[5]
	protocol = iph[6]
	s_addr = socket.inet_ntoa(iph[8])
	d_addr = socket.inet_ntoa(iph[9])
	
	print("Version : "+str(version)+ "\nIP Header Length : "+str(ihl)+ "\nTTL : "+str(ttl)+"\nProtocol : "+str(protocol)+"\nSource Address : "+str(s_addr)+ "\nDestination Address : "+str(d_addr))
	print("\n\n")
	print("+++++++++++++++++++++++++++TCP HEADER+++++++++++++++++++++++++++")
	tcp_header = packet[iph_length:iph_length+20]
	tcph = unpack('!HHLLBBHHH',tcp_header)
	source_port = tcph[0]
	dest_port = tcph[1]
	sequence = tcph[2]
	acknowledgement = tcph[3]
	doff_reserved = tcph[4]
	tcph_length = doff_reserved >> 4
	print('Source Port : '+str(source_port)+'\nDest Port : '+str(dest_port)+'\nSequence Number : '+str(sequence)+'\nAcknowledgement : ' +str(acknowledgement)+'\nTCP header length : '+str(tcph_length))
	h_size = iph_length + tcph_length * 4
	data_size = len(packet) - h_size
	data = packet[data_size:]
	print("\n\n\n+++++++++++++++++++++++++++DATA+++++++++++++++++++++++++++")
	print('\nData : '+str(data))  


