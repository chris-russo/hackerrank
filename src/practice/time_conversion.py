from datetime import datetime


# https://www.hackerrank.com/challenges/time-conversion/problem
def time_conversion(t: str, input_fmt: str = '%I:%M:%S%p',
                    output_fmt: str = '%H:%M:%S') -> str:
    return datetime.strptime(t, input_fmt).strftime(output_fmt)
