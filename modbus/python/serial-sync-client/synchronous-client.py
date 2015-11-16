#!/usr/bin/env python

#---------------------------------------------------------------------------#
# import the various server implementations
#---------------------------------------------------------------------------#

import time
import random

from pymodbus.client.sync import ModbusSerialClient as ModbusClient

from regs import *
import sqlite3

#---------------------------------------------------------------------------#
# configure the client logging
#---------------------------------------------------------------------------#
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

BASE_ADDR_MODULE_A = 0x02
BASE_ADDR_MODULE_B = 0x10

MAX_MODULE_B_COUNT = 16

client = ModbusClient(method='rtu', port='/dev/pts/11', retries=1)

b_list = []
def scan_modules():
    '''Scan active modules on the bus'''
    client.connect(MAX_MODULE_B_COUNT)
    for i in xrange():
        rr = client.read_input_registers(0x1051, 1, unit=BASE_ADDR_MODULE_B + i)
        if rr is not None and rr.function_code < 0x80:
            print BASE_ADDR_MODULE_B + i
            b_list.append(BASE_ADDR_MODULE_B + i)
    client.close()
    return b_list


if __name__ == '__main__':
    print "Scan b moudles..."
    #b_list = []
    #b_list = scan_modules()
    print "Start polling..."
    while 1:
        pass
        time.sleep(1)
