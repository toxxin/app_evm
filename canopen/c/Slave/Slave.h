#include "TestSlave.h"

void MPU_SLAVE_heartbeatError(CO_Data* d, UNS8);

UNS8 MPU_SLAVE_canSend(Message *);

void MPU_SLAVE_initialisation(CO_Data* d);
void MPU_SLAVE_preOperational(CO_Data* d);
void MPU_SLAVE_operational(CO_Data* d);
void MPU_SLAVE_stopped(CO_Data* d);

void MPU_SLAVE_post_sync(CO_Data* d);
void MPU_SLAVE_post_TPDO(CO_Data* d);
void MPU_SLAVE_storeODSubIndex(CO_Data* d, UNS16 wIndex, UNS8 bSubindex);
void MPU_SLAVE_post_emcy(CO_Data* d, UNS8 nodeID, UNS16 errCode, UNS8 errReg);
