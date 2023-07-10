import sys
from analyzer import toolbox

def start():
    '''
    Initialize Toolbox object
    '''
    return toolbox.Toolbox()

def get_input():
    '''
    Get user input (values as arguments in command line,
    analysis function in seperate input)
    '''
    print("Input values (sperated by blank space): ", sys.argv)
    values = [float(i) for i in sys.argv[1:]]

    print('''Input calculation function
          mean --> mean
          standard deviation --> std
          median --> median
          quantile n-th --> quantile n
          percentile n% --> percentile n
          inter quartile range --> iqr
          ''')
    calc_func_input = [i for i in input().split(' ')]

    return values, calc_func_input

def calculate(tb, values, calc_func_input):
    '''
    Call calculation function on values
    '''
    if len(calc_func_input) == 1:
        method = calc_func_input[0]
        arg = None
    elif len(calc_func_input) == 2:
        method = calc_func_input[0]
        arg = int(calc_func_input[1])
    op = getattr(tb, method, None)

    if callable(op):
        args = [values, arg]
        op(*[a for a in args if a is not None])
        return getattr(tb, '_' + method, None)
    else:
        raise(TypeError)


if __name__ == "__main__":
    tb = start()
    val, func = get_input()
    result = calculate(tb, val, func)
    print(result)
