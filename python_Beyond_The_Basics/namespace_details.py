"""Information on Namespace

when we write a import following happen under the hood
viz. import abc
1. Scan SYS.PATH and find directory with same name(abc) with __init__.py file.
execute the __init__.py file
2. If Step 1 is unsuccessful look for a file  with .py extension per import
viz. abc.py
3. If Step 2 is unsuccessful load all the directory with the given name which does
not have __init__.py file in them as namespace package.
i.e. if we have d:\py_proj\test1\abc and d:\py_proj\test2\abc
both are loaded but nothing is executed.

Thus, namespace package are directories without __init__.py file"""