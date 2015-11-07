CC=gcc
CFLAGS=-g -O2 -Wall
LDFLAGS=

INCLUDE_DIRS=
LIBRARY_DIRS=
LIBS=-lmodbus

SOURCES=client.c
OBJECTS=$(SOURCES:.cpp=.o)
	EXECUTABLE=client

.PHONY: all

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS) 
	    $(CC) $(LDFLAGS) $(INCLUDE_DIRS) $(LIBRARY_DIRS) $(OBJECTS) -o $@ $(LIBS)

.cpp.o:
	    $(CC) $(CFLAGS) $(INCLUDE_DIRS) $< -o $@


.PHONY: clean

clean:
	rm -f *.o
	rm $(EXECUTABLE)
