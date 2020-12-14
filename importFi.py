import ast
import astor

# TODO: Add some configuration in this process to workflow
# TODO: Can the ast find the previous variable?

source1 = '''
fi = ti.TensorFI(sess,
                configFileName = 'default.yaml',
                logLevel = 50,
                disableInjections=False,
                name = "convolutional",
                fiPrefix = 'fi_')
'''

source = '''
fi = ti.TensorFI(sess)
'''

sessName = ast.Name("sess", ast.Load())
sessNameList = []
sessNameList.append(sessName)
tiName = ast.Name('ti', ast.Load())
fiName = ast.Name('fi', ast.Store())
fiNameList = []
fiKeyList = []
fiNameList.append(fiName)
confKey = ast.keyword('configFileName', ast.Str('default.yaml'))
logKey = ast.keyword('logLevel', ast.Num(50))
disaKey = ast.keyword('disableInjections', ast.Name('False', ast.Load()))
nameKey = ast.keyword('name', ast.Str('convolutional'))
preKey = ast.keyword('fiPrefix', ast.Str('fi_'))
fiKeyList.append(confKey)
fiKeyList.append(logKey)
fiKeyList.append(disaKey)
fiKeyList.append(preKey)
tiAttr = ast.Attribute(tiName, 'TensorFI', ast.Load())
tiCall = ast.Call(tiAttr, sessNameList, fiKeyList, None, None)
tiBody = ast.Assign(fiNameList, tiCall)

# print(ast.dump(ast.parse(source1)))
print(astor.to_source(tiBody))




