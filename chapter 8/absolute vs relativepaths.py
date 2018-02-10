import os
print(os.path.abspath('.'))
print(os.path.abspath('.\\Scripts'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))
path='C:\\ramesh-home\\PycharmProjects\\python_learning\\chapter 8'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))