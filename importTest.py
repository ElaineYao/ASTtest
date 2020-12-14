import ast

importSource = '''
import TensorFI as ti
'''

'''
Module(body=[Import(names=[alias(name='Tensorfi', asname='ti')])])
'''
# Ways to insert 'import TensorFI as ti'
alia = ast.alias(ast.Str('TensorFI'). ast.Str('ti'))
importBody = ast.Import(alia)

# TODO : find places automatically

print(ast.dump(ast.parse(importBody)))