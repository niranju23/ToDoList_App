from datetime import datetime

def validate_date(due_date):
    try:
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        today = datetime.now().date()
        if parsed_date >= today:
            return True
        else:
            return False
    except:
        return False
    

