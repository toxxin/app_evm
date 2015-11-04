#!/usr/bin/env python
'''
Pymodbus Synchronous Test Server
--------------------------------------------------------------------------

The synchronous server is implemented in pure python without any third
party libraries (unless you need to use the serial protocols which require
pyserial). This is helpful in constrained or old environments where using
twisted just is not feasable.
'''
#---------------------------------------------------------------------------# 
# import the various server implementations
#---------------------------------------------------------------------------# 
from pymodbus.server.sync import StartTcpServer
from pymodbus.server.sync import StartUdpServer
from pymodbus.server.sync import StartSerialServer

from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

from pymodbus.transaction import ModbusRtuFramer
#---------------------------------------------------------------------------# 
# configure the service logging
#---------------------------------------------------------------------------# 
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

BASE_ADDR_MODULE_A = 0x02
BASE_ADDR_MODULE_B = 0x10

store_a = ModbusSlaveContext(
    di = block_disc_a,
    co = block_coils_a,
    hr = block_holding_a,
    ir = block_input_a)

store_b1 = ModbusSlaveContext(
    di = block_disc_b1,
    co = block_coils_b1,
    hr = block_holding_b1,
    ir = block_input_b1)

store_b2 = ModbusSlaveContext(
    di = block_disc_b2,
    co = block_coils_b2,
    hr = block_holding_b2,
    ir = block_input_b2)


store_b3 = ModbusSlaveContext(
    di = block_disc_b3,
    co = block_coils_b3,
    hr = block_holding_b3,
    ir = block_input_b3)

slaves = {
    BASE_ADDR_MODULE_A: store_a,

    BASE_ADDR_MODULE_B: store_b1,
    BASE_ADDR_MODULE_B+1: store_b2,
    BASE_ADDR_MODULE_B+5: store_b3,
}

context = ModbusServerContext(slaves=slaves, single=False)

#---------------------------------------------------------------------------# 
# initialize the server information
#---------------------------------------------------------------------------# 
# If you don't set this or any fields, they are defaulted to empty strings.
#---------------------------------------------------------------------------# 
identity = ModbusDeviceIdentification()
identity.VendorName  = 'Pymodbus'
identity.ProductCode = 'PM'
identity.VendorUrl   = 'http://github.com/bashwork/pymodbus/'
identity.ProductName = 'Pymodbus Server'
identity.ModelName   = 'Pymodbus Server'
identity.MajorMinorRevision = '1.0'

#---------------------------------------------------------------------------# 
# run the server you want
#---------------------------------------------------------------------------# 
# Ascii:
#StartSerialServer(context, identity=identity, port='/dev/pts/36', timeout=1)

# RTU:
#StartSerialServer(context, framer=ModbusRtuFramer, identity=identity, port='/dev/pts/36', timeout=.005)
StartSerialServer(context, identity=identity, port='/dev/pts/36', timeout=.005)
