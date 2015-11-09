
CC = arm-none-linux-gnueabi-gcc
CXX = /home/anton/Distrib/arm-2013.05/bin/arm-none-linux-gnueabi-g++
LD = /home/anton/Distrib/arm-2013.05/bin/arm-none-linux-gnueabi-g++
OPT_CFLAGS = -O2
CFLAGS = $(OPT_CFLAGS)
PROG_CFLAGS = -DEBUG_WAR_CONSOLE_ON -g
EXE_CFLAGS =  -lpthread -lrt -ldl
OS_NAME = Linux
ARCH_NAME = arm
PREFIX = arm-none-linux-gnueabi-
TARGET = unix
CAN_DRIVER = can_socket
TIMERS_DRIVER = timers_unix
TESTMASTER = "OwnMaster"

INCLUDES = -I./include -I./include/$(TARGET) -I./include/$(CAN_DRIVER) -I./include/$(TIMERS_DRIVER)

MASTER_OBJS = TestMaster.o OwnMaster.o Master.o

OBJS = $(MASTER_OBJS) ./libs/libcanfestival.a ./libs/libcanfestival_$(TARGET).a

ifeq ($(TIMERS_DRIVER),timers_rtai)
	PROGDEFINES = -DUSE_RTAI
endif

all: $(TESTMASTER)

../../drivers/$(TARGET)/libcanfestival_$(TARGET).a:
	$(MAKE) -C ../../drivers/$(TARGET) libcanfestival_$(TARGET).a


$(TESTMASTER): $(OBJS)
	$(LD) $(CFLAGS) $(PROG_CFLAGS) ${PROGDEFINES} $(INCLUDES) -o $@ $(OBJS) $(EXE_CFLAGS)
	
TestMaster.c: TestMaster.od
	$(MAKE) -C ../../objdictgen gnosis
	#python ../../objdictgen/objdictgen.py TestMaster.od TestMaster.c

%.o: %.c
	$(CC) $(CFLAGS) $(PROG_CFLAGS) ${PROGDEFINES} $(INCLUDES) -o $@ -c $<

%.o: %.cpp
	$(CXX) $(CFLAGS) $(PROG_CFLAGS) ${PROGDEFINES} $(INCLUDES) -o $@ -c $<

clean:
	rm -f $(MASTER_OBJS)
	rm -f $(TESTMASTER)
