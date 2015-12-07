#!/usr/bin/env python

#---------------------------------------------------------------------------#
# import the various server implementations
#---------------------------------------------------------------------------#

import time
import random
import zerorpc

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

import pdb

BASE_ADDR_MODULE_A = 0x02
BASE_ADDR_MODULE_B = 0x10

MAX_MODULE_B_COUNT = 16

client = ModbusClient(method='ascii', port='/dev/pts/9', retries=1)

b_list = []
def scan_modules():
    '''Scan active modules on the bus'''
    client.connect(MAX_MODULE_B_COUNT)
    for i in xrange(3):
        rr = client.read_input_registers(0x1051, 1, unit=BASE_ADDR_MODULE_B + i)
        if rr is not None and rr.function_code < 0x80:
            b_list.append(BASE_ADDR_MODULE_B + i)
    client.close()
    return umn_list

class moduleRPC(object):
    def get_umns(self):
        return scan_modules()
    def read_coils_b(self, addr):
        client.connect()
        rq = client.read_coils(regs_b_coils["REG_COILS_B_T1"] - 1, 1, unit=addr)
        rr = client.read_coils(regs_b_coils["REG_COILS_B_T2"] - 1, 4, unit=addr)
        client.close()
        if rq.bits[0]:
            reg = (1 << 0)

        for i in range(4):
            if rr.bits[i]:
                reg |= (1 << (i+1))
        return reg

    def set_coil_b(self, addr):
        client.connect()
        client.write_coil(regs_b_coils["REG_COILS_B_T1"] - 1, random.randint(0, 1), unit=addr)
        client.close()

    def read_input_b(self, addr):
        client.connect()
        rr = client.read_input_registers(regs_umn["REG_INPUT_B_VERSION"] - 1, len(regs_b_input), unit=addr)
        client.close()
        if rr.function_code < 0x80:
            return [r for r in rr.registers]

    def read_hold_b(self, addr):
        client.connect()
        rr = client.read_holding_registers(regs_umn["REG_HOLDING_B_T1"] - 1, len(regs_b_holding), unit=addr)
        client.close()
        if rr.function_code < 0x80:
            return [r for r in rr.registers]

    def set_hold_b(self, addr):
        client.connect()
        rq = client.write_register(0x0082 - 1, random.randint(1, 100), unit=addr)
        client.close()
        return 200

umn = zerorpc.Server(RPC())
umn.bind("tcp://0.0.0.0:4343")
umn.run()

