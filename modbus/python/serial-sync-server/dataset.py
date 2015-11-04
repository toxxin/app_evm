__author__ = 'Anton Glukhov'

import random

from regs import *
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSparseDataBlock


block_disc_a = ModbusSequentialDataBlock(regs_ksk["REG_DISC_A"], [0]*25)
block_coils_a = ModbusSequentialDataBlock(regs_ksk["REG_COILS_A"], [1]*18)
block_input_a = ModbusSequentialDataBlock(regs_ksk["REG_INPUT_A"], [random.randint(0,100) for x in range(92)])
block_holding_a = ModbusSequentialDataBlock(regs_ksk["REG_HOLDING_A"], [random.randint(0,100) for x in range(8)])


block_disc_b1 = ModbusSequentialDataBlock(regs_umn["REG_DISC_B"], [0]*8)
block_coils_b1 = ModbusSparseDataBlock({0x0083: 1, 0x0100: 1, 0x0101: 0, 0x0102: 1, 0x0103: 1})
block_input_b1 = ModbusSequentialDataBlock(regs_umn["REG_INPUT_B"], [random.randint(0,100) for x in range(len(10))])
block_holding_b1 = ModbusSequentialDataBlock(regs_umn["REG_HOLDING_B"], [random.randint(0,100) for x in range(len(10))])

block_disc_b2 = ModbusSequentialDataBlock(regs_umn["REG_DISC_B"], [1]*8)
block_coils_b2 = ModbusSparseDataBlock({0x0083: 1, 0x0100: 1, 0x0101: 0, 0x0102: 1, 0x0103: 1})
block_input_b2 = ModbusSequentialDataBlock(regs_umn["REG_INPUT_B"], [random.randint(0,100) for x in range(17)])
block_holding_b2 = ModbusSequentialDataBlock(regs_umn["REG_HOLDING_B"], [random.randint(0,100) for x in range(3)])

block_disc_b3 = ModbusSequentialDataBlock(regs_umn["REG_DISC_B"], [1]*8)
block_coils_b3 = ModbusSparseDataBlock({0x0083: 1, 0x0100: 1, 0x0101: 0, 0x0102: 1, 0x0103: 1})
block_input_b3 = ModbusSequentialDataBlock(regs_umn["REG_INPUT_B"], [random.randint(0,100) for x in range(5)])
block_holding_b3 = ModbusSequentialDataBlock(regs_umn["REG_HOLDING_B"], [random.randint(0,100) for x in range(2)])
