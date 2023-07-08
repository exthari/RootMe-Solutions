import struct
  
a = '00000020#0804b160#0804853d#00000009#bffffc6b#b7e1b589#bffffb34#b7fc3000#b7fc3000#0804b160#39617044#28293664#6d617045#bf000a64#0804861b#00000002#bffffb34#bffffb40#115cf300#bffffaa0#00000000#00000000#b7e03f21#b7fc3000#b7fc3000#00000000#b7e03f21#00000002#bffffb34#bffffb40#bffffac4#00000001#00000000#b7fc3000#b7fe771a#b7fff000#00000000#b7fc3000#00000000#00000000'
b = a.split("#")
  
for add in b:
        #to convert little endian to big-endian
        try:
                i=bytes.fromhex(add)
                #print(i.decode("utf-8"),end="")
                print(i.decode()[::-1] ,end="")

        except:
                pass
