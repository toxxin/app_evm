#include <stdlib.h>
#include <stdio.h>
#include <modbus/modbus.h>
#include <modbus/modbus-rtu.h>

int main(void)
{
	modbus_t *ctx = modbus_new_rtu("/dev/pts/30", 19200, 'N', 8, 1);
	if (!ctx) {
		fprintf(stderr, "Failed to create the context:\n");
		exit(1);
	}

	if (modbus_connect(ctx) == -1) {
		fprintf(stderr, "Unable to connect:\n");
		modbus_free(ctx);
		exit(1);
	}

	modbus_set_slave(ctx, 0x20);

	uint16_t reg[3];

	int num = modbus_read_input_registers(ctx, 0x1053, 3, reg);
	if (num != 3) {
		fprintf(stderr, "Failed to read:\n");
	} else {
		printf("val1 = %d\nval2 = %d\nval3 = %d\n", reg[0], reg[1], reg[2]);
	}

	modbus_close(ctx);
	modbus_free(ctx);

	return 0;
}

