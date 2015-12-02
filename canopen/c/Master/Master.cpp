/*
This file is part of CanFestival, a library implementing CanOpen Stack. 

Copyright (C): Edouard TISSERANT and Francis DUPIN

See COPYING file for copyrights details.

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
*/
#include <stdio.h>
#include <iostream>
#include <unistd.h>
extern "C"
{
#include "Master.h"
#include "OwnMaster.h"
}
extern s_BOARD MasterBoard;
/*****************************************************************************/
void MPU_MASTER_heartbeatError(CO_Data* d, UNS8 heartbeatID)
{
	eprintf("MPU_MASTER_heartbeatError %d\n", heartbeatID);
}

/********************************************************
 * ConfigureSlaveNode is responsible to
 *  - setup master RPDO 1 to receive TPDO 1 from id 2
 *  - setup master RPDO 2 to receive TPDO 2 from id 2
 ********************************************************/
void MPU_MASTER_initialisation(CO_Data* d)
{
	eprintf("MPU_MASTER_initialisation\n");
}

UNS8 ReadSDO(UNS8 nodeId, UNS16 index, UNS8 subIndex, UNS8 dataType, void* data, UNS8* size)
{
	UNS32 abortCode = 0;
	UNS8 res = SDO_UPLOAD_IN_PROGRESS;
	UNS32 sz = 0;
	UNS8 dat = 0;

	UNS8 err = readNetworkDict(&MPU_MASTER_Data, nodeId, index, subIndex, 0, 0);
	if (err)
	{
		printf("------>Can't readNetworkDict: %x\n", err);
		return 0xFF;
	}
	for(;;)
	{
		res = getReadResultNetworkDict(&MPU_MASTER_Data, nodeId, &dat, &sz, &abortCode);
		if (res != SDO_UPLOAD_IN_PROGRESS)
			break; 
		usleep(1000000);
		continue;
	}
	closeSDOtransfer(&MPU_MASTER_Data, nodeId, SDO_CLIENT);
	if (res == SDO_FINISHED)
		return 0;
	return 0xFF;
}

// Step counts number of times ConfigureSlaveNode is called
static int init_step = 0;

/*Froward declaration*/
static void ConfigureSlaveNode(CO_Data* d, UNS8 nodeId);

/**/
static void CheckSDOAndContinue(CO_Data* d, UNS8 nodeId)
{
	UNS32 abortCode;	
	if(getWriteResultNetworkDict (d, nodeId, &abortCode) != SDO_FINISHED)
		eprintf("Master : Failed in initializing slave %2.2x, step %d, AbortCode :%4.4x \n", nodeId, init_step, abortCode);

	/* Finalise last SDO transfer with this node */
	closeSDOtransfer(&MPU_MASTER_Data, nodeId, SDO_CLIENT);

	ConfigureSlaveNode(d, nodeId);
}

/********************************************************
 * ConfigureSlaveNode is responsible to
 *  - switch to operational mode
 *  - send NMT to slave
 ********************************************************
 * This an example of :
 * Network Dictionary Access (SDO) with Callback 
 * Slave node state change request (NMT) 
 ********************************************************
 * This is called first by MPU_MASTER_post_SlaveBootup
 * then it called again each time a SDO exchange is
 * finished.
 ********************************************************/
 
static void ConfigureSlaveNode(CO_Data* d, UNS8 nodeId)
{
	/* Put the master in operational mode */
	setState(d, Operational);

	/* Ask slave node to go in operational mode */
	masterSendNMTstateChange (d, nodeId, NMT_Start_Node);
}


void MPU_MASTER_preOperational(CO_Data* d)
{
	eprintf("MPU_MASTER_preOperational\n");
}


void CheckReadInfoSDO(CO_Data *d, UNS8 nodeid)
{
	UNS32 abortCode;
	UNS32 data=0;
	UNS32 size=64;

	if(getReadResultNetworkDict(&MPU_MASTER_Data, nodeid, &data, &size, &abortCode) != SDO_FINISHED)
		printf("Master : Failed in getting information for slave %2.2x, AbortCode :%4.4x \n", nodeid, abortCode);
	else
		printf("Addr       : %x\n", data);

	closeSDOtransfer(&MPU_MASTER_Data, nodeid, SDO_CLIENT);
}

void MPU_MASTER_operational(CO_Data* d)
{
	eprintf("MPU_MASTER_operational\n");
#if 0
//	while(1)
//	{
		eprintf("MPU_MASTER_operational\n");
	
		UNS8 res;
		UNS32 num = 0;
		UNS8 size;
		size = sizeof (num);
		//res = ReadSDO(0, 0x1280, 1, uint8, &num, &size);
		res = ReadSDO(1, 0x1018, 1, uint32, &num, &size);

		printf("Read number of entries: %d\n", num);

		sleep(10);
//	}
	while (1){}
#endif
	readNetworkDictCallback(&MPU_MASTER_Data, 1, 0x1018, 0x00, uint8, CheckReadInfoSDO, 0);
}

void MPU_MASTER_stopped(CO_Data* d)
{
	eprintf("MPU_MASTER_stopped\n");
}

void MPU_MASTER_post_sync(CO_Data* d)
{
	eprintf("MPU_MASTER_stopped\n");
}

void MPU_MASTER_post_emcy(CO_Data* d, UNS8 nodeID, UNS16 errCode, UNS8 errReg)
{
	eprintf("Master received EMCY message. Node: %2.2x  ErrorCode: %4.4x  ErrorRegister: %2.2x\n", nodeID, errCode, errReg);
}

char query_result = 0;
char waiting_answer = 0;

static void CheckSDO(CO_Data* d, UNS8 nodeId)
{
	UNS32 abortCode;	
	if(getWriteResultNetworkDict (d, nodeId, &abortCode) != SDO_FINISHED)
		eprintf("Master : Failed in changing Slave's transmit type AbortCode :%4.4x \n", abortCode);

	/* Finalise last SDO transfer with this node */
	closeSDOtransfer(&MPU_MASTER_Data, nodeId, SDO_CLIENT);
}


void MPU_MASTER_post_TPDO(CO_Data* d)
{
}

void MPU_MASTER_post_SlaveBootup(CO_Data* d, UNS8 nodeid)
{
	eprintf("MPU_MASTER_post_SlaveBootup %x\n", nodeid);
	std::cout << "MPU_MASTER_post_SlaveBootup. Node id: " << nodeid << std::endl;

	/* log bootup node id */
	ConfigureSlaveNode(d, nodeid);
}
