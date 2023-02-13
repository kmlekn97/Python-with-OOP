from types import TracebackType
from typing import Optional
from ExceptionType import ExceptionType

class MyExceptionClass(ExceptionType):
    def __init__(self,message,etype):
        super().__init__(etype)
        print(message)

    def with_traceback(self):
        print("Bu Benim Aritmatik Hatamdır")





