import ast
import astor

def addImport(fPath):

    i = 0;
    parse_src = ast.parse(open(fPath).read())

    for node in ast.walk(parse_src):
        i = i+1;
        if isinstance(node, ast.Import):
            alia = ast.alias('TensorFI', 'ti')
            aliaList = []
            aliaList.append(alia)
            importBody = ast.Import(aliaList)
            parse_src.body.insert(i, importBody)
            break

    print(ast.dump(parse_src))
    print(astor.to_source(parse_src))

if __name__ == '__main__':
    addImport('astTest.py')