import sys

def get_error_message(error_message: Exception,error_details: sys):
        _,__,exc_tb = error_details.exc_info()
        filename = exc_tb.tb_frame.f_code.co_filename
        linenumber = exc_tb.tb_lineno
        
        error_message = f"""
        Exception occured in script file {filename},
        line numer {linenumber},
        error message is {str(error_message)}
        """
        
        return error_message

class CustomException(Exception):
    def __init__(self,error_message: Exception,error_details : sys):
        self.error_details = error_details
        self.error_message = get_error_message(error_message=error_message,
                                                error_details=self.error_details)
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return self.error_message