#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    if name is None:
        return 'Hello, World!'
    elif name != '':
        return 'Hello, %s!' %name    
    else:
        return 'Hello, World!'
