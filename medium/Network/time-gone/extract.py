import pyshark

capture = pyshark.FileCapture('ntp_payload.pcap', display_filter='ntp.flags.mode == 4 && udp.srcport == 123')

field_name = 'ntp.refid'
flag = ""

for pkt in capture:
    ref_id = pkt.ntp.get_field_value(field_name).split(":")[0]
    flag += bytes.fromhex(ref_id).decode('ascii')
flag = flag[2:len(flag)-2]
print(flag)
