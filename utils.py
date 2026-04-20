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
    

def validate_priority(priority):
    if priority in ['low','medium','high']:
        return True
    else:
        return False

    
    

