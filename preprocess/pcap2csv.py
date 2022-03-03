import sys,os


def convert(inputfile):
    cmd = 'C:\\"Program Files"\Wireshark\\tshark.exe -r {} -T fields -e frame -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -e ip.proto -e frame.protocols -e tcp.flags -e frame.len -e ip.ttl -e tcp.window_size_value -e tcp.seq -e frame.time -e frame.ignored -e frame.time_delta -z rtp,streams -E header=y -E separator=, -E quote=d -E occurrence=f > {}'
    #cmd =  'C:\\"Program Files"\Wireshark\\tshark.exe -r {} -T tabs -E header=y -E separator=, -E quote=d -E occurrence=f > {}'
    final_cmd = cmd.format(inputfile, "output.csv")
    os.system(final_cmd)


input_file = sys.argv[1]
convert(input_file)