def foo(x, y = 0, z = 0):
    return 100*x + 10*y + 1*z

def bar(*args, named_parameter = 'BBAARR'):
    for arg in args:
        print(named_parameter, 'arg = ', arg)


bar()
bar(['the', 'list', 'of'])
bar(1, 2, 3)
bar([1, 2, 3])
bar('jelly', 'fish', named_parameter='separator')

'''
print(foo(1, 2, 3))
print(foo(z = 1, x=2, y=3))
print(foo(2, 7))
print(foo(7))
'''