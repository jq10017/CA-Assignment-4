from MUX import mux2
from ALU import ALU
from RegisterFile import RegisterFile
from ControlUnit import ControlUnit

class SingleCycleProcessor:
    def __init__(self):
        self.pc = 0  
        self.registers = RegisterFile()
        self.instruction_memory = []  
        self.alu = ALU()
        self.control = ControlUnit()

    def load_instructions(self, instructions):
        self.instruction_memory = instructions

    def run(self):
        while self.pc < len(self.instruction_memory):
            instruction = self.instruction_memory[self.pc]
            self.execute(instruction)
            self.pc += 1  

    def execute(self, instruction):
        parts = instruction.split()
        opcode = parts[0]
        rd = int(parts[1][1:])
        rs = int(parts[2][1:])
        rt = int(parts[3][1:]) if len(parts) > 3 else None
        function_field = parts[4] if len(parts) > 4 else None

        signals = self.control.generate_signals(opcode, function_field)
        a_input = mux2(signals['invert_a'], self.registers.registers[rs], ~self.registers.registers[rs])
        b_input = mux2(signals['invert_b'], self.registers.registers[rt], ~self.registers.registers[rt])

        if signals['alu_op'] == 'sub':
            result = self.alu.sub(a_input, b_input)
        elif signals['alu_op'] == 'and':
            result = self.alu.and_op(a_input, b_input)
        elif signals['alu_op'] == 'or':
            result = self.alu.or_op(a_input, b_input)
        else:
            raise ValueError(f"Unknown ALU op: {signals['alu_op']}")

        if signals['reg_write']:
            self.registers.registers[rd] = result