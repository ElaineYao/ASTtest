#/usr/bin/python

import ast

expr = '''
... import tensorflow as tf
... import sys
... node2 = tf.constant(4, dtype=tf.float64)
... node3 = tf.add(node1, node2, name = 'add1')
... '''
expr_ast = ast.parse(expr)
ast.dump(expr_ast)

# Output of ast.dump
'''
Module(
    body=[
        Import(names=[alias(name='tensorflow', asname='tf')]),
        Import(names=[alias(name='sys', asname=None)]),
        Assign(targets=[Name(id='node2', ctx=Store())],
               value=Call(func=Attribute(value=Name(id='tf', ctx=Load()),
                                         attr='constant',
                                         ctx=Load()),
                          args=[Num(n=4)],
                          keywords=[keyword(arg='dtype', value=Attribute(value=Name(id='tf', ctx=Load()), attr='float64', ctx=Load()))],
                          starargs=None,
                          kwargs=None)),
        Assign(targets=[Name(id='node3', ctx=Store())],
               value=Call(func=Attribute(value=Name(id='tf', ctx=Load()),
                                         attr='add',
                                         ctx=Load()),
                          args=[Name(id='node1', ctx=Load()), Name(id='node2', ctx=Load())],
                          keywords=[keyword(arg='name', value=Str(s='add1'))],
                          starargs=None,
                          kwargs=None))])
'''
# Output of print(expr_ast.__dict__)
# TODO: How to find the place and add the line
# TODO: Next steps: 1. Read the official documentation - find out how to add code and generate the code that I want
# TODO: 2. Parse more code and get familiar with it. 3. Find out how to set the python file/ code as the input


{'body':
     [<_ast.Import object at 0x7fe91f37a550>,
      <_ast.Import object at 0x7fe91f37a5d0>,
      <_ast.Assign object at 0x7fe91f37a690>,
      <_ast.Assign object at 0x7fe91f37a890>]}
