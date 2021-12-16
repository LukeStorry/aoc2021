
from collections import deque
from math import prod

packets = []

class Packet:
    def __init__(self, bits: deque[int]) -> None:
        def take(n): return [bits.popleft() for _ in range(n)]
        def bits_to_int(bl): return int(''.join(str(b) for b in bl), 2)
        
        packets.append(self)
        self.version = bits_to_int(take(3))
        self.type_id = bits_to_int(take(3))

        if self.type_id == 4:  # Literal
            value_bits = []
            while True:
                start, *remainder = take(5)
                value_bits += remainder
                if start == 0:
                    break
            self.value = bits_to_int(value_bits)

        else:  # Operator
            self.subpackets = []
            match take(1):
                case [0]:
                    subpackets_length = bits_to_int(take(15))
                    start_bit_length = len(bits)
                    while len(bits) > start_bit_length - subpackets_length:
                        self.subpackets.append(Packet(bits))
                case [1]:
                    subpackets_count = bits_to_int(take(11))
                    while len(self.subpackets) < subpackets_count:
                        self.subpackets.append(Packet(bits))

            match self.type_id:
                case 0: self.value = sum(s.value for s in self.subpackets)
                case 1: self.value = prod(s.value for s in self.subpackets)
                case 2: self.value = min(s.value for s in self.subpackets)
                case 3: self.value = max(s.value for s in self.subpackets)
                case 5: self.value = 1 if self.subpackets[0].value > self.subpackets[1].value else 0
                case 6: self.value = 1 if self.subpackets[0].value < self.subpackets[1].value else 0
                case 7: self.value = 1 if self.subpackets[0].value == self.subpackets[1].value else 0
    
    def __repr__(self) -> str:
        return f"<{'Literal' if self.type_id == 4 else 'Operator ' + str(self.type_id)} Packet (version {self.version}) with value {self.value}>"


def hex_to_bits(hex_str: str) -> deque[int]:
    return deque(int(bit) for char in hex_str for bit in bin(int(char, 16))[2:].zfill(4))

packet = Packet(hex_to_bits(open("inputs/16.txt").read()))

print(sum(p.version for p in packets))
print(packet.value)
