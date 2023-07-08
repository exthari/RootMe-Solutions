from pwnlib.fmtstr import *


def send_fmt_payload(payload):
    print(repr(payload))

# Create a FmtStr object and give to him the function
format_string = FmtStr(send_fmt_payload, offset=9)
format_string.write(0xbffffa58, 0xdeadbeef) # write 0x0 at 0x1337babe
print(format_string.execute_writes())
