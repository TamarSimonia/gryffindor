oper = input('please enter an argument: ')

def conductAnOperation(x):
    result = eval(x)
    return result

print(oper, "=", conductAnOperation(oper))
