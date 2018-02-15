#!/usr/bin/env python3
import subprocess

#TODO: Add support for windows

''' Returns a list of avaiable network interfaces'''
def get_interfaces():
    ifconfig = subprocess.getoutput("ifconfig").split("\n\n")
    interfaces = [i.split(":")[0] for i in ifconfig]

    return interfaces
