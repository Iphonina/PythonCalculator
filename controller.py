import model
import view
import operation
import logger

def start():
    some_str = view.inp()
    a, b, op = operation.oper(some_str)
    if op == '+':
        result = model.summma(a, b)
    elif op == '-':
        result = model.diff(a, b)
    elif op == '*':
        result = model.mult(a, b)
    else:
        result = model.div(a, b)
    logger.log(a, b, op, result)
    view.view_data(result)