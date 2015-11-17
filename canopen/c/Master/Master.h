#include "TestMaster.h"

void MPU_MASTER_heartbeatError(CO_Data* d, UNS8);

UNS8 MPU_MASTER_canSend(Message *);

void MPU_MASTER_initialisation(CO_Data* d);
void MPU_MASTER_preOperational(CO_Data* d);
void MPU_MASTER_operational(CO_Data* d);
void MPU_MASTER_stopped(CO_Data* d);

void MPU_MASTER_post_sync(CO_Data* d);
void MPU_MASTER_post_TPDO(CO_Data* d);
void MPU_MASTER_post_emcy(CO_Data* d, UNS8 nodeID, UNS16 errCode, UNS8 errReg);
void MPU_MASTER_post_SlaveBootup(CO_Data* d, UNS8 nodeid);
