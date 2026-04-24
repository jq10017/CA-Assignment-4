from SingleCycleProcessor import SingleCycleProcessor

if __name__ == "__main__":
    processor = SingleCycleProcessor()
    instructions = [
        "AND $4 $0 $1",      
        "AND $6 $2 $3 INV",  
        "OR $0 $4 $6",       
]
    processor.load_instructions(instructions)
    processor.registers.registers[0] = 0b10    
    processor.registers.registers[1] = 0b100   
    processor.registers.registers[2] = 0b110   
    processor.registers.registers[3] = 0b1000  
    processor.registers.registers[4] = 0
    processor.registers.registers[5] = 0
    processor.registers.registers[6] = 0
    
    print("Initial registers:", processor.registers.registers)
    print("\nExecution trace:")
    
    for pc in range(len(instructions)):
        instruction = instructions[pc]
        print(f"\nInstruction {pc}: {instruction}")
        
        parts = instruction.split()
        opcode = parts[0]
        function_field = parts[4] if len(parts) > 4 else None
        signals = processor.control.generate_signals(opcode, function_field)
        print(f"Control signals: {signals}")
        
        processor.execute(instruction)
        print(f"Registers after: {processor.registers.registers}")
    
    print(f"\nFinal output (Y, assuming $0): {processor.registers.registers[0]}")