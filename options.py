#!/usr/bin/env
import re

''' Options used when sending IP/TCP packets,
    such as ip address src/dest, port nos src/dst,
    flags etc. '''
class Options:
    def __init__(self, opts={}):
        #valid option types
        #:NOTE: allow ip dst to have mutliple options, e.g. list of possible dst ips
        self.opt_types = {}
        self.opt_keys = ["dip", "sip", "dport", "sport"]

        return None

        self.opts = otps

        if self._is_valid() == -1: raise Exception("[-] An invalid option has been passed: {}".format(opts))

    ''' Checks only valid options are used,
        and valid data-types are used '''
    def _is_valid(self):
        if type(self.opts) != dict: return -1

        #regex expressions to check if IP/Port values are valid
        #IP regex will check contains 4 octets seperated by '.', in the range 0-255
        #Port regex checks port is between 0 and 65535
        valid_regex = {"ip": r'^(?:(?:2[0-5]{2}|[0-1]\d{2}|\d{1,2})\.){3}(?:2[0-5]{2}|[0-1]\d{2}|\d{1,2})$',
                       "port": r'^(?:6[0-5]{2}[0-3][0-5]|[0-5]\d{4}|\d{1,4})$'}

        for key in self.opts:
            if key.lower() not in self.opt_keys: return -1

            val = self.opts[key]
            if "ip" in key: k = "ip"
            elif "port" in key: k = "port"

            r = re.match(valid_regex[k], val)

            if not r: return -1

if __name__ == '__main__':
    ip = "2.555.22.22"
    r = Options().valid_ip_format(ip)
    print(r)
