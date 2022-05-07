# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it
# Chip output
# Real torque T = -500 mA
#chipTorque = 0xFE0C0000
Integer_chip_torque= -32768000


# hex 2'complement

def to_hex_2(val, nbits):
    return (val + (1 << nbits)) % (1 << nbits) 

#Output decode operation

Decode_V2 = to_hex_2(Integer_chip_torque,32)

print("first value :", Decode_V2)

# Take the torque part seconde part of the register

Torque_part = hex((Decode_V2 >> 16) & 0xFFFF)
print("The torque part:", Torque_part )

# Convert the torque part to an integer for it's display

def to_int(val, nbits):
    i = int(val, 16)
    if i >= 2 ** (nbits - 1):
        i -= 2 ** nbits
    return i

Integer_Torque = to_int(Torque_part.lstrip('0x'), 16)

print("The real torque is :", Integer_Torque)



