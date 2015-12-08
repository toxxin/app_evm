import zerorpc

b = zerorpc.Client()
b.connect("tcp://127.0.0.1:4343")
print b.geti_modules()
print b.read_coils_b(0x20)
print b.read_hold_b(0x20)
print b.set_hold_b(0x20)
print b.read_hold_b(0x20)
