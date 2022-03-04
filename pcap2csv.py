import sys,os

def exec(input_file, user_os):
    def convert(inputfile,user_os,filepath='C:\\"Program Files"\Wireshark\\tshark.exe'):
        if user_os == "win":
            cmd = filepath + ' -r {} -T fields -e frame -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -e ip.proto -e frame.protocols -e tcp.flags -e frame.len -e ip.ttl -e tcp.window_size_value -e tcp.seq -e frame.time -e frame.ignored -e frame.time_delta -E header=y -E separator=, -E quote=d -E occurrence=f > {}'

        elif user_os == "mac":
            cmd = 'tshark -r {} -T fields -e frame -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -e ip.proto -e frame.protocols -e tcp.flags -e frame.len -e ip.ttl -e tcp.window_size_value -e tcp.seq -e frame.time -e frame.ignored -e frame.time_delta -E header=y -E separator=, -E quote=d -E occurrence=f > {}'
        else:
            return

        final_cmd = cmd.format(inputfile, "static/files/preprocess.csv")
        os.system(final_cmd)


    #input_file = sys.argv[1]
    #user_os = sys.argv[2]

    if len(sys.argv)>3:
        filepath = sys.argv[3]

    oslist=["win","mac"]
    if user_os not in oslist:
        print("os not compatible of now")
        exit

    convert(input_file,user_os)
