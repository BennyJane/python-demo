# flask 源码
methods = ['get']
required_methods = ['post']

# methods = 0
# required_methods = 1
methods |= required_methods
print(methods)