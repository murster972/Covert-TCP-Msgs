#!/usr/bin/env python3
from interfaces import get_interfaces
from scapy.all import *

class Receiver:
    def __init__(self, l, options={}, constants=[]):
        self.constants = constants
        self.seg_size = l

        #temp stores segs recieved untill all segs sent by user
        #are recieved
        self.cur_segs = {}
        self.expected_segs = 0

        #this will indicate if the user is sending ascii or binary
        #ascii is 0 binary 1
        self.MODE = 0

        interfaces = get_interfaces()

        #p_filter = "tcp and port " + str(options["dst"])
        p_filter = "tcp and port 80"
        p_interface = "wlp3s0"

        sniffer = sniff(filter=p_filter, iface=p_interface, prn=self._receive_segments)

    ''' Handles any packets received '''
    def _receive_segments(self, packet):
        #cheks if packet is from sender
        print(packet.summary())

        #if not, discards

        #else

        #decodes

        #if all flags set to 1, it indicates segs about to be sent
        #   and has info about segs, no of segs etc.

        #if ascii msg converts back to ascii

        #if binary stores in new file

    ''' Decodes segments '''
    def _decode_msg(self, segs):
        pt = []
        cnst_ind = 0

        for seg in segs:
            #s = bin(int(seg, 2) ^ self.constants[cnst_ind])[2:]

            bin_c = bin(self.constants[cnst_ind])[2:]

            s = self._bin_xor(seg, bin_c)

            pt.append(s)

            cnst_ind += 1
            if cnst_ind >= len(self.constants): cnst_ind = 0

        return pt

    ''' Padds a binary string so it can be divided into blocks of length l
        :param m: binary string
        :param l: length to padd to
        :output str: padded binary string '''
    def _padd_bin(self, m, l):
        padd = l - (len(m) % l)

        #stops msgs already multiple of length l being padded
        if padd == l: padd = 0

        return ("0" * padd) +  m

    ''' Xors binary strings, b1 ^ b2

        This is used when decoding segments as it
        ensures segs are correct bit length once
        XORd, unlike converting to int XORing then
        converting back to bin.

        :parm b1, b2: binary strings
        :output str: binary string b1 ^ b2 '''
    def _bin_xor(self, b1, b2):
        l1, l2 = len(b1), len(b2)
        if l1 > l2:
            b2 = ("0" * (l1 - l2)) + b2
        elif l2 > l1:
            b1 = ("0" * (l2 - l1)) + b1

        result = ""

        for i in range(l1):
            b = int(b1[i], 2) + int(b2[i], 2)
            result += str(b % 2)

        return result

def test(x):
    d = x.show()

    if d:
        for i in d: print(i)

def main():
    interface="lo"
    p = sniff(filter="tcp and port 66", iface=interface, prn=lambda x:test(x))

if __name__ == '__main__':
    Receiver(21, constants=[1])

    # const = [21, 127, 1]
    # #segs = ['00011101', '01000110', '01111000', '11100001']
    # segs = ['00011101', '01010011', '01111000', '11100001']
    # x = Receiver(21, constants=const)
    # pt = "".join(x._decode_msg(segs))
    #
    # pt = x._padd_bin(pt.lstrip("0"), 7)
