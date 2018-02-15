#!/usr/bin/env python3
from interfaces import get_interfaces
from argparse import ArgumentParser
from scapy.all import *

#NOTE: bounce method working, but not other, think Because
#       on private vlan
#NOTE: Because the virtual machine is using same ethernet, wireshark
#      in the VM will also show traffic from host machine, i.e. laptop

#TODO: check segents are properly encoded


#TODO: test packets and encoded and sent properly!


class Sender:
    TCP_SEQ_SIZE = 32

    def __init__(self, msg, method, constants, options={}):
        self.msg = msg
        self.method_no = method
        self.constants = constants
        self.options = options

        #this will indicate if the user is sending ascii or binary
        #ascii is 0 binary 1
        self.MODE = 0

        self.seg_l = 8

        #the keys for options used in tcp or ip
        self.ip_opts = ["dst", "src"]
        self.tcp_opts = ["dport", "sport"]

        self._check_options()

        if type(self.constants) != list or len(self.constants) < 1:
            raise Exception("--INSERT ERROR MSG--")

        #NOTE: constants cannot be larger than 2**l - 1
        #      or the result of seg XOR constant will be
        #      larger than length l.
        for i in self.constants:
            if type(i) != int: raise Exception("--INSERT ERROR MSG--")
            if i > (2**self.seg_l) - 1: raise Exception("--INSERT ERROR MSG--")

        self.send_segements()

    ''' Converts msg to binary, encodes and sends each segment '''
    def send_segements(self):
        #converts msg to binary and encodes
        bin_m = self._msg_to_bin()
        segs = self._encode_msg(bin_m)

        print(segs)

        exit()

        #size of seg no.
        no_size = Sender.TCP_SEQ_SIZE - self.seg_l

        if len(segs) > 2**no_size - 1:
            return Exception("[-] Segment Error: not enough IDs to identify each segment.")

        for i in range(len(segs)):
            seg_no = bin(i + 1)[2:]
            SEQ_NO = self._padd_bin(seg_no + segs[i], Sender.TCP_SEQ_SIZE)

            #creates packet and applies options - dest/src port, ip etc.
            ip = IP()
            tcp = TCP()

            for key in self.ip_opts:
                if key not in self.options: continue
                ip.key = self.options[key]

            for key in seasierelf.tcp_opts:
                if key not in self.options: continue
                tcp.key = self.options[key]

            send(ip/tcp)

    ''' Segements encoded msg into blocks of size l and multiplies by constant/s
        :param enc_m: msg to encode (in binary)
        :output list: list of segements, in order'''
    def _encode_msg(self, enc_m):
        #TODO: regex to check for binary

        if type(self.seg_l) != int or self.seg_l < 1 or len(self.constants) < 1:
            raise Exception("--INSERT ERROR MSG--")

        #padd enc_msg to match segement size
        padd_m = self._padd_bin(enc_m, self.seg_l)

        segments = []
        cnst_ind = 0

        for i in range(self.seg_l, len(padd_m) + 1, self.seg_l):
            #get seg of length l and xor with current constant
            seg = bin(int(padd_m[i - self.seg_l:i], 2) ^ self.constants[cnst_ind])[2:]
            seg = self._padd_bin(seg, self.seg_l)

            segments.append(seg)

            cnst_ind += 1
            if cnst_ind == len(self.constants): cnst_ind = 0

        return segments

    ''' Converts msgs to bits
        :param msg: msg (in ascii chars) to be converted
        :outout str: encodes msg (in bits)'''
    def _msg_to_bin(self):
        if len(self.msg) == 0 or type(self.msg) != str: return 0

        b_msg = ""

        for i in self.msg:
            b = bin(ord(i))[2:]
            b_msg += self._padd_bin(b, 7)

        return b_msg

    ''' Padds a binary string so it can be divided into blocks of length l
        :param m: binary string
        :param l: length to padd to
        :output str: padded binary string '''
    def _padd_bin(self, m, l):
        padd = l - (len(m) % l)

        #stops msgs already multiple of length l being padded
        if padd == l: padd = 0

        return ("0" * padd) +  m

    ''' Checks that the options choosen for the packet are correct '''
    def _check_options(self):
        #every option possible and its type
        #opt_keys = {"dst": lambda}
        pass

def main():
    #get any cmdline args
    parser = ArgumentParser()

    parser.add_argument("--DIP", type=str, help="Destination IP address", default="")
    parser.add_argument("--SIP", type=str, help="Source IP address", default="")
    parser.add_argument("--DPort", type=int, help="Destination Port no.", default=0)
    parser.add_argument("--SPort", type=int, help="Source Port no.", default=0)

    args = parse.parse_args()

    #get any required options not passed - e.g. dest IP, method, msg, etc.

    #get constants - if any used

if __name__ == '__main__':
    #TODO: GO THROUGH IT STEP BY STEP CHECKING EACH MODULE is working CORRECTLY
    msg = "A1st"
    method = -1
    const = [21, 127, 1]
    t = Sender(msg, method, constants=const)
