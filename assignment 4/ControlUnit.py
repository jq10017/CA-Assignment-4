class ControlUnit:
    def __init__(self):
        pass

    def generate_signals(self, opcode, function_field=None):
        signals = {
            'alu_op': None,
            'invert_a': False,
            'invert_b': False,
            'reg_write': True 
        }
        if opcode == 'SUB':
            signals['alu_op'] = 'sub'
        elif opcode == 'AND':
            signals['alu_op'] = 'and'
            if function_field == 'INV':
                signals['invert_a'] = True 
        elif opcode == 'OR':
            signals['alu_op'] = 'or'
            if function_field == 'INV':
                signals['invert_a'] = True
        return signals