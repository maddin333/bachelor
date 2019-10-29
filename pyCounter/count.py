import re

# pattern = re.compile(r'\n*\* (\w*)\n')
#errorClassesDict = {'mysql','duplicateFunctionParameter','arrayValueByReference','magic_quotes_runtime','list','ereg','split','oldClassConstructors','static','variableInterpolation','foreachByReference','arrayValueByReference','newOperatorWithReference','pregEval'}
pattern = re.compile(r'(mysql|duplicateFunctionParameter|arrayValueByReference|magic_quotes_runtime|list\(|ereg|split|oldClassConstructors|static|variableInterpolation|foreachByReference|arrayValueByReference|newOperatorWithReference|pregEval)')
#linePattern = '\* deprecatedFunctions(\s.*\n)+\n'
count = {}

# add found errorClasses to Dict. If already present, increase counter
def addToDict(errorClass):
    if errorClass in count:
        count[errorClass] += 1
    else:
        count[errorClass] = 1

# helper to print dictionary
def prettyPrint(dictToPrint):
    for key in dictToPrint:
        print(f'{key}: {dictToPrint[key]}')

with open('report.md', 'r') as file:
    text = file.read()
    data = re.findall(pattern, text)
    for errorClass in data:
        addToDict(errorClass)
    prettyPrint(count)

