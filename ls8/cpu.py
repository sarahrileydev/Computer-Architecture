"""CPU functionality."""

import sys

PRN = 0b01000111
LDI = 0b10000010
HLT = 0b00000001


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        pass
        # Add 256 bytes of memory and
        # 8 general-purpose registers
        # Also add properties for any internal registers you need, e.g. PC

        # init ram
        self.ram = [0] * 255
        # init registers
        self.reg = [0] * 8
        # pointer position 0 at the ram
        self.pc = 0

    def ram_read(self, read_address):
        return self.ram[read_address]

    def ram_write(self, write_value, write_address):
        self.ram[write_address] = write_value

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        while True:
                ir = self.ram[self.pc]
                op_A = self.ram_read(self.pc + 1)
                op_B = self.ram_read(self.pc + 2)

                if ir == LDI:
                    self.reg[op_A] = op_B
                    self.pc += 3
                elif ir == PRN:
                    print(self.reg[op_A])
                    self.pc += 2
                elif ir == HLT:
                    break
                    sys.exit(1)
