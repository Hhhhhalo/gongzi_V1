from datetime import datetime


def check_answer(answer_list):
    for item in answer_list:
        if item.upper() not in ["A", "B", "C", "D"]:
            return False
    return True

def format_datetime(date):
    return date.strftime("%Y-%m-%d %H:%M:%S")

def str2datetime(date, format="%Y-%m-%d %H:%M:%S"):
    pass




    return datetime.strptime(date, format)
