import sys
import logging
from src.logger import logging

def get_error_info(error,error_info:sys):
    _,_,exc_tb = error_info.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line = exc_tb.tb_lineno
    error_message = f"The error occured in {file_name} at line no {line} with {str(error)} error message"
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_info:sys):
        super().__init__(error_message)
        self.error_message = get_error_info(error_message,error_info = error_info)
        

    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomException(e,sys)