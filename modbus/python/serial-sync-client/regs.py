__author__ = 'Anton Glukhov'


regs_a_disk = [
    "REG_DISC_A_T1", "REG_DISC_A_T2", "REG_DISC_A_T3", "REG_DISC_A_T4"
]

regs_a_coils = [
    "REG_COILS_A_T1", "REG_COILS_A_T2", "REG_COILS_A_T3",
    "REG_COILS_A_T4", "REG_DISC_A_T5"
]

regs_a_input = [
    "REG_INPUT_A_T1", "REG_INPUT_A_T2", "REG_INPUT_A_T3",
    "REG_INPUT_A_T4", "REG_INPUT_A_T5", "REG_INPUT_A_T6",
    "REG_INPUT_A_T7", "REG_INPUT_A_T8", "REG_INPUT_A_T9",
    "REG_INPUT_A_T10", "REG_INPUT_A_T11", "REG_INPUT_A_T12",
    "REG_INPUT_A_T13", "REG_INPUT_A_T14", "REG_INPUT_A_T15",
    "REG_INPUT_A_T16", "REG_INPUT_A_T17", "REG_INPUT_A_T18",
    "REG_INPUT_A_T19", "REG_INPUT_A_T20", "REG_INPUT_A_T21",
    "REG_INPUT_A_T22", "REG_INPUT_A_T23", "REG_INPUT_A_T24",
    "REG_INPUT_A_T25", "REG_INPUT_A_T26"
]

regs_a_holding = [
    "REG_HOLDING_A_T1", "REG_HOLDING_A_T2", "REG_HOLDING_A_T3",
    "REG_HOLDING_A_T4", "REG_HOLDING_A_T5", "REG_HOLDING_A_T6",
    "REG_HOLDING_A_T7", "REG_HOLDING_A_T8", "REG_HOLDING_A_T9",
    "REG_HOLDING_A_T10"
]

regs_a = {
    "REG_DISC_A_T1":   0x099B,

    "REG_COILS_A_T1":       0x0083,

    "REG_INPUT_A_T1":       0x1051,

    "REG_HOLDING_A_T1":     0x0082,
}

regs_b = {
    "REG_DISC_B_T1":        0x1000,

    "REG_COILS_B_T1"        0x0081,

    "REG_INPUT_B_T1":       0x1020,

    "REG_HOLDING_B_T1":     0x1FF7,
}
