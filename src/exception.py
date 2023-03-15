import sys
import logging
from src.logger import logging

# custom exception handling in python documentation

def error_message_detial(error,error_detial:sys):
    _,_,exc_tb = error_detial.exc_info() #which file which line the execption or error will be given by this
    file_name = exc_tb.tb_frame.f_code.co_filename # gives the file name where the error occured 
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, 
        exc_tb.tb_lineno, # the line number in the file where error occurred
        str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message,error_detial:sys):
        super().__init__(error_message) # inherit the exception class ??
        self.error_message = error_message_detial(error_message,error_detial=error_detial)
    
    def __str__(self):
        return self.error_message