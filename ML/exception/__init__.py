import os
import sys

class MLException(Exception):
    def __init__(self, error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message = MLException.get_detailed_error_message(error_message=error_message,error_detail=error_detail)

    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys) -> str:
        _,_,exec_tb = error_detail.exc_info()
        line_num = exec_tb.tb_frame.f_lineno
        filename = exec_tb.tb_frame.f_code.co_filename

        error_message = f"Error occured in script: [{filename}] at line number [{line_num}] error_message is : [{error_message}]"

        return error_message

    def __str__(self) -> str:
        return self.error_message

    def __repr__(self) -> str:
        return MLException.__name__.str()