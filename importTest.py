import ast
import astor

source = '''
import os
import tensorflow as tf
'''


i = 0;
parse_src = ast.parse(source)

for node in ast.walk(parse_src):
    i = i+1;
    if isinstance(node, ast.Import):
        alia = ast.alias('TensorFI', 'ti')
        aliaList = []
        aliaList.append(alia)
        importBody = ast.Import(aliaList)
        parse_src.body.insert(i, importBody)
        break

# print(ast.dump(parse_src))
print(astor.to_source(parse_src))