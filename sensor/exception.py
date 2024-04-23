import sys
import os

def error_message_detail(error, error_detail:sys):
    """
    Extracts details of the error including file name, line number, and error message.
    
    Args:
        error: The error message.
        error_detail: The system-specific error detail.

    Returns:
        str: A formatted error message containing file name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename

    error_message = "An Error occurred.\nDetails: File Name: {0}, Line Number: {1}, Error: {2}".format(
    filename, exc_tb.tb_lineno, str(error))
    return error_message


class SensorException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)

        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
