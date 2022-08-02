from datetime import datetime

def add_zero(date):
    return f"0{date}" if int(date) < 10 else date   

def data():
    d = datetime.now()
    return f"{add_zero(d.day)}.{add_zero(d.month)}.{d.year} {add_zero(d.hour)}:{add_zero(d.minute)}:{add_zero(d.second)}"