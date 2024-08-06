import sys
from src.logger import logging

def get_error_message(error, error_detail: sys) -> str:
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in file '{file_name}' at line {line_number}: {error}"
    return error_message

class CardioPredictionException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        self.error_message = get_error_message(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message
